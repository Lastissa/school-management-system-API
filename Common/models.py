from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import logging, random, time

logger = logging.getLogger(__name__)

class SchemaManager(BaseUserManager):
    def _blueprint(self, email, role, password= None, user_key= None, **kwargs):
        #   =================================================
        #   By default
        #   User_key cannot be set by user but cos of special people like management account creation
        #   they can set user_key
        #   =================================================
        if not email: raise ValueError("Email is req")
        if not role: raise ValueError("role is req")
        if role not in ['ADMIN', 'MANAGEMENT', 'TEACHING_STAFF', 'NON_TEACHING_STAFF', 'STUDENT', 'PARENT']:
            logger.error(msg=f"{email} tried to set an invalid role {role}")
            raise ValueError(f'{role} is INVALID')
        if not user_key:
        #   =================================================
            # Set a temp user key
        #   =================================================
            user_key= role[:2] +str(time.time_ns()+random.randint(1,10)).replace('.', '')[-4:] #TE9999 or NO9999 , ALso might hit duplicate issue but this will be rare
            
        #   -------------------------------------------------------------------------------
        #   ALSO TO INCREASE SECURTIY, ENFORCE A FIXED PREFIX FOR MNGT
        print(user_key)
        if user_key[:2].upper() != role[:2]: raise ValueError("For security, this naming of user_key does not follow standard convection, refer to developer for detail")
        #   -------------------------------------------------------------------------------
        
        instance = self.model(email=email.upper(), role=role, user_key=user_key.upper(), **kwargs)
        if not password: 
            logger.info(msg=f"{email} set no password on account creation")
            instance.set_unusable_password()
        else:
            logger.info(msg=f"{email} set a password on account creation")
            instance.set_password(password)
        instance.save(using=self._db)
        return instance
    
    def create_admin(self, email, password):
        user = self._blueprint(email = email, password = password, role = "ADMIN", is_staff=True, is_superuser=True,is_active=True,email_verified=True)
        return user
    
    def create_interested_applicant(self, email, password):
        #=====================================================
        #   This for enrolling interested students into the system
        #=====================================================
        user = self._blueprint(email = email, password = password, role = "STUDENT")
        return user
    def create_mngt_accout(self, email, password, user_key= None):
         #=====================================================
        #   This for enrolling mngt into the system by the admins
        #=====================================================
        user = self._blueprint(email = email, password = password, role = "MANAGEMENT", user_key= user_key, is_active= True, is_mngt=True, email_verified=True)
        return user
        
class Schema(AbstractBaseUser):
    #--------- main one needed for Auth------
    email = models.EmailField(blank=False, null= False, unique=True)
    user_key = models.CharField(max_length=50, db_index=True, unique=True) #Blank on first because email is used 
    
    USERNAME_FIELD = 'user_key'
    REQUIRED_FIELDS = []
    ##############################################################
    # FOR DJANGO ADMIN
    def has_module_perms(self, app_label):return self.is_superuser
    def has_perm(self, app_label):return self.is_superuser
    ############################################################## 
    
    def __str__(self):
        return self.user_key + f" Active: {self.is_active}"
    objects = SchemaManager()
    
    # --- ROLE AND SECURITY PHERIPHERALS ; ---
    role_choice=[
        ('ADMIN', 'Admin'),
        ('MANAGEMENT', 'Management'),
        ('TEACHING_STAFF', 'Teaching Staff'),
        ('NON_TEACHING_STAFF', 'Non Teaching Staff'),
        ('STUDENT', 'Student'),
        ('PARENT', 'Parent'),
    ]
    ###############################################
    #   EVEN THOUGH ROLE ALREADY EXIST
    #   I USED THE IS_MNGT & IS_STAFF FOR PERMISSION CLASSES
    #   WHILE ROLES SERVE AS THE REAL GATEWAY FOR ACCESS
    ###############################################
    role = models.CharField(max_length=20, choices=role_choice, blank=False, null=False, db_index=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_mngt = models.BooleanField(default=False)                        # Models for management
    is_active = models.BooleanField(default=False)                      # Mngt should be the one to change status
    email_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    

#Will move to the student app
class StudentProfile(models.Model):
    #Data Incoming from the school that will use it, get to be set only after interestee have walked down to the school 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    year_of_birth = models.DateField()
    
    
    
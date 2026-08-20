from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import logging, random, time

logger = logging.getLogger(__name__)

class SchemaManager(BaseUserManager):
    def _blueprint(self, email, role, password= None, *args, **kwargs):
        if not email: raise ValueError("Email is req")
        if not role: raise ValueError("role is req")
        if role not in ['ADMIN', 'MANAGEMENT', 'TEACHING_STAFF', 'NON_TEACHING_STAFF', 'STUDENT', 'PARENT']:
            logger.error(msg=f"{email} tried to set an invalid role {role}")
            raise ValueError(f'{role} is INVALID')
        temp_user_key= role[:2] +str(time.time_ns()+random.randint(1,10)).replace('.', '')[-4:] #TE9999 or NO9999 
        instance = self.model(email=email, role=role, user_key=temp_user_key, *args, **kwargs)
        if not password: 
            logger.info(msg=f"{email} set no password on account creation")
            instance.set_unusable_password()
        else:
            logger.info(msg=f"{email} set a password on account creation")
            instance.set_password(password)
        instance.save(using=self._db)
        return instance
    
    def create_admin(self, email, password, *args, **kwargs):
        user = self._blueprint(email = email, password = password, role = "ADMIN", is_staff=True, is_superuser=True,is_active=True,email_verified=True, *args, **kwargs)
        return user
        
class Schema(AbstractBaseUser):
    #--------- main one needed for Auth------
    email = models.EmailField(blank=False, null= False, unique=True)
    user_key = models.CharField(max_length=50, db_index=True, unique=True) #Blank on first because email is used 
    
    USERNAME_FIELD = 'user_key'
    REQUIRED_FIELDS = []
    ##############################################################
    # FOR DJANGO ADMIN
    def has_module_perms(self, app_label):
        print("ahs module perm is being used", self.is_superuser)
        return self.is_superuser
    def has_perm(self, app_label):
        print( "has_perm is being used", self.is_superuser)
        return self.is_superuser
    ############################################################## 
    
    def __str__(self):
        return self.user_key + f" Active: {self.is_active}"
    objects = SchemaManager()
    
    # --- ROLE AND SECURITY PHERIPHERALS ---
    role_choice=[
        ('ADMIN', 'Admin'),
        ('MANAGEMENT', 'Management'),
        ('TEACHING_STAFF', 'Teaching Staff'),
        ('NON_TEACHING_STAFF', 'Non Teaching Staff'),
        ('STUDENT', 'Student'),
        ('PARENT', 'Parent'),
    ]
    role = models.CharField(max_length=20, choices=role_choice, blank=False, null=False, db_index=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_mngt = models.BooleanField(default=False)                        # Models for management
    is_active = models.BooleanField(default=True)
    email_verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    

#Will move to the student app
class StudentProfile(models.Model):
    #Data Incoming from the school that will use it, get to be set only after interestee have walked down to the school 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    other_name = models.CharField(max_length=100)
    year_of_birth = models.DateField()
    
    
    
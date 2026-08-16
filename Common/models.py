from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import logging

logger = logging.getLogger(__name__)

class SchemaManager(BaseUserManager):
    def _blueprint(self, email, role, password= None, *args, **kwargs):
        if not email: raise ValueError("Email is req")
        if not role: raise ValueError("role is req")
        if role not in ['ADMIN', 'MANAGEMENT', 'TEACHING_STAFF', 'NON_TEACHING_STAFF', 'STUDENT', 'PARENT']:
            logger.error(msg=f"{email} tried to set an invalid role {role}")
            raise ValueError(f'{role} is INVALID')
        istance = self.model(email=email, role=role)
        if not password: 
            logger.info(msg=f"{email} set no password on account creation")
            istance.set_unusable_password(0)
        else:
            logger.info(msg=f"{email} set a password on account creation")
            istance.set_password(password)
        return istance
    
    def create_admin(self, email, password, *args, **kwargs):
        user = self._blueprint(email, password, role = "ADMIN" *args, **kwargs)
        user.save()
        
class Schema(AbstractBaseUser):
    #--------- main one needed for Auth------
    email = models.EmailField(blank=False, null= False, unique=True)
    user_key = models.CharField(max_length=50, blank=True, null = True, db_index=True, unique=True) #Blank on first because email is used 
    
    USERNAME_FIELD = 'user_key'
    REQUIRED_FIELDS = []
    
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
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_mngt = models.BooleanField(default=False)                        # Models for management
    is_active = models.BooleanField(default=True)
    email_verified = False
    date_created = models.DateTimeField(auto_now_add=True)
        
        
        

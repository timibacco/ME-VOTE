
'''from django.urls import reverse
import uuid

class ElectoralProcess(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique= True, max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    link = models.SlugField(unique=True)

    def get_absolute_url(self):
        return reverse('process_detail', args=[str(self.link)])'''

from Elections.models import ElectoralProcess
from django.contrib.auth.models import AbstractUser, Group, Permission,User, PermissionsMixin,BaseUserManager
from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model







class participantUserManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
       

        if not email:
            raise ValueError('The Email field must be set')
        extra_fields.setdefault('is_voter',True)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_super_official',True)
        return self.create_user(email, password, **extra_fields)

class Participant(AbstractUser):
    class Meta:
        permissions = [
#            ('delete_participant', 'Can delete participants'),
            ('end_election', 'Can end election'),
#            ("add_participant", "Can add a new participant"),
            ("start_election", "Can start election"),
            ("grant_offical_perm", "Can permit to be an official"),
            ("can_vote", "can vote in election"),
#           ("can_go_dehradoon", "Trip to Dehradoon"),
#          ("can_go_mussoorie", "Trip to Mussoorie"),
#         ("can_go_haridwaar", "Trip to Haridwaar"),
    #        ("can_go_rishikesh", "Trip to Rishikesh"),
        ]
    #username_validator = UnicodeUsernameValidator()
    #uuid = 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=128, null=False, blank=False)
    email = models.EmailField(unique= True, blank=False, null=False,)
 
    electoral_process = models.ForeignKey(ElectoralProcess,null= True, on_delete=models.CASCADE ,help_text ="What election is the user involved in?")
    is_voter = models.BooleanField(default=False)
    is_official = models.BooleanField(default=False)
    is_super_official = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add= True, default = timezone.now)
    groups = models.ManyToManyField(Group)

    is_active = models.BooleanField(default=True)

    objects= participantUserManager()
    message = f"Welcome onboard{first_name + last_name},\nYou're now one step closer to be verified. Follow the link below to be verified.\n\n Sincerely,\nMeVote"
    EMAIL_FIELD = 'email' 
    USERNAME_FIELD = 'email'
    
    REQUIRED_FIELDS = ["first_name",
                       "last_name",
                       "username",
                       ]
    def email_user(self):
        message = self.message 
        return super().email_user(subject='Profile creation',message= message, from_email='osabayomi@student.oauife.edu.ng')
    def __str__(self):
        return self.get_full_name 
    
    
    
       


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, email, password=None, is_staff=False, is_admin=False):
        if not email:
            raise ValueError('User must have an email address')
        if not password:
            raise ValueError('User must have a password')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(email, password=password)
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user


class UserProfile(AbstractBaseUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, max_length=100, null=True, verbose_name='email address')
    profile_pic = models.ImageField(upload_to='accounts/media/%Y/%m/%d', blank=True)
    address = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=15, null=True)
    postal_code = models.CharField(max_length=15, null=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserProfileManager()

    def get_username(self):
        return self.email

    def get_fullname(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name
        else:
            return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return self.get_fullname()

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

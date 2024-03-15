from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import datetime
from django.template.defaultfilters import slugify

# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError('User must provide and email address')
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self, email, name, password):
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
        
        
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    phone = models.CharField(max_length=13)
    is_staff = models.BooleanField(default=False)
    is_alumni = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    visitors = models.BooleanField(default=True, null=True)
    
    objects = UserAccountManager()
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return f"Email => {self.name}"
    
    
    
    
    
""" 
Blog application backend modeling for NFCS blog platform ### NFCS EXCOS, 27th Nov. 2023
"""
class Categories(models.TextChoices):
    NFCS = 'nfcs',
    CATECHISM = "catechism",
    LIFE_OF_SAINTS = "life_of_saints",
    SCHOOL = "school",
    ACCOMMODATION = "accommodation",
    ALUMNI = "alumni",
    EXAMS = "exams",
    PIOUS_SOCIETY = 'pious_society',
    CHAPLAINCY = 'chaplaincy',
    BIBLE = 'bible',
    EUCHARIST = "eucharist",
    
    
class BlogPost(models.Model):
    title = models.CharField(max_length=75)
    slug = models.SlugField()
    category = models.CharField(max_length=75, choices=Categories.choices, default=Categories.NFCS)
    excerpt = models.CharField(max_length=150)
    month = models.CharField(max_length=3)
    day = models.CharField(max_length=2)
    content = models.TextField()
    featured = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True, null=True)
    thumbnail1 = models.ImageField(upload_to="Photos/%Y/%m/%d", null=True, blank=True)
    thumbnail2 = models.ImageField(upload_to="Photos/%Y/%m/%d", null=True, blank=True)
    thumbnail3 = models.ImageField(upload_to="Photos/%Y/%m/%d", null=True, blank=True)
    thumbnail4 = models.ImageField(upload_to="Photos/%Y/%m/%d", null=True, blank=True)
    thumbnail5 = models.ImageField(upload_to="Photos/%Y/%m/%d", null=True, blank=True)
    
    def save(self, *args, **kwargs):
        original_slug = slugify(self.title)
        queryset = BlogPost.objects.all().filter(slug__iexact=original_slug).count()
        
        count = 1
        slug = original_slug
        while(queryset):
            slug = original_slug + '-' + str(count)
            count += 1
            queryset = BlogPost.objects.all().filter(slug__iexact=slug).count()
        
        self.slug = slug
        
        if self.featured:
            try:
                temp = BlogPost.objects.filter(featured=True)
                if self != temp:
                    temp.featured = False
                    # temp.save()
                
            except BlogPost.DoesNotExist:
                pass 
        
        super(BlogPost, self).save(*args, **kwargs)
    
    def __str__(self):
        return f':=> {self.title}'
    
    
    
    
    
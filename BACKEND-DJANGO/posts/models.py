from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def projectFile(instance, filename):
    return '/'.join(['projectPhotos', str(instance.title), filename])

def profileFile(instance, filename):
    return '/'.join(['profilePhotos', str(instance.email), filename])
class Project(models.Model):
    '''
    Model that describes a project. The properties are title of the project, the image of the landing page of the project, a detailed description of the project and a link to the project site
    '''
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=projectFile, default='/projectPhotos/default.jpg')
    description = models.TextField()
    link = models.CharField(max_length=200)


class Profile(models.Model):
    '''
    Model that describes a user profile. Properties include a profile photo, a user bio,the projects the user has posted ,contact info
    '''
    # user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email=models.EmailField(default='user@domain.com')
    picture = models.ImageField(upload_to=profileFile)
    bio = models.TextField()
    phone = models.CharField(max_length=15, null=True)
    


class Ratings(models.Model):
    '''
    Model that describes a Rate. The properties are project being rated, the user rating the project , the design and usability and content scores and the average project score.
    '''
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='ratings', related_query_name='rating')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ratings', related_query_name='rating')
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    overall = models.IntegerField()
    posted_on=models.DateTimeField(auto_now_add=True)

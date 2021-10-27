from django.db import models

# Create your models here.

def nameFile(instance, filename):
    return '/'.join(['projects', str(instance.title), filename])
class Project(models.Model):
    '''
    Model that describes a project. The properties are title of the project, the image of the landing page of the project, a detailed description of the project and a link to the project site
    '''
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile)
    description = models.TextField()
    link = models.CharField(max_length=200)


class Profile(models.Model):
    '''
    Model that describes a user profile. Properties include a profile photo, a user bio,the projects the user has posted ,contact info
    '''
    picture = models.ImageField(upload_to='users/profiles/')
    bio = models.TextField()
    contact = models.CharField(max_length=70)


class Rate(models.Model):
    '''
    Model that describes a Rate. The properties are project being rated, the user rating the project , the design and usability and content scores and the average project score.
    '''
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    design = models.IntegerField()
    usability = models.IntegerField()
    content = models.IntegerField()
    overall = models.IntegerField()
    posted_on=models.DateTimeField(auto_now_add=True)

from django.db import models

# Create your models here.
class Contact(models.Model):
    slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=500)
    yourmessage = models.TextField()


    def __str__(self):
        return self.name

class Portfolio(models.Model):
    projectname = models.CharField(max_length=100)
    projecttype = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    language = models.CharField(max_length=200)
    preview = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.projectname

class Blogpost(models.Model):
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=50,default="")
    presentedby = models.CharField(max_length=50,default="")
    desc = models.TextField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to="pics")

    def __str__(self):
        return self.title
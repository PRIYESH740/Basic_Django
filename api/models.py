from django.db import models

class Service(models.Model):
    service_icon=models.CharField(max_length=50)
    service_title=models.CharField(max_length=100)
    service_des=models.TextField()

class TeamMember(models.Model):
    member_image = models.ImageField(upload_to='members/')
    member_name=models.CharField(max_length=50)
    member_position=models.CharField(max_length=50)

class FoodItem(models.Model):
    food_image = models.ImageField(upload_to='foods/')
    food_name=models.CharField(max_length=50)
    food_des=models.CharField(max_length=100)

class Homepage(models.Model):
    gallery_image = models.ImageField(upload_to='galleries/')


class ContactFormEnquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=150)
    message=models.TextField(max_length=500)


    def __str__(self):
        return f'username: {self.name}'


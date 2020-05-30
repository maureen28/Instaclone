from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile/',null=True, default ='profile/image.jpg')
    bio = models.CharField(max_length=60,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Comment(models.Model):
    comments = models.CharField(max_length=60,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comments

    #Save comments
    def save_comment(self):
        return self.save()

    #Delete comments
    def delete_comment(self):
        self.delete()

    #Get comments
    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment

class Image(models.Model):
    name = models.CharField(max_length = 150, default='Armies')
    caption = models.CharField(max_length = 60)
    time_created= models.DateTimeField(default=datetime.now, blank=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    message = models.TextField(default='Hey there.')
    my_image = models.ImageField(upload_to='gallery/',default ='gallery/image.jpg')

    def __str__(self):
        return self.caption

    #  Save image
    def save_image(self):
        self.save()

    # Delete image
    def delete_image(self):
        self.delete()

    #  Update image
    @classmethod
    def update_image(cls,current_value,new_value):
        filtered_image = Image.objects.filter(image_name=current_value).update(image_name=new_value)
        return filtered_image

    #update caption
    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned

    #  retrieve all
    @classmethod
    def retrieve_all(cls):
        all_items = Image.objects.all()
        for item in all_items:
            return item;

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image


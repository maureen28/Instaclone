from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


# Create your models here.
class Profile(models.Model):
    profile_pics = models.ImageField(upload_to='profile/',null=True)
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
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.comments
    class Meta:
        ordering = ['-comment_date']

    # save comment
    def save_comment(self):
        return self.save()

    # delete comment
    def delete_comment(self):
        self.delete()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment


# Image
class Image(models.Model):
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length = 100, unique=True)
    likes = models.IntegerField(default=0, null=True)
    caption = models.CharField(max_length=160)
    my_image = models.ImageField(upload_to='gallery/')
    profile = models.ForeignKey(Profile, null=True)

    def __str__(self):
        return self.title

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

    #  retrieve all
    @classmethod
    def retrieve_all(cls):
        all_items = Image.objects.all()
        for item in all_items:
            return item;

    @classmethod
    def get_image_by_id(cls,incoming_id):
        image_result = cls.objects.get(id=incoming_id)
        return image_result

    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned
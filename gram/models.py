from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',null=True)
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
    # def save_profile(self):
    #     self.save()

    # def delete_profile(self):
    #     self.delete()
        
    # @classmethod
    # def get_profile(cls):
    #     profile = Profile.objects.all()
    #     return profile

    # @classmethod
    # def find_profile(cls,search_term):
    #     profile = cls.objects.filter(user__username__icontains=search_term)
    #     return profile

    # @classmethod
    # def update_profile(cls,id,bio):
    #     updated = Image.objects.filter(id=id).update(bio = bio)
    #     return updated

class Image(models.Model):
    image = models.ImageField()
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(default=timezone.now)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['-upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned

    @classmethod
    def get_all(cls):
        imgs = Image.objects.all()
        return imgs

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image

class Comment(models.Model):
    comments = models.CharField(max_length=60,null=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.comments
    class Meta:
        ordering = ['-comment_date']
    def save_comment(self):
        return self.save()
    def delete_comment(self):
        self.delete()
        
    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment
    
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    post = models.ImageField()
    caption = models.CharField(max_length=200)
    def __str__(self):
        return self.post()
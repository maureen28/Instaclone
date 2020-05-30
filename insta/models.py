from django.db import models

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
    author = models.ForeignKey(User, blank=True, null=True, related_name="nimo")
    time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    title = models.CharField(max_length = 100, unique=True)
    likes = models.IntegerField(default=0, null=True)
    caption = models.CharField(max_length=160)
    my_image = models.ImageField(upload_to='gallery/')
    profile = models.ForeignKey(Profile, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')


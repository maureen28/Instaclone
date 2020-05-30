from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile, Comment

# Create your tests here.
class InstagramTestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up data for the whole TestCase
        cls.user = User(id=1,username='Nimo',email='nimo@gmail.com',password='nimo5!34')
        cls.profile1 = Profile(bio='Live life',profile_pic='prof_pics/image.jpg')
        cls.comment1 =Comment(comments ='Looking good', user =cls.user)
        cls.image1 = Image(id=1,caption='Jedi',name='Armies',title=cls.comment1, my_image='gallery/flower.jpg',profile=cls.profile1)

    # Testing  instance
    def test_instance(cls):
        cls.assertTrue(isinstance(cls.user, User))
        cls.assertTrue(isinstance(cls.profile1, Profile))
        cls.assertTrue(isinstance(cls.comment1, Comment))
        cls.assertTrue(isinstance(cls.image1, Image))

    # Teardown
    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()
        Comment.objects.all().delete()

    # Testing Save Method
    def save_method_test(self):
        self.image1.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    # Testing Delete Method
    def delete_method_test(self):
        self.image1.save_image()
        filtered_img = Image.objects.filter(name='Armies')
        Image.delete_image(filtered_img)
        final_images = Image.objects.all()
        self.assertTrue(len(final_images) == 0)

    # Testing Update Method
    def update_method_test(self):
        self.image1.save_image()
        filtered_img = Image.update_image('Armies','Abnomaree')
        fetched = Image.objects.get(name ='Abnomaree')
        self.assertEqual(fetched.name,'Abnomaree')

    # Testing get image Method
    def get_image_by_id_test_method(self):
        self.image1.save_image()
        fetched_image = Image.get_image_by_id(1)
        self.assertEqual(fetched_image.id,1)

    # Testing search image Method
    def search_by_username_test_method(self):
        self.profile.save_profile()
        fetch_specific = Profile.objects.get(user=1)
        self.assertTrue(fetch_specific.id==1)


    #  test all images
    def display_all_images_test_method(self):
        self.image1.save_image()
        final_images = Image.retrieve_all()
        self.assertEqual(final_images.title,'Armies')

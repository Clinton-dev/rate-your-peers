from django.test import TestCase
from django.contrib.auth.models import User
from .models import Project, Rating

class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='charles')
        self.post = Project.objects.create(id=1, title='test post', description='short description',image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e',
                                        author=self.user, link='http://ur.coml')
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))

    def test_save_post(self):
        self.post.save()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Project.objects.all()
        self.assertTrue(len(posts) > 0)

class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='charles')
        self.post = Project.objects.create(id=1, title='test post', description='short description',image='https://ucarecdn.com/0ccf61ff-508e-46c6-b713-db51daa6626e',
                                        author=self.user, link='http://ur.coml')
        self.rating = Rating.objects.create(id=1, design=6, usability=7, content=9, user=self.user, project=self.post)
    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))
    def test_save_rating(self):
        self.rating.save()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)


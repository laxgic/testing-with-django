from django.test import TestCase

from .models import Post



class PostModelTests(TestCase):

    def setUp(self):
        self.post = Post.objects.create(
            title='New Post',
            author='Matthew',
            slug='new_slug')

    def test_post_model(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(self.post.__str__(), 'New Post')

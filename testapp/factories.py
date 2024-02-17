# testapp/factories.py
import factory
from django.contrib.auth.models import User
from testapp.models import BlogPost

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Faker('user_name')  # Using Faker for test data

class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost
    title = "Factory Generated Title"
    content = factory.Faker('paragraph')
    author = factory.SubFactory(UserFactory)  # Creates associated user

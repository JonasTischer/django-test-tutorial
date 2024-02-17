# conftest.py is a file that is used to define fixtures for pytest.
import pytest
from testapp.factories import BlogPostFactory, UserFactory

@pytest.fixture
def test_user():
    return UserFactory(username='testuser')

@pytest.fixture(scope='session')
def blog_posts(django_db_setup, django_db_blocker,):
    with django_db_blocker.unblock():
        # Create a set of blog posts for testing
        BlogPostFactory.create_batch(size=10, is_published=True)
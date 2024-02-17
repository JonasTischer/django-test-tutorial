# testapp/tests.py
from testapp.factories import BlogPostFactory
from testapp.models import BlogPost

def test_blog_post_creation(db):
    post = BlogPostFactory()
    assert post.pk == 1
    assert post.title == "Factory Generated Title"

def test_blog_post_author(db, test_user):  # Add 'test_user' as an argument
    BlogPostFactory(author=test_user)

    published_posts = BlogPost.objects.filter()
    assert published_posts.count() == 1
    assert published_posts.first().author == test_user

def test_blog_post_publication_status(db, blog_posts):
    published_posts = BlogPost.objects.filter(is_published=True)
    assert published_posts.count() == 10
    # Additional assertions can be made here
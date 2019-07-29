import base64
from django.conf import settings
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from .models import (
    Tag, Post, Comment, Reply, Rating, Bookmark,
    )

User = get_user_model()

class PostsTest(TestCase):
    def setUp(self):
        client = BackendApplicationClient(client_id=settings.SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url='https://bitbucket.org/site/oauth2/access_token', client_id=settings.SOCIAL_AUTH_BITBUCKET_OAUTH2_KEY, client_secret=settings.SOCIAL_AUTH_BITBUCKET_OAUTH2_SECRET)
        print(token)

    def test_posts(self):
        pass

    def test_tags(self):
        pass

    def test_comments(self):
        pass

    def test_replies(self):
        pass

    def test_bookmarks(self):
        pass


import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from blog.models import post


@pytest.fixture
def author(db):
    return User.objects.create_user("alice", "alice@example.com", "pw-12345-xyz")


def test_str_is_title(author):
    assert str(post.objects.create(title="Hello", content="x", author=author)) == "Hello"


def test_absolute_url(author):
    p = post.objects.create(title="Hello", content="x", author=author)
    assert p.get_absolute_url() == reverse("post-detail", kwargs={"pk": p.pk})


def test_url_is_optional(author):
    p = post(title="t", content="c", author=author)
    p.full_clean()

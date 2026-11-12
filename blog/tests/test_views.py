import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from blog.models import post


@pytest.fixture
def alice(db):
    return User.objects.create_user("alice", password="pw-12345-xyz")


@pytest.fixture
def bob(db):
    return User.objects.create_user("bob", password="pw-12345-xyz")


@pytest.fixture
def alice_post(alice):
    return post.objects.create(title="Alice post", content="body", author=alice)


def test_home_lists_posts_newest_first(client, alice):
    post.objects.create(title="old", content="x", author=alice)
    post.objects.create(title="new", content="x", author=alice)
    res = client.get(reverse("blog-home"))
    assert res.status_code == 200
    assert [p.title for p in res.context["posts"]] == ["new", "old"]


def test_home_paginates_by_five(client, alice):
    for i in range(7):
        post.objects.create(title=f"p{i}", content="x", author=alice)
    res = client.get(reverse("blog-home"))
    assert len(res.context["posts"]) == 5
    assert len(client.get(reverse("blog-home") + "?page=2").context["posts"]) == 2


def test_detail_view(client, alice_post):
    res = client.get(reverse("post-detail", args=[alice_post.pk]))
    assert res.status_code == 200
    assert b"Alice post" in res.content


def test_user_posts_only_shows_that_user(client, alice, bob, alice_post):
    post.objects.create(title="Bob post", content="x", author=bob)
    res = client.get(reverse("user-posts", args=["alice"]))
    assert [p.title for p in res.context["posts"]] == ["Alice post"]


def test_user_posts_unknown_user_404(client, db):
    assert client.get(reverse("user-posts", args=["nobody"])).status_code == 404


def test_create_requires_login(client, db):
    res = client.get(reverse("post-create"))
    assert res.status_code == 302
    assert "/login/" in res.url


def test_create_sets_author(client, alice):
    client.force_login(alice)
    res = client.post(reverse("post-create"), {"title": "T", "content": "C"})
    assert res.status_code == 302
    assert post.objects.get(title="T").author == alice


def test_only_author_can_update(client, alice_post, bob):
    client.force_login(bob)
    url = reverse("post-update", args=[alice_post.pk])
    assert client.post(url, {"title": "hacked", "content": "x"}).status_code == 403
    alice_post.refresh_from_db()
    assert alice_post.title == "Alice post"


def test_author_can_update(client, alice, alice_post):
    client.force_login(alice)
    client.post(reverse("post-update", args=[alice_post.pk]), {"title": "Edited", "content": "x"})
    alice_post.refresh_from_db()
    assert alice_post.title == "Edited"


def test_only_author_can_delete(client, alice_post, bob):
    client.force_login(bob)
    assert client.post(reverse("post-delete", args=[alice_post.pk])).status_code == 403
    assert post.objects.filter(pk=alice_post.pk).exists()


def test_author_can_delete(client, alice, alice_post):
    client.force_login(alice)
    res = client.post(reverse("post-delete", args=[alice_post.pk]))
    assert res.status_code == 302
    assert not post.objects.filter(pk=alice_post.pk).exists()


def test_about_page(client, db):
    assert client.get(reverse("blog-about")).status_code == 200

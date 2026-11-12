import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from users.models import profile


@pytest.fixture
def user(db):
    return User.objects.create_user("carol", "carol@example.com", "pw-12345-xyz")


def test_profile_created_by_signal(user):
    assert profile.objects.filter(user=user).exists()


def test_register_creates_user(client, db):
    res = client.post(
        reverse("register"),
        {
            "username": "dave",
            "email": "dave@example.com",
            "password1": "Str0ng-pass-phrase!",
            "password2": "Str0ng-pass-phrase!",
        },
    )
    assert res.status_code == 302
    assert User.objects.filter(username="dave").exists()


def test_register_rejects_mismatched_passwords(client, db):
    res = client.post(
        reverse("register"),
        {
            "username": "eve",
            "email": "eve@example.com",
            "password1": "Str0ng-pass-phrase!",
            "password2": "different",
        },
    )
    assert res.status_code == 200
    assert not User.objects.filter(username="eve").exists()


def test_login_and_logout_via_post(client, user):
    assert client.login(username="carol", password="pw-12345-xyz")
    res = client.post(reverse("logout"))
    assert res.status_code in (200, 302)
    assert "_auth_user_id" not in client.session


def test_logout_get_not_allowed(client, user):
    client.force_login(user)
    assert client.get(reverse("logout")).status_code == 405


def test_profile_requires_login(client, db):
    res = client.get(reverse("profile"))
    assert res.status_code == 302
    assert "/login/" in res.url


def test_profile_updates_user_fields(client, user):
    client.force_login(user)
    res = client.post(reverse("profile"), {"username": "carol", "email": "new@example.com"})
    user.refresh_from_db()
    assert res.status_code == 302
    assert user.email == "new@example.com"

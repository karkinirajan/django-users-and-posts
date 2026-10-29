# Django Users and Posts

A server-rendered Django blog: users register and log in, edit their profile and avatar, and create, edit, and delete their own posts. Anyone can browse posts and per-author pages.

## Features

- Registration, login, logout (POST), and password reset using Django's auth views.
- Profile page with avatar upload (images are resized to 300x300 on save).
- Posts: create, update, and delete restricted to the author; public list (5 per page), detail, and per-user pages.
- Django admin at `/admin/`.
- Production-ready settings: env-driven config, `DATABASE_URL`, WhiteNoise static files, HTTPS/HSTS headers when `DJANGO_DEBUG=false`.

## Stack

Python 3.13, Django 5.2 LTS, django-crispy-forms (bootstrap4), Pillow, WhiteNoise, gunicorn, SQLite by default or PostgreSQL via `DATABASE_URL`. See [VERSIONS.md](./VERSIONS.md).

## Quickstart

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/kneeraazon404/django-users-and-posts.git
cd django-users-and-posts
cp .env.example .env            # then edit values; export them or use your shell's env loader
export DJANGO_SECRET_KEY="$(python3 -c 'import secrets; print(secrets.token_urlsafe(50))')"
export DJANGO_DEBUG=true
uv sync
uv run python manage.py migrate
uv run python manage.py createsuperuser
uv run python manage.py runserver
```

Open http://127.0.0.1:8000.

## Configuration

All settings come from environment variables (see [.env.example](./.env.example)).

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_SECRET_KEY` | required | Django secret key; startup fails without it |
| `DJANGO_DEBUG` | `false` | Debug mode |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated hosts |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | empty | Comma-separated origins, e.g. `https://example.com` |
| `DATABASE_URL` | local SQLite file | Any `dj-database-url` URL (e.g. PostgreSQL) |
| `DJANGO_EMAIL_BACKEND` | console backend | Set to the SMTP backend for real email |
| `DJANGO_EMAIL_HOST`, `_PORT`, `_USE_TLS`, `_HOST_USER`, `_HOST_PASSWORD` | see settings | SMTP settings |
| `DJANGO_SECURE_SSL_REDIRECT` | `true` when not debug | Redirect HTTP to HTTPS |
| `DJANGO_HSTS_SECONDS` | `3600` | HSTS max-age when not debug |

Never commit secrets or `.env` files.

## Testing

```bash
uv run pytest -q
uv run ruff check .
uv run ruff format --check .
```

Tests use `django_go0.settings_test` (in-memory SQLite, temporary media directory) and cover the models, post permissions, registration, login/logout, and profile updates. CI runs the same commands (`.github/workflows/ci.yml`).

## Project structure

```
django_go0/   project settings, urls, wsgi, settings_test.py
blog/         posts: models, class-based views, templates, static, tests/
users/        profiles: registration, profile views, signals, templates, tests/
manage.py
pyproject.toml, uv.lock   dependencies (requirements.txt is exported for Heroku-style builds)
Procfile      gunicorn entry point
```

## Deployment

`Procfile` runs `gunicorn django_go0.wsgi`. Set `DJANGO_DEBUG=false`, a real `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`, and `DATABASE_URL`, then run `python manage.py migrate` and `python manage.py collectstatic --noinput`.

## License

MIT. See [LICENSE](LICENSE).

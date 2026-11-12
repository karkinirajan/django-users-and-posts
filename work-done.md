# Work done: django-users-and-posts

Branch: `chore/modernize` (local, not pushed). Date: 2026-10-29.

## What was there
A Django 2.1 blog app (apps `blog`, `users`, project `django_go0`) pinned to 2019 dependencies, with no real tests (empty `tests.py` stubs). It had uncommitted work at the start. Tracked in git: compiled `.pyc`/`__pycache__`, `db.sqlite3`, uploaded profile photos under `media/`, and 473 collected static files under `django_go0/static/`.

## Step 1: your uncommitted work, committed as-is
- `django_go0/settings.py`: hardcoded secret key, DEBUG, ALLOWED_HOSTS and SMTP credentials replaced with environment variables.
- `blog/models.py`: `url` field made optional; new migration `blog/migrations/0006_post_url_optional.py`.
- `blog/views.py`: template path typo fixed (`"blog / emails.html"`).
- `users/views.py`: `is_valid` calls fixed (they were missing parentheses); success message only on valid save.
- `README.md`: configuration section.
- Removed tracked `.pyc` and `__pycache__` files.

## Step 2: modernization changes by file
| File | Before | Change |
|---|---|---|
| `pyproject.toml`, `uv.lock`, `.python-version` | absent | New: uv project, Python 3.13, Django 5.2 LTS, pytest/ruff config |
| `requirements.txt` | 28 pins from 2019 | Regenerated from the lockfile (`uv export`) for Heroku-style builds |
| `django_go0/settings.py` | `django_heroku`, `USE_L10N`, SQLite only, no static serving | Removed `django_heroku` and `USE_L10N`; `DATABASE_URL` via dj-database-url; WhiteNoise middleware and `STORAGES`; crispy bootstrap4 pack; `CSRF_TRUSTED_ORIGINS`; HTTPS/HSTS/secure-cookie settings when not debug |
| `django_go0/settings_test.py` | absent | New test settings (in-memory DB, temp media, locmem email) |
| `blog/templates/blog/base.html` | Logout was a GET link | Logout is a POST form (Django 5 requires POST) |
| `blog/migrations/0002_post_website.py` | imported `django.utils.timezone.utc` (removed in Django 5) | Uses `datetime.timezone.utc` |
| `blog/migrations/0007_alter_post_id.py`, `users/migrations/0003_alter_profile_id.py` | absent | New: AutoField to BigAutoField to match `DEFAULT_AUTO_FIELD` |
| `users/models.py` | `profile.save()` crashed if the avatar file was missing (e.g. default.jpg is not in the repo) | Resize only when the file exists |
| `users/apps.py` | unchanged logic | Kept `import users.signals` in `ready()` with a noqa (ruff autofix had removed it and broke profile creation; caught by tests) |
| `users/views.py` | unused `username` variable | Removed |
| `blog/views.py` | one over-long line | Wrapped (string content unchanged) |
| `blog/urls.py`, `django_go0/urls.py`, `django_go0/wsgi.py`, `manage.py`, `blog/admin.py`, `users/forms.py`, `users/signals.py` | black 19 style | Reformatted by `ruff format` / import sort only; no logic change |
| `blog/tests.py`, `users/tests.py` | empty stubs | Replaced by `blog/tests/` and `users/tests/` packages (22 tests) |
| `.github/workflows/ci.yml` | absent | New: uv sync, ruff, migration check, pytest |
| `.env.example` | absent | New |
| `.gitignore` | ignored pyc only | Also ignores db.sqlite3, media/, staticfiles/, django_go0/static/, .venv, .env, caches |
| `db.sqlite3`, `media/`, `django_go0/static/` | tracked in git | Untracked with `git rm --cached`; files remain on disk |
| `README.md` | claimed "RESTful APIs" and JS interactivity that the code does not have; Python 3.8, pip | Rewritten to match the code: features, uv quickstart, config table, testing, structure, deployment |
| `VERSIONS.md` | absent | New |
| `work-done.md` | absent | This file |

## Verification (actual runs)
- `uv run pytest -q`: 22 passed.
- `uv run ruff check .`: all checks passed. `uv run ruff format --check .`: clean.
- `manage.py makemigrations --check --dry-run`: no changes detected.
- `manage.py migrate` on a fresh scratch SQLite DB: full chain applies.
- `manage.py check --deploy` with production-style env: only 2 optional warnings (SECURE_HSTS_INCLUDE_SUBDOMAINS, SECURE_HSTS_PRELOAD), left for the owner.

## Needs your attention
- **Rotate credentials.** The old secret key and SMTP password were committed in earlier history, so removing them from the working tree does not remove them from git history. Rotate them, and consider rewriting history. Commands for a rewrite will be handed to you; I do not run pushes.
- `db.sqlite3` (user accounts and password hashes) and `media/` photos were committed in history for the same reason.
- `blog/views.py: Emails` is not routed in any urls.py and contains hardcoded third-party recipient addresses. I left it untouched; consider removing it.
- `default.jpg` (the profile default) is not in the repo; add one under `media/` or change the model default.
- Extra optional HSTS settings (subdomains, preload) left as your decision.
- Nothing pushed. To publish: `git push -u origin chore/modernize`

# Versions

Resolved in `uv.lock` on 2026-10-29. Previous pins (`requirements.txt` before this change) were from 2019.

| Component | Version | Previous | Note |
|---|---|---|---|
| Python | 3.13 (`.python-version`; resolved 3.13.18) | 3.8+ | `requires-python >=3.13` |
| Django | 5.2.18 | 2.1 | 5.2 is the current LTS line (Django 6.1.2 is the newest non-LTS release; 6.2 LTS not yet out) |
| django-crispy-forms | 2.7 | 1.7.2 | bootstrap4 pack now in separate package |
| crispy-bootstrap4 | 2026.2 | n/a | new, required by crispy-forms 2.x |
| Pillow | 13.0.0 | 9.3.0 | |
| WhiteNoise | 6.12.0 | 4.1.2 | |
| dj-database-url | 3.1.2 | 0.5.0 | |
| gunicorn | 26.2.0 | 19.9.0 | |
| psycopg | 3.3.6 (binary) | psycopg2 2.7.7 + psycopg2-binary 2.8.3 | duplicate drivers replaced by one |
| django-storages | 1.14.6 (s3 extra) | 1.7.1 | |
| django-heroku | removed | 0.3.1 | unmaintained; replaced by dj-database-url + WhiteNoise |
| boto3 | pulled in via django-storages[s3] | 1.9.96 | |

Dev: pytest, pytest-django, ruff (see `[dependency-groups]` in `pyproject.toml`).

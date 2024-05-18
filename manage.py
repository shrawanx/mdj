import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.append(str(BASE_DIR.parent))

SETTINGS = dict(
    BASE_DIR=BASE_DIR,
    SECRET_KEY='djangoISsoCOOL',
    DEBUG=True,
    ROOT_URLCONF='urls',  # so that it can denote urls.py
    INSTALLED_APPS=[
        'apps.MDJConfig',
    ],
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
)
if __name__ == "__main__":
    import django
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(**SETTINGS)
    django.setup()

    execute_from_command_line(sys.argv)
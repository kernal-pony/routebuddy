from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
DEBUG = False

# Host security
ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(',')

# Database configuration using production environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# Static assets production configurations (collectstatic path)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# CORS Configuration for Production
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS').split(',')

# ─── SECURITY HEADERS ─────────────────────────────────────────────────────────
# Force HTTP to HTTPS redirects
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', cast=bool, default=True)

# Cookie Security
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Browser Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# HSTS Security (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

"""
Django settings for routechoices project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "your-secret-key"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

# Application definition

INSTALLED_APPS = [
    "routechoices",
    "routechoices.core",
    "routechoices.site",
    "routechoices.lib",
    "django_hosts",
    "corsheaders",
    "user_sessions",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "background_task",
    "django_bootstrap5",
    "admincommand",
    "oauth2_provider",
    "rest_framework",
    "drf_yasg",
    "markdownify.apps.MarkdownifyConfig",
    "django_s3_storage",
    "raven.contrib.django.raven_compat",
    "qr_code",
    "captcha",
    "django_read_only",
    "compressor",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.sitemaps",
]

MIDDLEWARE = [
    "routechoices.core.middleware.HostsRequestMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "routechoices.core.middleware.XForwardedForMiddleware",
    "user_sessions.middleware.SessionMiddleware",
    "routechoices.core.middleware.CorsMiddleware",
    "csp.middleware.CSPMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

SESSION_ENGINE = "user_sessions.backends.db"

ROOT_URLCONF = "routechoices.urls"
ROOT_HOSTCONF = "routechoices.hosts"
DEFAULT_HOST = "www"
PARENT_HOST = "routechoices.dev:8081"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "OPTIONS": {
            "loaders": [
                (
                    "django.template.loaders.cached.Loader",
                    [
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ],
                ),
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "routechoices.lib.context_processors.site",
            ],
        },
    },
]

WSGI_APPLICATION = "routechoices.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "app_db",
        "USER": "app_user",
        "PASSWORD": "changeme",
        "HOST": "db",
        "PORT": "",
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

TIME_ZONE = "UTC"

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

SITE_ID = 1

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_assets"),
]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGIN_URL = "//www.routechoices.dev:8081/accounts/login/"
REDIRECT_ALLOWED_DOMAINS = ["api.routechoices.dev", "www.routechoices.dev"]
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

SESSION_COOKIE_DOMAIN = ".routechoices.dev"
SESSION_COOKIE_SAMESITE = None

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
}

SLUG_BLACKLIST = [
    ".htaccess",
    ".htpasswd",
    ".well-known",
    "400",
    "401",
    "403",
    "404",
    "405",
    "406",
    "407",
    "408",
    "409",
    "410",
    "411",
    "412",
    "413",
    "414",
    "415",
    "416",
    "417",
    "421",
    "422",
    "423",
    "424",
    "426",
    "428",
    "429",
    "431",
    "500",
    "501",
    "502",
    "503",
    "504",
    "505",
    "506",
    "507",
    "508",
    "509",
    "510",
    "511",
    "about",
    "about-us",
    "abuse",
    "access",
    "account",
    "accounts",
    "ad",
    "add",
    "admin",
    "administration",
    "administrator",
    "ads",
    "advertise",
    "advertising",
    "aes128-ctr",
    "aes128-gcm",
    "aes192-ctr",
    "aes256-ctr",
    "aes256-gcm",
    "affiliate",
    "affiliates",
    "ajax",
    "alert",
    "alerts",
    "alpha",
    "amp",
    "analytics",
    "api",
    "app",
    "apps",
    "asc",
    "assets",
    "atom",
    "auth",
    "authentication",
    "authorize",
    "autoconfig",
    "autodiscover",
    "avatar",
    "backers",
    "backup",
    "banner",
    "banners",
    "beta",
    "billing",
    "billings",
    "blog",
    "blogs",
    "board",
    "bookmark",
    "bookmarks",
    "broadcasthost",
    "business",
    "buy",
    "cache",
    "calendar",
    "campaign",
    "captcha",
    "careers",
    "cart",
    "cas",
    "categories",
    "category",
    "cdn",
    "cgi",
    "cgi-bin",
    "chacha20-poly1305",
    "change",
    "channel",
    "channels",
    "chart",
    "chat",
    "checkout",
    "clear",
    "client",
    "close",
    "cms",
    "com",
    "comment",
    "comments",
    "community",
    "compare",
    "compose",
    "config",
    "connect",
    "contact",
    "contest",
    "cookies",
    "copy",
    "copyright",
    "count",
    "create",
    "crossdomain.xml",
    "css",
    "curve25519-sha256",
    "customer",
    "customers",
    "customize",
    "dashboard",
    "db",
    "deals",
    "debug",
    "delete",
    "desc",
    "dev",
    "developer",
    "developers",
    "diffie-hellman-group-exchange-sha256",
    "diffie-hellman-group14-sha1",
    "disconnect",
    "discuss",
    "dns",
    "dns0",
    "dns1",
    "dns2",
    "dns3",
    "dns4",
    "docs",
    "documentation",
    "domain",
    "download",
    "downloads",
    "downvote",
    "draft",
    "drop",
    "ecdh-sha2-nistp256",
    "ecdh-sha2-nistp384",
    "ecdh-sha2-nistp521",
    "edit",
    "editor",
    "email",
    "enterprise",
    "error",
    "errors",
    "event",
    "events",
    "example",
    "exception",
    "exit",
    "explore",
    "export",
    "extensions",
    "false",
    "family",
    "faq",
    "faqs",
    "favicon.ico",
    "features",
    "feed",
    "feedback",
    "feeds",
    "file",
    "files",
    "filter",
    "follow",
    "follower",
    "followers",
    "following",
    "fonts",
    "forgot",
    "forgot-password",
    "forgotpassword",
    "form",
    "forms",
    "forum",
    "forums",
    "friend",
    "friends",
    "ftp",
    "get",
    "git",
    "go",
    "group",
    "groups",
    "guest",
    "guidelines",
    "guides",
    "head",
    "header",
    "help",
    "hide",
    "hmac-sha",
    "hmac-sha1",
    "hmac-sha1-etm",
    "hmac-sha2-256",
    "hmac-sha2-256-etm",
    "hmac-sha2-512",
    "hmac-sha2-512-etm",
    "home",
    "host",
    "hosting",
    "hostmaster",
    "htpasswd",
    "http",
    "httpd",
    "https",
    "humans.txt",
    "icons",
    "images",
    "imap",
    "img",
    "import",
    "info",
    "insert",
    "investors",
    "invitations",
    "invite",
    "invites",
    "invoice",
    "is",
    "isatap",
    "issues",
    "it",
    "jobs",
    "join",
    "js",
    "json",
    "keybase.txt",
    "learn",
    "legal",
    "license",
    "licensing",
    "limit",
    "live",
    "liveloxmap",
    "load",
    "local",
    "localdomain",
    "localhost",
    "lock",
    "login",
    "logout",
    "lost-password",
    "mail",
    "mail0",
    "mail1",
    "mail2",
    "mail3",
    "mail4",
    "mail5",
    "mail6",
    "mail7",
    "mail8",
    "mail9",
    "mailer-daemon",
    "mailerdaemon",
    "map",
    "marketing",
    "marketplace",
    "master",
    "me",
    "media",
    "member",
    "members",
    "message",
    "messages",
    "metrics",
    "mis",
    "mobile",
    "moderator",
    "modify",
    "more",
    "mx",
    "my",
    "net",
    "network",
    "new",
    "news",
    "newsletter",
    "newsletters",
    "next",
    "nil",
    "no-reply",
    "nobody",
    "noc",
    "none",
    "noreply",
    "notification",
    "notifications",
    "ns",
    "ns0",
    "ns1",
    "ns2",
    "ns3",
    "ns4",
    "ns5",
    "ns6",
    "ns7",
    "ns8",
    "ns9",
    "null",
    "oauth",
    "oauth2",
    "offer",
    "offers",
    "online",
    "openid",
    "order",
    "orders",
    "overview",
    "owner",
    "page",
    "pages",
    "partners",
    "passwd",
    "password",
    "pay",
    "payment",
    "payments",
    "photo",
    "photos",
    "pixel",
    "plans",
    "plugins",
    "policies",
    "policy",
    "pop",
    "pop3",
    "popular",
    "portfolio",
    "post",
    "postfix",
    "postmaster",
    "poweruser",
    "preferences",
    "premium",
    "press",
    "previous",
    "pricing",
    "print",
    "privacy",
    "privacy-policy",
    "private",
    "prod",
    "product",
    "production",
    "profile",
    "profiles",
    "project",
    "projects",
    "public",
    "purchase",
    "put",
    "quota",
    "redirect",
    "reduce",
    "refund",
    "refunds",
    "register",
    "registration",
    "remove",
    "replies",
    "reply",
    "report",
    "request",
    "request-password",
    "reset",
    "reset-password",
    "response",
    "return",
    "returns",
    "review",
    "reviews",
    "robots.txt",
    "root",
    "rootuser",
    "rsa-sha2-2",
    "rsa-sha2-512",
    "rss",
    "rules",
    "sales",
    "save",
    "script",
    "sdk",
    "search",
    "secure",
    "security",
    "select",
    "services",
    "session",
    "sessions",
    "settings",
    "setup",
    "share",
    "shift",
    "shop",
    "signin",
    "signup",
    "site",
    "sitemap",
    "sites",
    "smtp",
    "sort",
    "source",
    "sql",
    "sse",
    "ssh",
    "ssh-rsa",
    "ssl",
    "ssladmin",
    "ssladministrator",
    "sslwebmaster",
    "stage",
    "staging",
    "stat",
    "static",
    "statistics",
    "stats",
    "status",
    "store",
    "stripe",
    "style",
    "styles",
    "stylesheet",
    "stylesheets",
    "subdomain",
    "subscribe",
    "sudo",
    "super",
    "superuser",
    "support",
    "survey",
    "sync",
    "sysadmin",
    "system",
    "tablet",
    "tag",
    "tags",
    "team",
    "telnet",
    "terms",
    "terms-of-use",
    "test",
    "testimonials",
    "theme",
    "themes",
    "today",
    "tools",
    "topic",
    "topics",
    "tos",
    "tour",
    "tracker",
    "training",
    "translate",
    "translations",
    "trending",
    "trial",
    "true",
    "umac-128",
    "umac-128-etm",
    "umac-64",
    "umac-64-etm",
    "undefined",
    "unfollow",
    "unsubscribe",
    "update",
    "upgrade",
    "usenet",
    "user",
    "username",
    "users",
    "uucp",
    "var",
    "verify",
    "video",
    "view",
    "void",
    "vote",
    "webmail",
    "webmaster",
    "website",
    "widget",
    "widgets",
    "wiki",
    "wpad",
    "write",
    "www",
    "www-data",
    "www1",
    "www2",
    "www3",
    "www4",
    "you",
    "yourname",
    "yourusername",
    "zlib",
    "traccar",
]
ACCOUNT_ADAPTER = "routechoices.lib.account_adapters.SiteAccountAdapter"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
ACCOUNT_USERNAME_BLACKLIST = SLUG_BLACKLIST
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_USERNAME_MIN_LENGTH = "2"
ACCOUNT_USERNAME_VALIDATORS = "routechoices.lib.validators.custom_username_validators"
ACCOUNT_FORMS = {"reset_password": "routechoices.site.forms.ResetPasswordForm"}

EMAIL_HOST = "smtp"
EMAIL_PORT = 1025

CACHES = {
    "default": {
        "BACKEND": "diskcache.DjangoCache",
        "LOCATION": os.path.join(BASE_DIR, "cache"),
        "TIMEOUT": 300,
        # ^-- Django setting for default timeout of each key.
        "SHARDS": 4,
        "DATABASE_TIMEOUT": 0.10,  # 10 milliseconds
        # ^-- Timeout for each DjangoCache database transaction.
        "OPTIONS": {"size_limit": 2**30},  # 1 gigabyte
    },
}

CACHE_TILES = True
CACHE_EVENT_DATA = True

TMT250_PORT = 2000
GL200_PORT = 2002


# The AWS region to connect to.
AWS_REGION = "us-east-1"
# The AWS access key to use.
AWS_ACCESS_KEY_ID = "minio"
# The AWS secret access key to use.
AWS_SECRET_ACCESS_KEY = "minio123"
# The optional AWS session token to use.
AWS_SESSION_TOKEN = ""
AWS_S3_ENDPOINT_URL = "http://minio:9000"

GEOIP_PATH = os.path.join(BASE_DIR, "geoip")

SILENCED_SYSTEM_CHECKS = ["admin.E410"]

PATREON_CREATOR_ID = "xRJAgEV1zma3MfnaVGg9SRTYet-EUTKqn4O2Llz6_lk"

MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            "h1",
            "h2",
            "h3",
            "h4",
            "img",
            "a",
            "abbr",
            "acronym",
            "b",
            "blockquote",
            "em",
            "i",
            "li",
            "ol",
            "p",
            "strong",
            "ul",
        ],
        "WHITELIST_ATTRS": [
            "href",
            "src",
            "alt",
            "style",
        ],
        "WHITELIST_STYLES": [
            "color",
            "width",
            "height",
            "font-weight",
        ],
    }
}

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    "SCOPES": {"full": "Read and Write data"}
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
        "OAuth2": {
            "type": "oauth2",
            "authorizationUrl": "/oauth2/authorize/",
            "tokenUrl": "/oauth2/token/",
            "flow": "accessCode",
            "scopes": {
                "full": "Read and Write data",
            },
        },
    }
}

EMAIL_CUSTOMER_SERVICE = "support@routechoices.dev"

CHAT_SERVER = "chat.routechoices.dev:8081"
CHAT_INTERNAL_SECRET = "<change-me>"

POST_LOCATION_SECRETS = ["<replace-me>"]

XFF_TRUSTED_PROXY_DEPTH = 1

CSP_DEFAULT_SRC = (
    "'self'",
    "www.routechoices.dev:8081",
    "api.routechoices.dev:8081",
    "chat.routechoices.dev:8081",
    "www.routechoices.com",
    "api.routechoices.com",
)
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")
CSP_IMG_SRC = ("'self'", "*", "data:")
CSP_WORKER_SRC = ("'self'", "blob:")

CSRF_TRUSTED_ORIGINS = [
    "https://*.routechoices.dev:8081",
]
CSRF_USE_SESSIONS = True
CSRF_COOKIE_HTTPONLY = False

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

try:
    from .local_settings import *  # noqa: F403, F401
except ImportError:
    pass

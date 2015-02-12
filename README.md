## Usage

```bash
django-admin startproject \
  --template=https://github.com/SiliconValleyInsight/django-project-template/archive/master.zip \
  --extension=py,yml \
  PROJECT_NAME
```

## Packages

- [django-compressor](http://django-compressor.readthedocs.org)
- [django-libsass](https://github.com/torchbox/django-libsass)
- [django-storages](http://django-storages.readthedocs.org)
- [django-tastypie](http://django-tastypie.readthedocs.org)

## Apps

- [api](api/)

## Configuration

Environment variables are used to set configuration values:

```bash
# Enable debug mode (defaults to false)
export DEBUG=

# Session secret key (required)
export SECRET_KEY=

# Database URL (prioritized over Postgres settings)
export DATABASE_URL=

# Postgres settings (required for Docker deployment)
export POSTGRES_HOST=localhost
export POSTGRES_USER={{ project_name }}
export POSTGRES_PASSWORD=

# AWS S3 credentials (required if DEBUG is False)
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=

# Sentry DSN
export SENTRY_DSN=
```

You can also use a `.env` config file for Docker and Heroku deployment

## Deployment

Use the [Chaussette](http://chaussette.readthedocs.org) WSGI server with
[Meinheld](http://meinheld.org/) as backend.


### Docker

1. Build app image

  ```bash
  docker-compose build app
  ```

2. Create and run containers

  #### Development

  ```bash
  docker-compose up -d
  ```

  #### Production

  ```bash
  docker-compose -f docker-compose-prod.yml up -d
  ```


## Usage

```bash
django-admin startproject \
  --template=https://github.com/marksteve/django-project-template/archive/master.zip \
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
# Enable debug mode (default to false)
export DEBUG=
# Session secret key (required)
export SECRET_KEY=
# PostgreSQL host (defaults "localhost")
export POSTGRES_HOST=
# PostgreSQL user (defaults to project name)
export POSTGRES_USER=
# PostgreSQL password (required)
export POSTGRES_PASSWORD=
# AWS Access Key ID for S3 storage (required if DEBUG is false)
export AWS_ACCESS_KEY_ID=
# AWS Secret Access Key for S3 storage (required if DEBUG is false)
export AWS_SECRET_ACCESS_KEY=
# Sentry DSN
export SENTRY_DSN=
```

## Deployment

Use the [Chaussette](http://chaussette.readthedocs.org) WSGI server with
[Meinheld](http://meinheld.org/) as backend.


### Docker

1. Create `.env` config files

  #### Development

  `development.env`

  #### Production

  `production.env`

2. Build app image

  ```bash
  docker-compose build app
  ```

3. Create and run containers

  #### Development

  ```bash
  docker-compose up -d
  ```

  #### Production

  ```bash
  docker-compose -f docker-compose-prod.yml up -d
  ```


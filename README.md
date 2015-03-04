# SVI Django Starter Template

Clone this repo for any new webapp projects we're developing. 


## Developing Locally

#### Read
The [Docker](https://docs.docker.com/userguide/) docs!

#### Install

RECOMMENDED: Ubuntu Trusty

1. Install [docker](https://docs.docker.com/installation/ubuntulinux/). There's a helpful installation script.

 `$ curl -sSL https://get.docker.com/ubuntu/ | sudo sh`

2. Install [docker-compose](https://docs.docker.com/compose/)


OSX

1. Install [boot2docker](https://docs.docker.com/installation/mac/)
2. Install [docker-compose](http://docs.docker.com/compose/install/)

#### Set Up
.env file should contain environment variables as detailed below. There's a starter template in the folder .env.template

```cp .env.template .env```

Edit the resulting .env file as needed. At minimum, you need to set the postgres variables.


#### Code
Follow instructions below to deploy locally as Docker for development. No need to set a local virtualenv because requirements are installed into the Docker container.

-----

## Starting the Django Project
```bash
django-admin startproject \
  --template=https://github.com/SiliconValleyInsight/django-project-template/archive/master.zip \
  --extension=py,yml \
  --name=Procfile \
  PROJECT_NAME
```

## Preloaded Django Packages

- [django-compressor](http://django-compressor.readthedocs.org)
- [django-libsass](https://github.com/torchbox/django-libsass)
- [django-storages](http://django-storages.readthedocs.org)
- [django-tastypie](http://django-tastypie.readthedocs.org)

## Preloaded Apps

- [api](api/) 

## .env File Configuration 

Environment variables are used to set configuration values:

| env var        | description           | required?  |
| ------------- |:-------------:| -----:|
| export SECRET_KEY=     | session secret key | required |
| export DEBUG= | enable debug mode      |   opt |
| export DATABASE_URL= | Database URL (prioritized over Postgres settings)      |    opt |
| export POSTGRES_HOST=localhost | postgres host | required for Docker |
| export POSTGRES_USER={{ project_name }} | db username | required for Docker | 
| export POSTGRES_PASSWORD= | db password | required | 
| export AWS_ACCESS_KEY_ID= | AWS S3 credentials | required if Debug is False| 
| export AWS_SECRET_ACCESS_KEY= | AWS S3 credentials | required if AWS |
| export SENTRY_DSN= | Sentry DSN | opt | 


You can also use a `.env` config file for Docker and Heroku deployment



## Deployment

### Heroku

1. Create app

  ```bash
  heroku create
  ```

2. Set config

  ```bash
  heroku config:set SECRET_KEY=...
  ```

3. Push to remote

  ```bash
  git push heroku master
  ```

4. Start web process

  ```bash
  heroku ps:scale web=1
  ```

### Docker

1. Build app images (listed in docker-compose.yml)

  ```bash
  docker-compose build web 
  docker-compose build db
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


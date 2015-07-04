![Docker-Django-React Template](https://s3.amazonaws.com/media-p.slid.es/uploads/176500/images/1488501/ddr.png)

## Requirements

1. Docker Engine and Compose
2. NPM

## Starting the Django Project
```bash
django-admin startproject \
  --template=https://github.com/SiliconValleyInsight/ddr-template/archive/master.zip \
  --extension=sh,py,yml,json,env
  PROJECT_NAME
```

## Configure

```
# dev.env
SECRET_KEY=
POSTGRES_PASSWORD=
```

```
# prod.env
SECRET_KEY=
POSTGRES_PASSWORD=
```

## Install dependencies

```bash
docker-compose run --rm web bin/install.sh
```

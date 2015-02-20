from functools import partial
from storages.backends.s3boto import S3BotoStorage

StaticStorage = partial(S3BotoStorage, location='static')
MediaStorage = partial(S3BotoStorage, location='media')

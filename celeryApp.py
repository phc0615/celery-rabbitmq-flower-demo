from __future__ import absolute_import
from celery import Celery

app = Celery('test_celery',
	broker='pyamqp://admin:admin_admin@localhost/admin_vhost',
	backend='rpc://',
	include=['test_celery.tasks'])

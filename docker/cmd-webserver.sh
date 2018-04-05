#!/bin/bash -xe

python /usr/src/app/manage.py migrate --noinput
python /usr/src/app/manage.py collectstatic --noinput
# python /usr/src/app/manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')"
python /usr/src/app/manage.py loaddata _data/sections-only.json


gunicorn config.wsgi --bind 0.0.0.0:$PORT --log-file -

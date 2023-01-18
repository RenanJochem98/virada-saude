#!/bin/bash
set -e

if [ -n "$1" ]; then
    exec "$@"
fi

if [ "$ENV" = "development" ] ; then
    if test -f "core/manage.py"; then
        # python check_db.py --service-name mysql --ip db --port 5500
        # pip install —upgrade setuptools
        pip install -r requirements/base.txt
        pip install -r requirements/dev.txt
        pip install -r requirements/test.txt
        python core/manage.py makemigrations
        python core/manage.py migrate
        python core/manage.py collectstatic --noinput
        echo "Dev Run Server"
        python core/manage.py runserver 0.0.0.0:$PORT
    else
        echo "Dev Start Project"
        django-admin startproject core
    fi
else
    python core/manage.py makemigrations
    python core/manage.py migrate
    python core/manage.py collectstatic --noinput  # Collect static files

    # Prepare log files and start outputting logs to stdout
    mkdir -p /srv/logs/
    touch /srv/logs/gunicorn.log
    touch /srv/logs/access.log
    tail -n 0 -f /srv/logs/*.log &

    # Start Gunicorn processes
    echo Starting Gunicorn
    exec gunicorn core.wsgi \
        --bind 0.0.0.0:$PORT \
        --chdir /usr/src/app/core \
        --workers 3 \
        --timeout 60 \
        --log-level=info \
        --log-file=/srv/logs/gunicorn.log \
        --access-logfile=/srv/logs/access.log
fi

web: python manage.py collectstatic --noinput; gunicorn drawinglots.wsgi:application -b 0.0.0.0:$PORT --log-level=debug -w 3 --access-logfile '-' --access-logformat '"%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
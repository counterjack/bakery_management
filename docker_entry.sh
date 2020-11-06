# exit on error
set -e

echo "<<<<<<<<<<<<<<<<<<<<<  RUNNING MIGRATIONS >>>>>>>>>>>>>>>>>>>>>>>>"
echo $(ls)

python manage.py collectstatic
python manage.py migrate

#Create background service for celery worker and beat
# celery -A expense worker -l info -E &
gunicorn project.wsgi --bind 0.0.0.0:8000
#python src/manage.py runserver 0.0.0.0:8000
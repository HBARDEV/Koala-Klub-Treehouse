#!/bin/sh
echo "******  Make migrations  ******"
echo "******"
python manage.py makemigrations
echo "******"
echo "******  Done  ******"
echo "******"
echo "******  Migrating tables  ******"
echo "******"
python manage.py migrate
echo "******"
echo "******  Done  ******"
echo "******"
echo "******  Configuring database  ******"
echo "******"
python manage.py runscript db_config
echo "******"
echo "******  Done  ******"
echo "******"
echo "******"
echo "******  Get exchange rates  ******"
echo "******"
python manage.py update_rates
echo "******"
echo "******  Done  ******"
echo "******"

exec "$@"

#!/bin/sh
echo "******  Make migrations  ******"
echo "******"
python manage.py makemigrations
echo "******"
echo "******  Done  ******"
echo "******"
echo "******  Migrating tables  ******"
echo "******"
python manage.py migrate
echo "******"
echo "******  Done  ******"
echo "******"
echo "******  Collecting static  ******"
echo "******"
python manage.py collectstaic
echo "******"
echo "******  Done  ******"
echo "******"
echo "******  Get exchange rates  ******"
echo "******"
python manage.py update_rates
echo "******"
echo "******  Done  ******"
echo "******"
echo "******  Testing  ******"
echo "******"
python manage.py test
echo "******"
echo "******  Done  ******"

exec "$@"
#!/bin/sh

echo "Attente que la base de données soit prête..."
while ! nc -z db 3306; do
    sleep 1
done

echo "Base de données prête, démarrage de l'application..."
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
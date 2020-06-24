sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn --bind='0.0.0.0:8080' hello:app

sudo /etc/init.d/mysql start
mysql -uroot -e "create database web;"
mysql -uroot -e "grant all privileges on web.* to 'box'@'localhost' with grant option;"
~/web/ask/manage.py makemigrations
~/web/ask/manage.py migrate

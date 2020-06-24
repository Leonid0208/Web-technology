  
sudo /etc/init.d/nginx stop
sudo /etc/init.d/gunicorn stop
sudo rm /etc/nginx/sites-enabled/default
sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
# sudo /etc/init.d/nginx start
sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/nginx start
# sudo /etc/init.d/gunicorn start
sudo gunicorn -c /etc/gunicorn.d/hello.py hello

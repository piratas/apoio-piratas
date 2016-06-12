FROM python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir /app/
WORKDIR /app
RUN pip install --upgrade pip
ADD requirements.txt /app/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install supervisor nginx -y
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY apoio.nginx /etc/nginx/sites-enabled/apoio
RUN ln -sf /dev/stdout /var/log/nginx/access.log
RUN ln -sf /dev/stderr /var/log/nginx/error.log
ADD . /app/
WORKDIR /app/apoio/

#COPY ./docker-entrypoint.sh /docker-entrypoint.sh
#ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["/usr/bin/supervisord"]
#CMD uwsgi --socket=apoio.sock --chdir /app/apoio --wsgi-file wsgi.py --chmod-socket=666

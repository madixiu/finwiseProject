FROM nginx:1.19.2
COPY nginx/dev/dev.conf /etc/nginx/nginx.conf
COPY backend/static /usr/src/app/static/
EXPOSE 80
# RUN apt-get update && apt-get install -y supervisor
# COPY nginx/supervisor/config.conf /etc/supervisor/conf.d
# RUN mkdir /run/daphne/
# RUN user="$(id -u -n)"
# RUN sudo chown ubuntu.ubuntu /run/daphne/
# RUN suopervisorctl reread
# RUN supervisorctl update
CMD ["nginx", "-g", "daemon off;"]
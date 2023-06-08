# Dockerfile
FROM nginx:alpine

RUN apk add openjdk17

COPY . /usr/src/app
WORKDIR /usr/src/app

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000
CMD ./setup_server.sh
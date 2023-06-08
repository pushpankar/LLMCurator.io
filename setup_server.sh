#!/bin/sh
nginx -g 'daemon off;' &
java -jar target/app-standalone.jar
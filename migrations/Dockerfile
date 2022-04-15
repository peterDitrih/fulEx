FROM postgis/postgis:12-3.0
RUN mkdir -p /docker-entrypoint-initdb.d

COPY initdb.sh /docker-entrypoint-initdb.d/initdb.sh
COPY initdb.sql /tmp/initdb.sql
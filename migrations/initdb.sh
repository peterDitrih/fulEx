psql -U user -p 5432 -c "CREATE DATABASE fulex;"
psql -U user -p 5432 -d fulex < "/tmp/initdb.sql"

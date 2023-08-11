-- settings.sql
CREATE DATABASE warm_weather;
CREATE USER super WITH PASSWORD 'super';
GRANT ALL PRIVILEGES ON DATABASE warm_weather TO super;
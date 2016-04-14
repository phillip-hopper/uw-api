# uw-publishing


### PGSQL settings

    sudo -u postgres psql
    create user team43 createdb createuser password 'password';
    create database publish encoding 'UTF8';
    \q

In `/etc/postgresql/9.3/main/pg_hba.conf` change 

    local   all             all                                     peer
    host    all             all             127.0.0.1/32            peer

to 

    local   all             all                                     trust
    host    all             all             127.0.0.1/32            trust


Now, restart the service: `sudo service postgresql restart`.
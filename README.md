# mongorestore
Restore a MongoDB database. This script **only works** if the backup ran using script from this [repo](https://github.com/dhewana/mongodump).

## Config example
```
DB_HOST = '127.0.0.1'
DB_PORT = '27017'
DB_NAME = 'dbname'
BACKUP_PATH = '/home/user/dbname/'
```
Note : The `/` at the end of `BACKUP_PATH` is **important**.

## Allow executable
```
chmod +x mongorestore.py
```

## Cron job daily example
```
20 0 * * * /usr/bin/python3 /home/user/mongorestore.py > /home/user/mongorestore.log
```

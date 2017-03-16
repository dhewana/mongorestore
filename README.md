# mongorestore
Restore a MongoDB database. This script **only works** if the backup ran using script from this [repo](https://github.com/dhewana/mongodump).

## Config example
```
DB_HOST = ''
DB_PORT = ''
DB_NAME = ''
BACKUP_PATH = '/home/user/dbname/date/dbname/'
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

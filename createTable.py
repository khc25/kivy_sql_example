import psycopg2

from urllib.parse import urlparse

result = urlparse("dbpostgres://obbyumtp:McdTVFblMMvaFMEgp9FaC44jS7j7ZwX1@suleiman.db.elephantsql.com:5432/obbyumtp")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname
conn = psycopg2.connect(
    database = database,
    user = username,
    password = password,
    host = hostname
)
cur = conn.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, username varchar, password varchar);")
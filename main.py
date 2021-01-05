from urllib.parse import urlparse
import psycopg2
from kivy.uix.label import Label
from kivy.app import App
import kivy
kivy.require('1.0.6')  # replace with your current kivy version !


# cur.execute("CREATE TABLE test (id serial PRIMARY KEY, username varchar, password varchar);")

class MyApp(App):
    array = []
    def __init__(self):
        super(MyApp,self).__init__()
        result = urlparse(
            "dbpostgres://obbyumtp:McdTVFblMMvaFMEgp9FaC44jS7j7ZwX1@suleiman.db.elephantsql.com:5432/obbyumtp")

        username = result.username
        password = result.password
        database = result.path[1:]
        hostname = result.hostname
        conn = psycopg2.connect(
            database=database,
            user=username,
            password=password,
            host=hostname
        )
        cur = conn.cursor()
        result = cur.execute("SELECT * FROM test;")
        myresult = cur.fetchall()
        for x in myresult:
            self.array.append(x)

    def build(self):
        result = str(self.array)
        return Label(text=result)


if __name__ == '__main__':
    MyApp().run()

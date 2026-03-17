from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_message():
    try:
        conn = psycopg2.connect(
            host='db',
            database=os.environ.get('POSTGRES_DB'),
            user=os.environ.get('POSTGRES_USER'),
            password=os.environ.get('POSTGRES_PASSWORD')
        )
        cur = conn.cursor()
        cur.execute("SELECT message FROM test LIMIT 1;")
        message = cur.fetchone()[0]
        cur.close()
        conn.close()
        return message
    except:
        return "Сервис работает (БД недоступна)"

@app.route('/')
def index():
    return get_db_message()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import psycopg2
import telegramConnection

def main():
    print('dbPostgres.main')


def createQuary2DB():
    print('gfdgjdfg')

def connection2Postgres():
    conn = psycopg2.connect(dbname='nissancar', user=telegramConnection.db_user, password=telegramConnection.password, host='localhost')
    cursor = conn.cursor()
    cursor.execute('select * from public.carfuel')
    records = cursor.fetchall()
    print(records)
    cursor.close()
    conn.close()


def connection2PostgresSelect(query):
    print(query)
    conn = psycopg2.connect(dbname='nissancar', user=telegramConnection.db_user, password=telegramConnection.password, host='localhost')
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.execute('commit;')
    cursor.close()
    conn.close()
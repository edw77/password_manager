import psycopg2

def connect():
    try:
        connection = psycopg2.connect(user='postgres', password='admin', host='127.0.0.1', database='PassMan')
        return connection
    except (Exception, psycopg2.Error) as error:
        print(error)

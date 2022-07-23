from requests import post
import db_connection
import psycopg2

def store_passwords(connection, cursor, password, user_email, username, url, app_name):
    try:
        postgres_insert_query = """ INSERT INTO passwords (password, user_email, username, url, app_name) VALUES (%s, %s, %s, %s, %s)"""
        record_to_insert = (password, user_email, username, url, app_name)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)

def get_password_list(cursor,url='none'):
    try:
        postgres_query = """SELECT url,username,password from passwords"""
        if url == 'none':
            cursor.execute(postgres_query)
        else:
            postgres_query = postgres_query + """where url = %s"""
            record_to_insert = url
            cursor.execute(postgres_query, record_to_insert)
        
        return cursor.fetchall()

    except (Exception) as error:
        print(error)


import psycopg2

def store_data(data):
    conn = psycopg2.connect("dbname=test user=postgres password=secret")
    cur = conn.cursor()
    cur.execute("INSERT INTO my_table (data) VALUES (%s)", (data,))
    conn.commit()
    cur.close()
    conn.close()

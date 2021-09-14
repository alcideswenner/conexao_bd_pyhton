import psycopg2

host = "localhost"
dbname = "postgres"
user = "postgres"
password = "1914"
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
if conn :
   print("Ok")
   cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
   cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
   conn.commit()
   cursor.close()
   conn.close()
else:
   print("Erro")

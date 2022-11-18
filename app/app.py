from flask import Flask
import psycopg2-binary

app = Flask(__name__)
conn = psycopg2.connect(host="localhost", database="frogDB", user="frogUser", password="frogPass")

cur = conn.cursor()

@app.route('/')
def hello():
    conn = psycopg2.connect(host="localhost", database="frogDB", user="frogUser", password="frogPass")
    cur = conn.cursor()
    
    cur.execute('DROP TABLE IF EXISTS Frogs;')
    cur.execute('CREATE TABLE Frogs (id serial PRIMARY KEY,'
                                 'name varchar (50) NOT NULL,'
                                 'scientificName varchar (150) NOT NULL,'
                                 'color varchar(25) NOT NULL,'
                                 )
    cur.execute('INSERT INTO books (name, scientificName, color)'
        'VALUES (%s, %s, %s)',
        ('Bullfrog',
        'The scientific bullfrog',
        'Olive')
        )                   
    cur.execute('SELECT * FROM Frogs;')
    frogs = cur.fetchall()
    cur.close()
    conn.close()
	return frogs



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)


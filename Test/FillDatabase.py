import psycopg2
from datetime import *
from random import *
import sqlite3

connSqlite = sqlite3.connect(':memory:')
#connSqlite = sqlite3.connect('forex.db')

# Connect to an existing database
connPostgres = psycopg2.connect("dbname=forex user=postgres password=postgres host=localhost")

# Open a cursor to perform database operations
cur = connSqlite.cursor()

# Create table
cur.execute('''CREATE TABLE data
             (id int, par text,fecha date, timeframe text, apertura real, maximo real, minimo real, cierre real)''')

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)

#INSERT INTO public.data(
#           id, par, fecha, timeframe, apertura, maximo, minimo, cierre)
#  VALUES (1,'USD/EUR','10/12/2017 10:10:00','5 min',12.3,15.5,58.3,12);
pares=["USD/EUR",
       "USD/GBP",
       "USD/JPY",
       "USD/CAD",
       "USD/BTC",
       "EUR/GBP",
       "EUR/JPY",
       "EUR/CAD",
       "EUR/BTC",
       "GBP/JPY",
       "GBP/CAD",
       "GBP/BTC",
       "JPY/CAD",
       "JPY/BTC",
       "CAD/BTC",
       ]
fechaInicio = datetime.now()
fechaIncremental = fechaInicio
fechaTemporal= datetime.now()
delta = timedelta(seconds=300)
inicio=1
print('Inicioando proceso...')
for par in pares:
    print('Comenzando con el par numero:'+par+' tipo: '+par)
    for x in range(inicio,inicio+266666):
        valor1=random()*100
        valor2=random()*100
        if(valor1>valor2):
            maximo=valor1
            minimo=valor2
        else:
            maximo = valor2
            minimo = valor1
        # cur.execute("INSERT INTO public.data (id, par, fecha, timeframe, apertura, maximo, minimo, cierre) "
        #         "VALUES (%s, %s,%s, %s,%s, %s,%s, %s)",
        #         (x,par,fechaIncremental.strftime('%d/%m/%Y %H:%M:%S'),'5 min',random()*100,maximo,minimo,random()*100))

        cur.execute("INSERT INTO data (id, par, fecha, timeframe, apertura, maximo, minimo, cierre) "
                "VALUES ("+str(x)+", '"+par+"','"+fechaIncremental.strftime('%d/%m/%Y %H:%M:%S')+
                    "', '5 min',"+str(random()*100)+", "+str(maximo)+","+str(minimo)+", "+str(random()*100)+")"
                 )
                # (x,par,fechaIncremental.strftime('%d/%m/%Y %H:%M:%S'),'5 min',random()*100,maximo,minimo,random()*100))
        fechaIncremental+=delta
        # Make the changes to the database persistent
        connSqlite.commit()
        print('Insertado con id:'+str(x))
        fechaTemporal=datetime.now()
    inicio+=266666
    fechaIncremental=fechaInicio

# Close communication with the database
cur.close()
connSqlite.close()

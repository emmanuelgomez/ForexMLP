from datetime import *
from random import *
from Core import DBSelector

class Model:
    def __init__(self):
        self.database=DBSelector('psycopg2',dbname='forex', user='postgres', password='postgres', host='localhost')

    def SaveResults(self, topologyId, results):
        #pendiente

    def FillDatabase(self):
        pares = ["USD/EUR",
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
        delta = timedelta(seconds=300)
        inicio = 1
        print('Iniciando proceso...')
        for par in pares:
            print('Comenzando con el par numero:' + par + ' tipo: ' + par)
            for x in range(inicio, inicio + 266666):
                valor1 = random() * 100
                valor2 = random() * 100
                if (valor1 > valor2):
                    maximo = valor1
                    minimo = valor2
                else:
                    maximo = valor2
                    minimo = valor1
                # cur.execute("INSERT INTO public.data (id, par, fecha, timeframe, apertura, maximo, minimo, cierre) "
                #         "VALUES (%s, %s,%s, %s,%s, %s,%s, %s)",
                #         (x,par,fechaIncremental.strftime('%d/%m/%Y %H:%M:%S'),'5 min',random()*100,maximo,minimo,random()*100))

                self.database.execute("INSERT INTO data (id, par, fecha, timeframe, apertura, maximo, minimo, cierre) "
                            "VALUES (" + str(x) + ", '" + par + "','" + fechaIncremental.strftime('%d/%m/%Y %H:%M:%S') +
                            "', '5 min'," + str(random() * 100) + ", " + str(maximo) + "," + str(minimo) + ", " + str(
                    random() * 100) + ")"
                            )
                # (x,par,fechaIncremental.strftime('%d/%m/%Y %H:%M:%S'),'5 min',random()*100,maximo,minimo,random()*100))
                fechaIncremental += delta
                # Make the changes to the database persistent
                print('Insertado con id:' + str(x))
                fechaTemporal = datetime.now()
            inicio += 266666
            fechaIncremental = fechaInicio

        # Close communication with the database
        self.databaseclose()


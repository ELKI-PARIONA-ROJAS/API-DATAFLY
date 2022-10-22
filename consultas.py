import pymysql

def Pregunta1():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Puntuales en la salida'
        FROM vuelo
        WHERE (Hora_SalidaR - Hora_SalidaP) <= 15;''')
    for dato in cursor:
        pass
    conexion.close()
    return("Porcentaje de vuelos que han salido antes de los 15 min:"+' '+str(dato[0])+'%')

def Pregunta2():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Puntuales en la llegada'
        FROM vuelo
        WHERE (Hora_LlegadaR - Hora_LlegadaP) <= 15;''')
    for dato in cursor:
        pass
    conexion.close()
    return("Porcentaje de vuelos que han llegado antes de los 15 min:"+' '+str(dato[0])+'%')

def Pregunta3():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT ID_Aeropuerto_O, AVG(Hora_SalidaR - Hora_SalidaP) AS 'Retraso'
        FROM vuelo
        WHERE ID_EstadoVuelo = 'E'
        GROUP BY ID_Aeropuerto_O
        ORDER BY Retraso ASC
        LIMIT 10
        OFFSET 10;''')
    # for dato in cursor:
    #     pass
    # conexion.close()
    # return("Los 10 aeropuertos con mayor retraso en la salida de vuelos son:"+' '+str(dato[0]))
    # Devolver todos los datos
    conexion.close()
    return cursor.fetchall()


def Pregunta4():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT ID_Aeropuerto_D, AVG(Hora_LlegadaR - Hora_LlegadaP) AS 'Retraso'
        FROM vuelo
        WHERE ID_EstadoVuelo = 'E'
        GROUP BY ID_Aeropuerto_D
        ORDER BY Retraso ASC
        LIMIT 10
        OFFSET 10;''')
    # for dato in cursor:
    #     pass
    # conexion.close()
    # return("Los 10 aeropuertos con mayor retraso en la llegada de vuelos son:"+' '+str(dato[0]))
    # Devolver todos los datos
    conexion.close()
    return cursor.fetchall()


def Pregunta5():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT a.Aeropuerto, COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Porcentaje de aropuertos O'
        FROM vuelo as v
        JOIN aeropuerto_o as a
        ON v.ID_Aeropuerto_O = a.ID_Aeropuerto
        GROUP BY a.ID_Aeropuerto
        ORDER BY COUNT(*) DESC
        LIMIT 10;''')
    # for dato in cursor:
    #     pass
    # conexion.close()
    # return("Porcentaje de vuelos que salen de los Aeropuertos:"+' '+str(dato[0]))
    # return cursor.fetchall()
    salida = []
    for dato in cursor:
        salida.append(dato)
    conexion.close()
    return salida


def Pregunta6():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT a.Aeropuerto, COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Porcentaje de aeropuertos D'
        FROM vuelo as v
        JOIN aeropuerto_d as a
        ON v.ID_Aeropuerto_D = a.ID_Aeropuerto
        GROUP BY a.ID_Aeropuerto
        ORDER BY COUNT(*) DESC
        LIMIT 10;''')
    # for dato in cursor:
    #     pass
    # conexion.close()
    # return("Porcentaje de vuelos que llegan a los Aeropuertos:"+' '+str(dato[0]))
    # return cursor.fetchall()
    salida = []
    for dato in cursor:
        salida.append(dato)
    conexion.close()
    return salida


def Pregunta7():
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(
        '''SELECT a.Aerolinea, COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Porcentaje de aerolinea'
        FROM vuelo as v
        JOIN aerolinea as a
        ON v.ID_Aerolinea = a.ID_Aerolinea
        GROUP BY v.ID_Aerolinea
        ORDER BY COUNT(*) DESC
        LIMIT 10;''')
    # for dato in cursor:
    #     pass
    # conexion.close()
    # return("La aerolinea con mayores vuelos:"+' '+str(dato[0]))
    salida = []
    for dato in cursor:
        salida.append(dato)
    conexion.close()
    return salida



def query(query_):
    conexion = pymysql.connect (host='localhost', database='data_flight', user ='root', password='123')
    cursor = conexion.cursor()
    cursor.execute(query_)
    for dato in cursor:
        salida = dato
    return (salida)
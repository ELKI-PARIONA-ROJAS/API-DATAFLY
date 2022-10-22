-- Mostrar el porcentaje de vuelos que han salido antes de los 15 minutos de la hora de salida programada
SELECT COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Puntuales en la salida'
FROM vuelo
WHERE (Hora_SalidaR - Hora_SalidaP) <= 15;

-- Mostrar el porcentaje de vuelos que han llegado antes de los 15 minutos de la hora de llegada programada
SELECT COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Puntuales en la llegada'
FROM vuelo
WHERE (Hora_LlegadaR - Hora_LlegadaP) <= 15;


-- Mostrar el promedio de espera al llegar, agrupado por Aeropuerto

SELECT ID_Aeropuerto_O, AVG(Hora_SalidaR - Hora_SalidaP) AS 'Retraso'
FROM vuelo
WHERE ID_EstadoVuelo = 'E'
GROUP BY ID_Aeropuerto_O
ORDER BY Retraso ASC
LIMIT 10
OFFSET 10;

-- Mostrar el promedio de espera al llegar, agrupado por Aeropuerto

SELECT ID_Aeropuerto_D, AVG(Hora_LlegadaR - Hora_LlegadaP) AS 'Retraso'
FROM vuelo
WHERE ID_EstadoVuelo = 'E'
GROUP BY ID_Aeropuerto_D
ORDER BY Retraso ASC
LIMIT 10
OFFSET 10;


-- Mostrar la regularidad por aeropuerto de salida
SELECT a.Aeropuerto, COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Porcentaje de aropuertos O'
FROM vuelo as v
JOIN aeropuerto_o as a
ON v.ID_Aeropuerto_O = a.ID_Aeropuerto
GROUP BY a.ID_Aeropuerto
ORDER BY COUNT(*) DESC
LIMIT 10;

-- Mostrar la regularidad por aeropuerto de llegada
SELECT a.Aeropuerto, COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Porcentaje de aeropuertos D'
FROM vuelo as v
JOIN aeropuerto_d as a
ON v.ID_Aeropuerto_D = a.ID_Aeropuerto
GROUP BY a.ID_Aeropuerto
ORDER BY COUNT(*) DESC
LIMIT 10;



-- Mostrar el procentaje de dominio de mercado por aerolinea
SELECT a.Aerolinea, COUNT(*)*100/(SELECT COUNT(*) FROM vuelo) AS 'Porcentaje de aerolinea'
FROM vuelo as v
JOIN aerolinea as a
ON v.ID_Aerolinea = a.ID_Aerolinea
GROUP BY v.ID_Aerolinea
ORDER BY COUNT(*) DESC
LIMIT 10;

from fastapi import FastAPI
from pydantic import BaseModel
import consultas


app = FastAPI()

@app.get("/Pregunta_N°1")
def Puntualidad_Salida():
    return consultas.Pregunta1()

@app.get("/Pregunta_N°2")
def Puntualidad_Llegada():
    return consultas.Pregunta2()

@app.get("/Pregunta_N°3")
def Aeropuerto_Impuntual_Salida():
    return consultas.Pregunta3()

@app.get("/Pregunta_N°4")
def Aeropuerto_Impuntual_Llegada():
    return consultas.Pregunta4()

@app.get("/Pregunta_N°5")
def Aeropuerto_Salida():
    return consultas.Pregunta5()

@app.get("/Pregunta_N°6")
def Aeropuerto_LLegada():
    return consultas.Pregunta6()

@app.get("/Pregunta_N°7")
def Aerolinea_Rankeada():
    return consultas.Pregunta7()

@app.get("/Consulta/")
def Insertar_Query_MySQL(Query: str):
    return (consultas.query(Query))
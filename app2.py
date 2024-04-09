import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

with open('Mapa de Accidentalidad Vial Municipio de Medellín 2021.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Accidentalidad Municipio de Medellín 2021")

st.write('Se entiende por accidente de tránsito evento, generalmente involuntario, generado al menos por un un vehículo en movimiento, que causa daños a '
         'personas y bienes involucrados en él, e igualmente afecta la normal circulación de los vehículos que se movilizan por la vía o vías comprendidas en el' 
         'lugar o dentro de la zona de influencia del hecho0 (Ley 769 de 2002 - Código Nacional de Tránsito)'
         )
st.subheader('Sistema de consulta de Accidentalidad municipio de Medellín')

for feature in parsed_data['features']:
    longitud = feature['properties']['LONGITUD']
    latitud = feature['properties']['LATITUD']
    dia = feature['properties']['DIA']
    hora = feature['properties']['HORA']
    barrio = feature['properties']['BARRIO']
    direccion = feature['properties']['DIRECCION']
    
    # Aquí puedes hacer lo que quieras con las variables
    st.write("Longitud:", longitud)
    st.write("Latitud:", latitud)
    st.write("Día:", dia)
    st.write("Hora:", hora)
    st.write("Barrio:", barrio)
    st.write("Dirección:", direccion)
    st.write()

for feature in parsed_data['features']:
    longitud = feature['properties']['LONGITUD']
    latitud = feature['properties']['LATITUD']
    dia = feature['properties']['DIA']
    hora = feature['properties']['HORA']
    barrio = feature['properties']['BARRIO']
    direccion = feature['properties']['DIRECCION']
    
    # Aquí puedes hacer lo que quieras con las variables
    print("Longitud:", longitud)
    print("Latitud:", latitud)
    print("Día:", dia)
    print("Hora:", hora)
    print("Barrio:", barrio)
    print("Dirección:", direccion)
    print()

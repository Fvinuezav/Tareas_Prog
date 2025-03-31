informacion_personal = {
"Nombre": "Maria España",
"Edad": 19,
"Ciudad": "Ecuador", # Nota: cambiar "ciudad" (está como "Pais")
"Profesion": "Ingeniera"
}
informacion_personal["Ciudad"] = "Lago Agrio" # Se corrige "Ciudad" 
informacion_personal["Especializacion"] = "Sistemas" # Se agrega"Profesión" 
informacion_personal["Celular"] = "+593 986 345 2678" # Se agrega"Telefono" 
del informacion_personal["Edad"]  # Se elimina "Edad" al no ser necesaio
print("Datos:") #Se imprime el diccionario
print(informacion_personal)

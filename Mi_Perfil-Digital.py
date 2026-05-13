#uso de los tipos de datos en python
# 1. Datos basicos (str, int, bool, float)

nombre = "isabella lara cuadro"
edad = 13
estatura = 1.62
es_estudiante = True

# 2. Redes_Sociales = (tuple)

Redes_sociales = ("isa-lara", "019_isab")

# 3. Playlist de cantantes favoritos = (list en un dict)

Playlist = [{"titulo": "MIL D AURA", "artista": "kris r", "duracion": "3:23"},
{"titulo": "QUE LIO", "artista": "blessd", "duracion": "2:12"},
{"titulo": "SUPERSTAR", "artista": "blessd,los money makers", "duracion": "3:14"}]

print("presentacion personal")
print("Mi nombre es:", nombre)
print("Mi edad es:", edad)
print("Mi estatura es:", estatura)
print("¿estoy activo en el colegio?", es_estudiante)
print("Mis redes sociales son:", Redes_sociales)
print("Mi playlist favorita:") 
print(f"{cancion["titulo"]} - {cancion["artista"]})({cancion["duracion"]})min")
print ("----------------------------------")

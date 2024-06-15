# ejercicio en clase 15 de junio de 2024
import csv
def obtener_fichero_de_calificaciones():
    lista = []
    with open(r"C:\Users\cetecom\Downloads\calificaciones.csv", "r",newline="") as archivo:
        lector_csv = csv.reader(archivo,delimiter=";")
        pos = 0
          # Sirve para llenar los espacios vacios con 0's
            
        for linea in lector_csv:
            
            if pos!=0:
                for i in range(2,len(linea)):   # Sirve para llenar los espacios vacios con 0's
                    if linea[i] =='':
                        linea[i]='0,0'
                #año = int(linea[0])
                #trimestre1 = float(linea[1])
                #trimestre2 = float(linea[2])
                #trimestre3 = float(linea[3])
               # trimestre4 = float(linea[4])
                Apellidos = linea[0]
                nombre = linea[1]
                Asistencia =float(linea[2].replace("%","") )
                Parcial1 = float(linea[3].replace(",","."))
                Parcial2 =float(linea[4].replace(",","."))
                Ordinario1 =float(linea[5].replace(",","."))
                Ordinario2 =float(linea[6].replace(",","."))
                Practicas = float(linea[7].replace(",","."))
                OrdinarioPracticas = float(linea[8].replace(",","."))
                lista.append({
                    'Apellidos' :Apellidos,
                    'nombre':nombre,
                    'Asistencia':Asistencia,
                    'Parcial1' :Parcial1,
                    'Parcial2':Parcial2,
                    'Ordinario1' : Ordinario1,
                    'Ordinario2' :Ordinario2,
                    'Practicas' :Practicas,
                    'OrdinarioPracticas' :OrdinarioPracticas
                })
                print(lista)





            else:
                pos = 1
    return lista                
obtener_fichero_de_calificaciones()
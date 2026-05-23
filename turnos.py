import mysql.connector
#CONEXION A SQL
conexion = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "tu-password",
    database="agenda_turnos"
)
cursor = conexion.cursor()
#AGREGAR CL
def agregar cliente ():
    nombre = input ("Nombre:")
    telefono = input ("Telefono:")
    email = input ("Email:")
    sql=""
    INSERT INTO clientes (nombre, telefono, email)
    VALUES (%s,%s,%s)
    """
    valores = (nombre, telefono, email)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Cliente agregado correctamente")
#AGREGAR TURNO
def agregar_turno():
    id_cliente =input("ID del cliente:")
    fecha = input("Fecha (YYY-M-DD):")
    hora = input ("Hora(HH:MM:SS):")
    servicio = input ("Servicio:")
    sql = """
    INSERT INTO turnos
    (id_cliente, fecha.hora.servicio.estado)
    VALUES (%s, %s, %s, %s, %s)
    """
    valores = (
        id_cliente,
        fecha,
        hora,
        servicio,
        "PENDIENTE"
)
cursor.execute(sql,valores)
conexion.commit()
print("Turno agregado correctamente")
#TURNOS
def ver_turnos():
    sql = ""
    SELECT
        clientes.nombre,
        turnos.fecha,
        turnos.hora,
        turnos.servicio,
        turnos.estado
FROM turnos
JOIN clientes
ON turnos.id_cliente = clientes.id_cliente
"""
cursor.execute(sql)
resultados = cursor.fetchall()
print("n----TURNOS----")
for turno in resultados:
print(
   f"""
Cliente: {turno[0]}
Fecha:{turno[1]}
Hora:{turno[2]}
Servicio:{turno[3]}
Estado:{turno[4]}
"""
        )
#MENU
while True:
    print("""
1- Agregar cliente
2- Agregar turno
3- Ver turno
4- Salir
""")
    opcion = input ("Elegir opción:")
    if opcion == "1":
        agregar_cliente()
    elif opcion =="2":
          agregar_turno()
    if opcion =="3":
        ver_turnos()
    elif opcion == "4":
         print("Programa finalizado")
         break
    else:
        print("Opcion inválida")
cursor.close()
conexion.close()
   

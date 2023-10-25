import psycopg2
import random

conn = psycopg2.connect(
    database="",
    user="",
    password="",
    host="",
    port="5432",
    options="-c search_path="
    )

cursor = conn.cursor()

conn.autocommit = True

def generate_turno(n):
    i = 0
    while i < n:
        cursor.execute("SELECT dni FROM trabajador;")
        res = cursor.fetchall()
        dni = random.choice(res)[0]
        dia = random.choice(['L', 'M', 'X', 'J', 'V', 'S', 'D'])
        hora_entrada = random.randint(6, 9)
        hora_salida = random.randint(18, 24)
        cursor.execute(f"INSERT INTO turno(dni, dia, hora_entrada, hora_salida) VALUES ({dni}, {dia}, {hora_entrada}, {hora_salida});")
        i += 1

def generate_stock(n):
    i = 0
    cursor.execute("SELECT nombre_producto, medida FROM producto;")
    res1 = cursor.fetchall()
    cursor.execute("SELECT direccion FROM local;")
    res2 = cursor.fetchall()
    while i < n:
        try:
            fk = random.choice(res1)
            direccion = random.choice(res2)[0]
            cantidad = random.randint(0, 999)
            cursor.execute(f"SELECT nombre_producto, medida, direccion FROM stock WHERE nombre_producto='{fk[0]}' AND medida='{fk[1]}' AND direccion='{direccion}'")
            if not cursor.fetchone():
                cursor.execute(f"INSERT INTO stock(nombre_producto, medida, direccion, cantidad) VALUES ('{fk[0]}', '{fk[1]}', '{direccion}', {cantidad});")
                print("successfully inserted", i)
                i += 1
        except Exception as e:
            print(e, i)

def generate_compra_local(n):
    i = 0
    cursor.execute("SELECT correlativo FROM compra;")
    res1 = cursor.fetchall()
    cursor.execute("SELECT numero, direccion FROM caja;")
    res2 = cursor.fetchall()
    while i < n:
        try:
            correlativo = random.choice(res1)[0]
            fk = random.choice(res2)
            cursor.execute(f"SELECT correlativo FROM compralocal WHERE correlativo='{correlativo}'")
            if not cursor.fetchone():
                cursor.execute(f"INSERT INTO compralocal(correlativo, numero, direccion) VALUES ('{correlativo}', '{fk[0]}', '{fk[1]}');")
                print("successfully inserted", i + 1)
                i += 1
        except Exception as e:
            print(e, i)

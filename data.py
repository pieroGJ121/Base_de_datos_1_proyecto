import psycopg2
import random

conn = psycopg2.connect(
    database="", user="", password="", host="", port="5432", options="-c search_path="
)

cursor = conn.cursor()

conn.autocommit = True


def generate_turno(n):
    i = 0
    while i < n:
        cursor.execute("SELECT dni FROM trabajador;")
        res = cursor.fetchall()
        dni = random.choice(res)[0]
        dia = random.choice(["L", "M", "X", "J", "V", "S", "D"])
        hora_entrada = random.randint(6, 9)
        hora_salida = random.randint(18, 24)
        cursor.execute(
            f"INSERT INTO turno(dni, dia, hora_entrada, hora_salida) VALUES ({dni}, {dia}, {hora_entrada}, {hora_salida});"
        )
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
            cursor.execute(
                f"SELECT nombre_producto, medida, direccion FROM stock WHERE nombre_producto='{fk[0]}' AND medida='{fk[1]}' AND direccion='{direccion}'"
            )
            if not cursor.fetchone():
                cursor.execute(
                    f"INSERT INTO stock(nombre_producto, medida, direccion, cantidad) VALUES ('{fk[0]}', '{fk[1]}', '{direccion}', {cantidad});"
                )
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
            cursor.execute(
                f"SELECT correlativo FROM compralocal WHERE correlativo='{correlativo}'"
            )
            if not cursor.fetchone():
                cursor.execute(
                    f"INSERT INTO compralocal(correlativo, numero, direccion) VALUES ('{correlativo}', '{fk[0]}', '{fk[1]}');"
                )
                print("successfully inserted", i + 1)
                i += 1
        except Exception as e:
            print(e, i)


def generate_usuario(n):
    # Piero
    i = 0


def generate_artista_podcast(n):
    # Piero
    i = 0


def generate_artista_musical(n):
    # Jairo
    i = 0


def generate_evento(n):
    # Jairo
    i = 0


def generate_tiene_evento(n):
    # Jairo
    i = 0


def generate_red_social(n):
    # Jairo
    i = 0


def generate_tiene_red_social(n):
    # Jairo
    i = 0


def generate_playlist(n):
    # Jairo
    i = 0


def generate_almacena_playlist(n):
    # Jairo
    i = 0


def generate_favoritos(n):
    # Piero
    i = 0


def generate_cancion(n):
    i = 0
    letters = string.ascii_lowercase
    while i < n:
        idc = random.randint(100, 99999999)
        year = str(random.randint(2018, 2022))
        month = str(random.randint(1, 12))
        day = str(random.randint(1, 27))
        lang = random.choice(
            [
                "english",
                "spanish",
                "german",
                "japanese",
                "chinese",
                "hinde",
                "french",
                "portuguese",
                "bengali",
            ]
        )

        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        date = year + "-" + month + "-" + day
        nombre = "".join(random.choice(letters) for i in range(10))

        try:
            cursor.execute(
                f"INSERT INTO Contenido(ID, fechaLanzamiento, lenguaje, nombre) VALUES ({idc}, '{date}', '{lang}', '{nombre}');"
            )

            duracion = (
                "00:0"
                + str(random.randint(0, 9))
                + ":"
                + str(random.randint(0, 5))
                + str(random.randint(0, 9))
            )

            cursor.execute(
                f"INSERT INTO ContenidoAcumulable(ID, duracion) VALUES ({idc}, '{duracion}');"
            )

            genre = random.choice(
                [
                    "rock",
                    "hip-hop",
                    "pop",
                    "country",
                    "classical",
                    "opera",
                    "symphonic",
                    "jazz",
                    "eurobeat",
                    "orchestral",
                    "folk",
                ]
            )
            compositor = names.get_first_name()

            cursor.execute(
                f"INSERT INTO Cancion(ID, genero, compositor) VALUES ({idc}, '{genre}', '{compositor}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def make_cancion_correctly(n):
    i = 0


def generate_album(n):
    # Jairo
    i = 0
    letters = string.ascii_lowercase
    cursor.execute("SELECT ID FROM Cancion;")
    resc = cursor.fetchall()
    cursor.execute("SELECT ID FROM ArtistaMusical;")
    resam = cursor.fetchall()
    while i < n:
        idca = random.choice(resc)[0]
        correo = random.choice(resam)[0]
        idc = random.randint(100, 999999999)
        year = str(random.randint(2018, 2022))
        month = str(random.randint(1, 12))
        day = str(random.randint(1, 27))
        lang = random.choice(
            [
                "english",
                "spanish",
                "german",
                "japanese",
                "chinese",
                "hinde",
                "french",
                "portuguese",
                "bengali",
            ]
        )

        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        date = year + "-" + month + "-" + day
        nombre = "".join(random.choice(letters) for i in range(10))

        try:
            cursor.execute(
                f"INSERT INTO Contenido(ID, fechaLanzamiento, lenguaje, nombre) VALUES ({idc}, '{date}', '{lang}', '{nombre}');"
            )

            cursor.execute(f"INSERT INTO Album(ID) VALUES ({idc});")
            cursor.execute(
                f"INSERT INTO AlmacenaAlbum(IDC, IDA) VALUES ({idca}, {idc});"
            )
            cursor.execute(
                f"INSERT INTO CreaAlbum(correo, IDA) VALUES ('{correo}', {idc});"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_almacena_album(n):
    # Jairo
    i = 0


def generate_crea_album(n):
    # Jairo
    i = 0


def generate_crea_cancion(n):
    # Jairo
    i = 0


def generate_episodio(n):
    i = 0
    letters = string.ascii_lowercase
    cursor.execute("SELECT ID FROM Podcast;")
    res = cursor.fetchall()
    while i < n:
        idp = random.choice(res)[0]
        idc = random.randint(100, 999999)
        year = str(random.randint(2018, 2022))
        month = str(random.randint(1, 12))
        day = str(random.randint(1, 31))
        lang = random.choice(
            [
                "english",
                "spanish",
                "german",
                "japanese",
                "chinese",
                "hinde",
                "french",
                "portuguese",
                "bengali",
            ]
        )
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        date = year + "-" + month + "-" + day
        nombre = "".join(random.choice(letters) for i in range(10))

        try:
            cursor.execute(
                f"INSERT INTO Contenido(ID, fechaLanzamiento, lenguaje, nombre) VALUES ({idc}, '{date}', '{lang}', '{nombre}');"
            )

            duracion = (
                "00:0"
                + str(random.randint(0, 9))
                + ":"
                + str(random.randint(0, 5))
                + str(random.randint(0, 9))
            )

            cursor.execute(
                f"INSERT INTO ContenidoAcumulable(ID, duracion) VALUES ({idc}, '{duracion}');"
            )

            temporada = random.randint(1, 10)

            cursor.execute(
                f"INSERT INTO Episodio(ID, IDP, temporada) VALUES ({idc}, {idp}, {temporada});"
            )
            i += 1
        except Exception as e:
            print(e, i)

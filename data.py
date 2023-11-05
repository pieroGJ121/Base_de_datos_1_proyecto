import psycopg2
import random
import string
import names

conn = psycopg2.connect(
    database="", user="", password="", host="", port="5432", options="-c search_path="
)

cursor = conn.cursor()

conn.autocommit = True


def generate_artista_musical_from_usuarios(n):
    # Only use when there is data in usuarios
    i = 0
    letters = string.ascii_lowercase
    cursor.execute(
        "SELECT correo FROM Usuario EXCEPT SELECT correo FROM ArtistaPodcast;"
    )
    resc = cursor.fetchall()
    while i < n:
        correo = resc[i][0]
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
        try:
            cursor.execute(
                f"INSERT INTO ArtistaMusical(correo, generoMusical) VALUES ('{correo}', '{genre}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_evento(n):
    # Jairo
    # En mil, n es como 200 y para cada siguiente schema pones otro 0
    i = 0


def generate_tiene_evento(n):
    # Jairo
    # Los que participan son como 5 artistas en promedio por evento.
    # Para mil hay como 100 astistas musicales, asi que n es como 500. Para
    # cada siguiente schema pones otro 0
    i = 0


def generate_red_social(n):
    # Jairo
    # Este es fijo. Por cada res social principal que encuentres, lo pones. No
    # cambia respecto al schmema. El nombre seria el nombre de la red social
    i = 0


def generate_tiene_red_social(n):
    # Jairo
    # Cada artista musical tiene como 2 cuentas. Para mil, hay 100 artistas
    # musicales, asi que n es 200
    i = 0


def generate_playlist(n):
    # Jairo
    # Para mil, hay como unos 300 usuarios, asi que n es como 400. Para
    # el siguiente schema pones otro 0
    i = 0


def generate_almacena_playlist(n):
    # Jairo
    # Para mil, hay como unos 400 usuarios, asi que n es como 700. Para
    # el siguiente schema pones otro 0

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


def make_cancion_correctly():
    cursor.execute("SELECT ID FROM Cancion;")
    resc = cursor.fetchall()
    cursor.execute("SELECT correo FROM ArtistaMusical;")
    resam = cursor.fetchall()
    for idc in resc:
        correo = random.choice(resam)[0]
        cursor.execute(
            f"INSERT INTO CreaCancion(correo, IDC) VALUES ('{correo}', {idc[0]});"
        )


def generate_album(n):
    i = 0
    letters = string.ascii_lowercase
    cursor.execute("SELECT ID FROM Cancion;")
    resc = cursor.fetchall()
    cursor.execute("SELECT correo FROM ArtistaMusical;")
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
    # Deberian haber varias canciones por album, pero al probar en mi
    # computadora con favoritos, se puede demorar bastante en craer para el
    # millon. Para 1000, hora hay como 700 canciones y 70 albums, asi que n
    # es como 1200. Pones otro 0 para el siguiente schema, pero en el millon
    # que posiblemente se demore cambias el 12 por un 8. Si quieres tambien
    # puedes dejarlo por bastante tiempo
    i = 0


def generate_crea_album(n):
    # Jairo
    # Ahora hay al menos un autor para cada album. Haz que n sea como la
    # tercera parte de albumes que hay. Para 1000, hay 77, asi que n es como
    # 25. Para cada schema siguiente le pones otro 0
    i = 0


def generate_crea_cancion(n):
    # Jairo
    # Ahora hay al menos un autor para cada cancion. Haz que n sea como la
    # tercera parte de canciones que hay. Para 1000, hay 700, asi que n es como
    # 240. Para cada schema siguiente le pones otro 0
    i = 0


def generate_episodio(n):
    i = 0
    letters = string.ascii_lowercase
    cursor.execute("SELECT ID FROM Podcast;")
    res = cursor.fetchall()
    while i < n:
        idp = random.choice(res)[0]
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

            temporada = random.randint(1, 10)

            cursor.execute(
                f"INSERT INTO Episodio(ID, IDP, temporada) VALUES ({idc}, {idp}, {temporada});"
            )
            i += 1
        except Exception as e:
            print(e, i)

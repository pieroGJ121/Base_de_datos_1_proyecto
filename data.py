import psycopg2
import random
import string
import names
import names
from faker import Faker
import datetime

conn = psycopg2.connect(
    database="bd1_proyecto",
    user="postgres",
    password="",
    host="",
    port="5432",
    options="-c search_path=mil",
)

cursor = conn.cursor()

conn.autocommit = True

fake = Faker()

upper_limit_date = datetime.date(year=2024, month=12, day=30)
lower_limit_date = datetime.date(year=2018, month=1, day=1)


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


def generate_podcast(n):
    # Only use when there is data in usuarios
    i = 0
    letters = string.ascii_lowercase
    cursor.execute(
        "SELECT correo, fecha_creacion FROM ArtistaPodcast NATURAL JOIN Usuario;"
    )
    resc = cursor.fetchall()
    while i < n:
        idp = random.randint(100, 2147483645)
        artista = random.choice(resc)
        correo = artista[0]
        fecha = artista[1]
        date = fake.date_between(start_date=fecha, end_date=upper_limit_date).strftime(
            "%Y-%m-%d"
        )
        nombre = names.get_first_name()
        original = bool(random.getrandbits)
        try:
            cursor.execute(
                f"INSERT INTO Podcast(ID, nombre, original, fecha) VALUES ('{idp}', '{nombre}', {original}, '{date}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_evento(n):
    # Jairo
    # En mil, n es como 200 y para cada siguiente schema pones otro 0
    i = 0
    cursor.execute(
        "SELECT correo, fecha_creacion FROM ArtistaMusical NATURAL JOIN USUARIO;"
    )
    resc = cursor.fetchall()

    while i < n:
        ide = random.randint(100, 2147483645)
        nombre = "".join(random.choice(string.ascii_letters) for i in range(15))
        lugar = random.choice(
            [
                "Belgica",
                "California",
                "Miami",
                "Las Vegas",
                "Holanda ",
                "Chicago",
                "Australia ",
                "Paises Bajos",
                "Mexico",
                "Reino Unido",
            ]
        )
        user = random.choice(resc)  # cambiar el resc_2[n]
        correo = user[0]
        fecha = user[1]

        date = fake.date_between(start_date=fecha, end_date=upper_limit_date).strftime(
            "%Y-%m-%d"
        )

        try:
            # aritsita musical debe existir para q ocurra el evento
            cursor.execute(
                f"INSERT INTO Evento(ID,nombre, fecha, lugar ) VALUES ('{ide}', '{nombre}', '{date}', '{lugar}');"
            )
            cursor.execute(
                f"INSERT INTO TieneEventos(correo, ID) VALUES ('{correo}', '{ide}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_tiene_evento(n):
    # Los que participan son como 5 artistas en promedio por evento.
    # Para mil hay como 100 astistas musicales, asi que n es como 500. Para
    # cada siguiente schema pones otro 0

    # aun no esta implementado lo de arriba ^|
    i = 0
    cursor.execute(
        "SELECT correo, fecha_creacion FROM ArtistaMusical NATURAL JOIN Usuario;"
    )
    resc_1 = cursor.fetchall()
    cursor.execute("SELECT ID, fecha FROM Evento;")
    resc_2 = cursor.fetchall()
    # while para sacar una fecha mmenor y que el artista musical pueda participar en el evento

    while i < n:
        evento = random.choice(resc_2)
        user = random.choice(resc_1)
        while True:
            if user[1].strftime("%Y:%m:%d") <= evento[1].strftime("%Y:%m:%d"):
                break
            else:
                user = random.choice(resc_1)
                evento = random.choice(resc_2)
        correo = user[0]
        ide = evento[0]
        try:
            cursor.execute(
                f"INSERT INTO TieneEventos(correo, ID) VALUES ('{correo}', '{ide}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_red_social():
    # Jairo
    # Este es fijo. Por cada res social principal que encuentres, lo pones. No
    # cambia respecto al schmema. El nombre seria el nombre de la red social
    i = 0
    nombre = [
        "Facebook",
        "Youtube",
        "Instagram",
        "TikTok",
        "Twitter",
        "SoundCloud",
        "Bandcamp",
        "LoudUp",
        "Discord",
        "Threads",
    ]
    for i in nombre:
        cursor.execute(f"INSERT INTO RedSocial(nombre) VALUES ('{i}');")


def generate_tiene_red_social(n):
    # Jairo
    # Cada artista musical tiene como 2 cuentas. Para mil, hay 100 artistas
    # musicales, asi que n es 200

    # aun no esta implementado lo de arriba ^|
    i = 0
    cursor.execute("SELECT correo FROM ArtistaMusical;")
    resc_1 = cursor.fetchall()
    cursor.execute("SELECT nombre FROM RedSocial;")
    resc_2 = cursor.fetchall()
    while i < n:
        correo = random.choice(resc_1)[0]
        nombreRed = random.choice(resc_2)[0]
        username = "".join(random.choice(string.ascii_letters) for i in range(10))
        try:
            cursor.execute(
                f"INSERT INTO TieneRedes(correo, nombreRed, username) VALUES ('{correo}', '{nombreRed}', '{username}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_playlist(n):
    # Jairo
    # Para mil, hay como unos 300 usuarios, asi que n es como 400. Para
    # el siguiente schema pones otro 0

    # aun no esta implementado lo de arriba ^|
    i = 0
    cursor.execute("SELECT correo, fecha_creacion FROM Usuario;")
    resc = cursor.fetchall()
    while i < n:
        id = random.randint(100, 2147483645)
        user = random.choice(resc)
        correo = user[0]
        fecha = user[1]
        date = fake.date_between(start_date=fecha, end_date=upper_limit_date).strftime(
            "%Y-%m-%d"
        )
        privacidad = random.choice([True, False])
        nombre = "".join(random.choice(string.ascii_letters) for i in range(15))
        descripcion = "".join(random.choice(string.ascii_letters) for i in range(40))

        try:
            cursor.execute(
                f"INSERT INTO Playlist(ID, correo, fecha_creacion, privacidad, nombre, descripcion) VALUES ({id}, '{correo}', '{date}', {privacidad}, '{nombre}', '{descripcion}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_almacena_playlist(n):
    # Jairo
    # Para mil, hay como unos 400 usuarios, asi que n es como 700. Para
    # el siguiente schema pones otro 0

    i = 0
    cursor.execute(
        "SELECT ID, fecha_creacion FROM Playlist;"
    )  # ,selcet id, fecha de cracion
    resc_1 = cursor.fetchall()
    cursor.execute(
        "SELECT ID, fechaLanzamiento FROM ContenidoAcumulable NATURAL JOIN Contenido;"
    )  # join con ocntenido par aobtener fecha
    resc_2 = cursor.fetchall()
    # falta verificacion de fecha paraabotener fecha menor
    while i < n:
        playlist = random.choice(resc_1)
        contenido = random.choice(resc_2)
        while True:
            if playlist[1].strftime("%Y:%m:%d") > contenido[1].strftime("%Y:%m:%d"):
                break
            else:
                contenido = random.choice(resc_2)
                playlist = random.choice(resc_1)
        idp = playlist[0]
        idca = contenido[0]
        try:
            cursor.execute(
                f"INSERT INTO AlmacenaPlaylist(IDP, IDCA) VALUES ('{idp}', '{idca}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_cancion(n):
    i = 0
    letters = string.ascii_lowercase
    cursor.execute(
        "SELECT correo, fecha_creacion FROM ArtistaMusical NATURAL JOIN Usuario;"
    )
    resam = cursor.fetchall()
    while i < n:
        artista = random.choice(resam)
        correo = artista[0]
        fecha_artista = artista[1]
        idc = random.randint(100, 2147483645)
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

        date = fake.date_between(
            start_date=fecha_artista, end_date=upper_limit_date
        ).strftime("%Y-%m-%d")
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
                + ":"
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
            cursor.execute(
                f"INSERT INTO CreaCancion(correo, IDC) VALUES ('{correo}', {idc});"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_album(n):
    i = 0
    letters = string.ascii_lowercase
    cursor.execute("SELECT ID FROM Cancion;")
    resc = cursor.fetchall()
    cursor.execute(
        "SELECT correo, fecha_creacion FROM ArtistaMusical NATURAL JOIN Usuario;"
    )
    resam = cursor.fetchall()
    while i < n:
        idca = random.choice(resc)[0]
        artista = random.choice(resam)
        correo = artista[0]
        fecha_artista = artista[1]
        idc = random.randint(100, 2147483645)
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

        date = fake.date_between(
            start_date=fecha_artista, end_date=upper_limit_date
        ).strftime("%Y-%m-%d")
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
    cursor.execute(
        "SELECT ID, fechaLanzamiento FROM Cancion NATURAL JOIN Contenido;"
    )  # join con ncontenido apra verificar fecha primero se elige el album y luego la fecha
    resc_1 = cursor.fetchall()
    cursor.execute(
        "SELECT ID, fechaLanzamiento FROM Album NATURAL JOIN Contenido;"
    )  # verificar que la fecha d ealbum
    resc_2 = cursor.fetchall()
    while i < n:
        cancion = random.choice(resc_1)
        album = random.choice(resc_2)
        while True:
            if album[1].strftime("%Y:%m:%d") <= cancion[1].strftime("%Y:%m:%d"):
                break
            else:
                cancion = random.choice(resc_1)
                album = random.choice(resc_2)
        idc = cancion[0]
        ida = album[0]
        try:
            cursor.execute(
                f"INSERT INTO AlmacenaAlbum( IDC, IDA ) VALUES ('{idc}', '{ida}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_crea_album(n):
    # Jairo
    # Ahora hay al menos un autor para cada album. Haz que n sea como la
    # tercera parte de albumes que hay. Para 1000, hay 77, asi que n es como
    # 25. Para cada schema siguiente le pones otro 0
    i = 0
    cursor.execute(
        "SELECT correo, fecha_creacion FROM Usuario NATURAL JOIN ArtistaMusical;"
    )  # join artista con usuario
    resc_1 = cursor.fetchall()
    cursor.execute(
        "SELECT ID, fechaLanzamiento FROM Album NATURAL JOIN Contenido;"
    )  # join
    resc_2 = cursor.fetchall()
    while i < n:
        album = random.choice(resc_2)
        user = random.choice(resc_1)
        while True:
            if user[1].strftime("%Y:%m:%d") >= album[1].strftime("%Y:%m:%d"):
                break
            else:
                album = random.choice(resc_2)
                user = random.choice(resc_1)
        correo = user[0]
        ida = album[0]
        try:
            cursor.execute(
                f"INSERT INTO CreaAlbum( correo, IDA ) VALUES ('{correo}', '{ida}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_crea_cancion(n):
    # Jairo
    # Ahora hay al menos un autor para cada cancion. Haz que n sea como la
    # tercera parte de canciones que hay. Para 1000, hay 700, asi que n es como
    # 240. Para cada schema siguiente le pones otro 0
    i = 0
    cursor.execute(
        "SELECT correo, fecha_creacion FROM Usuario NATURAL JOIN ArtistaMusical;"
    )  # join con useuaro
    resc_1 = cursor.fetchall()
    cursor.execute(
        "SELECT ID, fechaLanzamiento FROM Cancion NATURAL JOIN Contenido;"
    )  # join con nontenido
    # while con fecha par aobtener una fecha valida
    resc_2 = cursor.fetchall()
    while i < n:
        user = random.choice(resc_1)
        cancion = random.choice(resc_2)
        while True:
            if user[1].strftime("%Y:%m:%d") <= cancion[1].strftime("%Y:%m:%d"):
                break
            else:
                cancion = random.choice(resc_2)
                user = random.choice(resc_1)
        correo = user[0]
        idc = cancion[0]
        try:
            cursor.execute(
                f"INSERT INTO CreaCancion(correo, idc ) VALUES ('{correo}', '{idc}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_episodio(n):
    i = 0
    letters = string.ascii_lowercase
    cursor.execute("SELECT ID, fecha FROM Podcast;")
    res = cursor.fetchall()
    while i < n:
        podcast = random.choice(res)
        idp = podcast[0]
        fecha_podcast = podcast[1]
        idc = random.randint(100, 2147483645)
        date = fake.date_between(
            start_date=fecha_podcast, end_date=upper_limit_date
        ).strftime("%Y-%m-%d")
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
        nombre = "".join(random.choice(letters) for i in range(10))

        try:
            cursor.execute(
                f"INSERT INTO Contenido(ID, fechaLanzamiento, lenguaje, nombre) VALUES ({idc}, '{date}', '{lang}', '{nombre}');"
            )

            duracion = (
                "0"
                + str(random.randint(0, 2))
                + ":"
                + str(random.randint(0, 5))
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


def create_mil():
    conn = psycopg2.connect(
        database="bd1_proyecto",
        user="postgres",
        password="",
        host="",
        port="5432",
        options="-c search_path=mil",
    )

    global cursor
    cursor = conn.cursor()

    conn.autocommit = True

    # Executed beforehand
    generate_cancion(650)
    generate_crea_cancion(220)
    generate_album(70)
    generate_almacena_album(400)
    generate_crea_album(30)

    generate_podcast(80)
    generate_episodio(330)

    # generate_evento(200)
    # generate_tiene_evento(300)

    # generate_red_social()
    # generate_tiene_red_social(300)

    generate_playlist(400)
    generate_almacena_playlist(640)


def create_diezmil():
    conn = psycopg2.connect(
        database="bd1_proyecto",
        user="postgres",
        password="",
        host="",
        port="5432",
        options="-c search_path=diezmil",
    )

    global cursor
    cursor = conn.cursor()

    conn.autocommit = True

    # generate_cancion(650 * 10)
    # generate_crea_cancion(220 * 10)
    generate_album(70 * 10)
    generate_almacena_album(400 * 10)
    generate_crea_album(30 * 10)

    generate_podcast(80 * 10)
    generate_episodio(330 * 10)

    generate_evento(200 * 10)
    generate_tiene_evento(450 * 10)

    # generate_red_social()
    # generate_tiene_red_social(300 * 10)

    generate_playlist(400 * 10)
    generate_almacena_playlist(640 * 10)


def create_cienmil():
    conn = psycopg2.connect(
        database="bd1_proyecto",
        user="postgres",
        password="",
        host="",
        port="5432",
        options="-c search_path=cienmil",
    )

    global cursor
    cursor = conn.cursor()

    conn.autocommit = True

    generate_cancion(650 * 100)
    generate_crea_cancion(220 * 100)
    generate_album(70 * 100)
    generate_almacena_album(400 * 100)
    generate_crea_album(30 * 100)

    generate_podcast(80 * 100)
    generate_episodio(330 * 100)

    generate_evento(200 * 100)
    generate_tiene_evento(450 * 100)

    generate_red_social()
    generate_tiene_red_social(300 * 100)

    generate_playlist(400 * 100)
    generate_almacena_playlist(640 * 100)


def create_milllon():
    conn = psycopg2.connect(
        database="bd1_proyecto",
        user="postgres",
        password="",
        host="",
        port="5432",
        options="-c search_path=millon",
    )

    global cursor
    cursor = conn.cursor()

    conn.autocommit = True

    generate_cancion(650 * 1000)
    generate_crea_cancion(220 * 1000)
    generate_album(70 * 1000)
    generate_almacena_album(350 * 1000)
    generate_crea_album(30 * 1000)

    generate_podcast(80 * 1000)
    generate_episodio(330 * 1000)

    generate_evento(200 * 1000)
    generate_tiene_evento(450 * 1000)

    generate_red_social()
    generate_tiene_red_social(200 * 1000)

    generate_playlist(400 * 1000)
    generate_almacena_playlist(600 * 1000)


# Falta el almacena y crea  de album, y el almacena de playlist

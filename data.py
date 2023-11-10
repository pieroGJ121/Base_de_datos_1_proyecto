import psycopg2
import random
import string
import names

conn = psycopg2.connect(
    database="postgres", user="postgres", password="Kw51XS123.", host="localhost", port="5432", options="-c search_path="
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
    cursor.execute("SELECT correo, fecha_creacion FROM ArtistaMusical;")
    resc = cursor.fetchall()

    while i < n:
        ide = random.randint(100, 99999999)
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

        fecha_creacion = f"{ random.randint(fecha.year, 2023) }-{ random.randint(fecha.month, 12) }-{ random.randint(fecha.day, 30) }"

        try:
            # aritsita musical debe existir para q ocurra el evento
            cursor.execute(
                f"INSERT INTO Evento(ID,nombre, fecha, lugar ) VALUES ('{ide}', '{nombre}', '{fecha_creacion}', '{lugar}');"
            )
            cursor.execute(f"INSERT INTO TieneEventos(ID) VALUES ('{ide}');")
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
            if user[1] <= evento[1]:
                break
            else:
                user = random.choice(resc_1)
        correo = user[0]
        ide = evento[0]
        try:
            cursor.execute(
                f"INSERT INTO TieneEvento(correo, ID) VALUES ('{correo}', '{ide}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


def generate_red_social():
    # Jairo
    # Este es fijo. Por cada res social principal que encuentres, lo pones. No
    # cambia respecto al schmema. El nombre seria el nombre de la red social
    i = 0
    nombre = random.choice(
        [
            "Facebook",
            "Youtube",
            "Instagram",
            "TikTok",
            "Twitter",
            "SoundCloud",
        ]
    )
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
        id = random.randint(100, 99999999)
        user = random.choice(resc)
        correo = user[0]
        fecha = user[1]
        fecha_creacion = f"{ random.randint(fecha.year, 2023) }-{ random.randint(fecha.mes, 12) }-{ random.randint(fecha.day, 30) }"
        privacidad = random.choice([True, False])
        nombre = "".join(random.choice(string.ascii_letters) for i in range(15))
        descripcion = "".join(random.choice(string.ascii_letters) for i in range(40))

        try:
            cursor.execute(
                f"INSERT INTO Playlist(ID, correo, fecha_creacion, privacidad, nombre, descripcion) VALUES ({id}, '{correo}', '{fecha_creacion}', {privacidad}, '{nombre}', '{descripcion}');"
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
            if playlist[1] > contenido[1]:
                break
            else:
                contenido = random.choice(resc_2)
        idp = playlist[0]
        idca = contenido[0]
        try:
            cursor.execute(
                f"INSERT INTO AlmacenaPlaylist( IDP, IDCA ) VALUES ('{idp}', '{idca}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


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
            if album[1] <= cancion[1]:
                break
            else:
                cancion = random.choice(resc_1)
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
            if user[1] >= album[1]:
                break
            else:
                album = random.choice(resc_2)
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
            if user[1] <= cancion[1]:
                break
            else:
                cancion = random.choice(resc_2)
        correo = user[0]
        idc = cancion[0]
        try:
            cursor.execute(
                f"INSERT INTO AlmacenaPlaylist( IDC, IDA ) VALUES ('{correo}', '{idc}');"
            )
            i += 1
        except Exception as e:
            print(e, i)


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

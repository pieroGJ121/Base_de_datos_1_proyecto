-- Creacion de tablas

CREATE TABLE Usuario(
	correo VARCHAR(255)  PRIMARY KEY,
	username VARCHAR(100),
	contrasenia VARCHAR(100),
	pais VARCHAR(60),
	fecha_creacion DATE,
	imagen_perfil VARCHAR(100),
	tipo_suscripcion BOOLEAN
);

CREATE TABLE Playlist(
	ID INT PRIMARY KEY,
	correo_usuario  VARCHAR(255) FOREIGN KEY REFERENCES Usuario(correo),
	fecha_creacion DATE,
	privacidad BOOLEAN,
	nombre  VARCHAR(100),
	descripcion  VARCHAR(400)
);

CREATE TABLE Contenido(
	ID,
	fechaLanzamiento,
	lenguaje,
	nombre,
	portada
);

CREATE TABLE ArtistaMusical(
	correo_usuario FOREIGN KEY REFERENCES Usuario(correo),
	genero_musica
);

CREATE TABLE RedSocial(
	nombre
);

CREATE TABLE Evento(
	nombre,
	fecha,
	lugar
);

CREATE TABLE ArtistaPodcast(
	correo_usuario FOREIGN KEY REFERENCES Usuario(correo)
);

CREATE TABLE ContenidoAcumulable(
	ID FOREIGN KEY REFERENCES Contenido(ID),
	duracion
);

CREATE TABLE Podcast(
	nombre,
	original
);

CREATE TABLE Temporada(
	ID FOREIGN KEY REFERENCES Contenido(ID),
	nombre FOREIGN KEY REFERENCES Podcast(nombre)
);

CREATE TABLE Album(
	ID FOREIGN KEY REFERENCES Contenido(ID)
);

CREATE TABLE Episodio(
	ID FOREIGN KEY REFERENCES Contenido(ID),
	nombre FOREIGN KEY REFERENCES Podcast(nombre)
);

CREATE TABLE Cancion(
	ID FOREIGN KEY REFERENCES Contenido(ID),
	genero,
	letra,
	compositor
);

CREATE TABLE Favoritos(
	correo FOREIGN KEY REFERENCES Usuario(correo),
	ID FOREIGN KEY REFERENCES ContenidoAcumulable(ID)
);

CREATE TABLE AlmacenaPlaylist(
	IDplaylist FOREIGN KEY REFERENCES Playlist(ID),
	correo FOREIGN KEY REFERENCES Usuario(correo),
	ID_CA FOREIGN KEY REFERENCES ContenidoAcumulable(ID)
);

CREATE TABLE Participa(
	correo FOREIGN KEY REFERENCES ArtistaPodcast(correo_usuario)
);

CREATE TABLE TieneRedes(
	correo FOREIGN KEY REFERENCES ArtistaPodcast(correo_usuario),
	ID_RS FOREIGN KEY REFERENCES RedSocial(nombre),
	username
);

CREATE TABLE TieneEventos(
	correo FOREIGN KEY REFERENCES ArtistaPodcast(correo_usuario),
	nombre FOREIGN KEY REFERENCES Evento(nombre)
);

CREATE TABLE AlmacenaTemporada(
	ID_Ep FOREIGN KEY REFERENCES Episodio(ID),
	ID_Tmp FOREIGN KEY REFERENCES Temporada(ID)
);

CREATE TABLE AlmacenaAlbum(
	ID_Cn FOREIGN KEY REFERENCES Cancion(ID),
	ID_Ab FOREIGN KEY REFERENCES Album(ID)
);

CREATE TABLE CreaAlbum(
	correo FOREIGN KEY REFERENCES ArtistaMusical(correo),
	ID_Ab FOREIGN KEY REFERENCES Album(ID)
);

CREATE TABLE CreaCancion(
	correo FOREIGN KEY REFERENCES ArtistaMusical(correo),
	ID_Cn FOREIGN KEY REFERENCES Cancion(ID)
);

CREATE TABLE CreaEpisodio(
	nombre FOREIGN KEY REFERENCES Podcast(Nombre),
	ID_Ep FOREIGN KEY REFERENCES Episodio(ID)
);

CREATE TABLE Temporada(
	nombre FOREIGN KEY REFERENCES Podcast(Nombre),
	ID_Tmp FOREIGN KEY REFERENCES Temporada(ID)
);


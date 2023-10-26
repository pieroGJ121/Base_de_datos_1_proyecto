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
	ID INT PRIMARY KEY,
	fechaLanzamiento DATE,
	lenguaje VARCHAR(30),
	nombre VARCHAR(50),
	portada VARCHAR(100)
);

CREATE TABLE ArtistaMusical(
	correo_usuario  VARCHAR(255) FOREIGN KEY REFERENCES Usuario(correo),
	genero_musica VARCHAR(30)
);

CREATE TABLE RedSocial(
	nombre VARCHAR(30) PRIMARY KEY
);

CREATE TABLE Evento(
	nombre VARCHAR(100) PRIMARY KEY,
	fecha DATE,
	lugar VARCHAR(50)	
);

CREATE TABLE ArtistaPodcast(
	correo_usuario VARCHAR(255) FOREIGN KEY REFERENCES Usuario(correo)
);



CREATE TABLE ContenidoAcumulable(
	ID INT FOREIGN KEY REFERENCES Contenido(ID),
	duracion TIME
);

CREATE TABLE Podcast(
	nombre VARCHAR(30) PRIMARY KEY,
	original BOOLEAN
);

CREATE TABLE Temporada(
	ID INT FOREIGN KEY REFERENCES Contenido(ID),
	nombre VARCHAR(30) FOREIGN KEY REFERENCES Podcast(nombre)
);

CREATE TABLE Album(
	ID INT FOREIGN KEY REFERENCES Contenido(ID)
);

CREATE TABLE Episodio(
	ID INT FOREIGN KEY REFERENCES Contenido(ID),
	nombre VARCHAR(30) FOREIGN KEY REFERENCES Podcast(nombre)
);

CREATE TABLE Cancion(
	ID INT FOREIGN KEY REFERENCES Contenido(ID),
	genero  VARCHAR(30),
	letra  VARCHAR(1000),
	compositor  VARCHAR(30)
);

CREATE TABLE Favoritos(
	correo VARCHAR(255) FOREIGN KEY REFERENCES Usuario(correo),
	ID INT FOREIGN KEY REFERENCES ContenidoAcumulable(ID)
);

CREATE TABLE AlmacenaPlaylist(
	IDplaylist INT FOREIGN KEY REFERENCES Playlist(ID),
	correo VARCHAR(255) FOREIGN KEY REFERENCES Usuario(correo),
	ID_CA INT FOREIGN KEY REFERENCES ContenidoAcumulable(ID)
);

CREATE TABLE Participa(
	correo VARCHAR(255) FOREIGN KEY REFERENCES ArtistaPodcast(correo_usuario),
	nombre VARCHAR(30)  FOREING KEY REFERENCES Podcast(Nombre)
);


CREATE TABLE TieneRedes(
	correo VARCHAR(255) FOREIGN KEY REFERENCES ArtistaPodcast(correo_usuario),
	nombre_Red VARCHAR(30) FOREIGN KEY REFERENCES RedSocial(nombre),
	username VARCHAR(30)
);

CREATE TABLE TieneEventos(
	correo VARCHAR(255) FOREIGN KEY REFERENCES ArtistaPodcast(correo_usuario),
	nombre VARCHAR(100) FOREIGN KEY REFERENCES Evento(nombre)
);

CREATE TABLE AlmacenaTemporada(
	ID_Ep INT FOREIGN KEY REFERENCES Episodio(ID),
	ID_Tmp INT FOREIGN KEY REFERENCES Temporada(ID)
);

CREATE TABLE AlmacenaAlbum(
	ID_Cn INT FOREIGN KEY REFERENCES Cancion(ID),
	ID_Ab INT FOREIGN KEY REFERENCES Album(ID)
);

CREATE TABLE CreaAlbum(
	correo VARCHAR(255) FOREIGN KEY REFERENCES ArtistaMusical(correo),
	ID_Ab INT FOREIGN KEY REFERENCES Album(ID)
);

CREATE TABLE CreaCancion(
	correo VARCHAR(255) FOREIGN KEY REFERENCES ArtistaMusical(correo),
	ID_Cn INT FOREIGN KEY REFERENCES Cancion(ID)
);

CREATE TABLE CreaEpisodio(
	nombre VARCHAR(30) FOREIGN KEY REFERENCES Podcast(Nombre),
	ID_Ep INT FOREIGN KEY REFERENCES Episodio(ID)
);

CREATE TABLE Temporada(
	nombre VARCHAR(30) FOREIGN KEY REFERENCES Podcast(Nombre),
	ID_Tmp INT FOREIGN KEY REFERENCES Temporada(ID)
);
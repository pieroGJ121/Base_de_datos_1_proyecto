-- Creacion de tablas

CREATE TABLE Usuario(
	correo VARCHAR(20)  PRIMARY KEY,
	username VARCHAR(15),
	contrasenia VARCHAR(10),
	pais VARCHAR(40),
	fecha_creacion DATE,
	tipo_suscripcion BOOLEAN
);

CREATE TABLE Playlist(
	ID INT PRIMARY KEY,
	correo VARCHAR(20),
	fecha_creacion DATE,
	privacidad BOOLEAN,
	nombre  VARCHAR(15),
	descripcion  VARCHAR(40)
);
ALTER TABLE playlist ADD CONSTRAINT usuario_fk_correo
FOREIGN KEY (correo) REFERENCES Usuario (correo);

CREATE TABLE Contenido(
	ID INT PRIMARY KEY,
	fechaLanzamiento DATE,
	lenguaje VARCHAR(10),
	nombre VARCHAR(15)
);

CREATE TABLE ArtistaMusical(
	correo  VARCHAR(20) PRIMARY KEY,
	genero_musica VARCHAR(10)
);
ALTER TABLE ArtistaMusical ADD CONSTRAINT usuario_fk_correo
FOREIGN KEY (correo) REFERENCES Usuario (correo);

CREATE TABLE RedSocial(
	nombre VARCHAR(15) PRIMARY KEY
);

CREATE TABLE Evento(
	nombre VARCHAR(15) PRIMARY KEY,
	fecha DATE,
	lugar VARCHAR(15)
);

CREATE TABLE ArtistaPodcast(
	correo VARCHAR(20) PRIMARY KEY
);
ALTER TABLE ArtistaPodcast ADD CONSTRAINT usuario_fk_correo
FOREIGN KEY (correo) REFERENCES Usuario (correo);


CREATE TABLE ContenidoAcumulable(
	ID INT PRIMARY KEY,
	duracion TIME
	FOREIGN KEY (ID) REFERENCES Contenido(ID)
);
ALTER TABLE ContenidoAcumulable ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);

CREATE TABLE Podcast(
	ID INT PRIMARY KEY,
	nombre VARCHAR(15),
	original BOOLEAN
);

CREATE TABLE Album(
	ID INT PRIMARY KEY
);
ALTER TABLE Album ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);

CREATE TABLE Episodio(
ID INT PRIMARY KEY,
IDP INT,
temporada VARCHAR(15)
);
ALTER TABLE Episodio ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);
ALTER TABLE Episodio ADD CONSTRAINT podcast_fk_id
FOREIGN KEY (IDP) REFERENCES Podcast (ID);

CREATE TABLE Cancion(
	ID INT PRIMARY KEY,
	genero  VARCHAR(10),
	compositor  VARCHAR(15)
);
ALTER TABLE Cancion ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);

CREATE TABLE Favoritos(
	correo VARCHAR(20) PRIMARY KEY,
	ID INT PRIMARY KEY
);
ALTER TABLE Favoritos ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);
ALTER TABLE Favoritos ADD CONSTRAINT usuario_fk_correo
FOREIGN KEY (correo) REFERENCES Usuario (correo);

CREATE TABLE AlmacenaPlaylist(
	IDP INT,
	IDCA INT
);
ALTER TABLE AlmacenaPlaylist ADD CONSTRAINT playlist_fk_id
FOREIGN KEY (IDP) REFERENCES Playlist (ID);
ALTER TABLE AlmacenaPlaylist ADD CONSTRAINT ca_fk_id
FOREIGN KEY (IDCA) REFERENCES ContenidoAcumulable (ID);

CREATE TABLE Participa(
	correo VARCHAR(20),
	IDP INT
);
ALTER TABLE Participa ADD CONSTRAINT participa_pk
PRIMARY KEY (correo, IDP);
ALTER TABLE Participa ADD CONSTRAINT ap_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaPodcast (correo);
ALTER TABLE Participa ADD CONSTRAINT podcast_fk_id
FOREIGN KEY (IDP) REFERENCES Podcast (ID);


CREATE TABLE TieneRedes(
	correo VARCHAR(20) PRIMARY KEY,
	nombreRed VARCHAR(10) PRIMARY KEY,
	username VARCHAR(10)
);
ALTER TABLE TieneRedes ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE TieneRedes ADD CONSTRAINT red_fk_nombre
FOREIGN KEY (nombreRed) REFERENCES RedSocial (nombre);

CREATE TABLE TieneEventos(
	correo VARCHAR(20) PRIMARY KEY,
	nombre VARCHAR(15) PRIMARY KEY
);
ALTER TABLE TieneEventos ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE TieneEventos ADD CONSTRAINT evento_fk_nombre
FOREIGN KEY (nombre) REFERENCES Evento (nombre);

CREATE TABLE AlmacenaAlbum(
	IDC INT PRIMARY KEY,
	IDA INT PRIMARY KEY
);
ALTER TABLE AlmacenaAlbum ADD CONSTRAINT cancion_fk_id
FOREIGN KEY (IDC) REFERENCES Cancion (ID);
ALTER TABLE AlmacenaAlbum ADD CONSTRAINT album_fk_id
FOREIGN KEY (IDA) REFERENCES Album (ID);

CREATE TABLE CreaAlbum(
	correo VARCHAR(20) PRIMARY KEY,
	IDA INT PRIMARY KEY
);
ALTER TABLE CreaAlbum ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE CreaAlbum ADD CONSTRAINT album_fk_id
FOREIGN KEY (IDA) REFERENCES Album (ID);

CREATE TABLE CreaCancion(
	correo VARCHAR(20) PRIMARY KEY,
	IDC INT PRIMARY KEY
);
ALTER TABLE CreaCancion ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE CreaCancion ADD CONSTRAINT cancion_fk_id
FOREIGN KEY (IDC) REFERENCES cancion (ID);

CREATE TABLE CreaEpisodio(
	IDP INT PRIMARY KEY,
	IDE INT PRIMARY KEY
);
ALTER TABLE CreaEpisodio ADD CONSTRAINT podcast_fk_id
FOREIGN KEY (ID) REFERENCES Podcast (ID);
ALTER TABLE CreaEpisodio ADD CONSTRAINT episodio_fk_id
FOREIGN KEY (IDE) REFERENCES Episodio (ID);


ALTER TABLE Usuario MODIFY COLUMN ID NOT NULL;
ALTER TABLE Playlist MODIFY COLUMN ID NOT NULL;
ALTER TABLE Contenido MODIFY COLUMN ID NOT NULL;
ALTER TABLE ArtistaMusical MODIFY COLUMN ID NOT NULL;
ALTER TABLE RedSocial MODIFY COLUMN nombre NOT NULL;
ALTER TABLE Evento MODIFY COLUMN nombre NOT NULL;
ALTER TABLE ArtistaPodcast MODIFY COLUMN ID NOT NULL;
ALTER TABLE ContenidoAcumulable MODIFY COLUMN ID NOT NULL;
ALTER TABLE Podcast MODIFY COLUMN nombre NOT NULL;
ALTER TABLE Album MODIFY COLUMN ID NOT NULL;
ALTER TABLE Episodio MODIFY COLUMN ID NOT NULL;
ALTER TABLE Cancion MODIFY COLUMN ID NOT NULL;
ALTER TABLE Favoritos MODIFY COLUMN ID NOT NULL;
ALTER TABLE AlmacenaPlaylist MODIFY COLUMN IDplaylist NOT NULL;
ALTER TABLE Participa MODIFY COLUMN nombre NOT NULL;
ALTER TABLE TieneRedes MODIFY COLUMN nombre_Red NOT NULL;
ALTER TABLE TieneEventos MODIFY COLUMN nombre NOT NULL;
ALTER TABLE AlmacenaAlbum MODIFY COLUMN ID_Cn NOT NULL;
ALTER TABLE CreaAlbum MODIFY COLUMN ID_Ab NOT NULL;
ALTER TABLE CreaCancion MODIFY COLUMN ID_Cn NOT NULL;
ALTER TABLE CreaEpisodio MODIFY COLUMN ID_Ep NOT NULL;

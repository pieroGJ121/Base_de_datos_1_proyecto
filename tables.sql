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
	generoMusical VARCHAR(10)
);
ALTER TABLE ArtistaMusical ADD CONSTRAINT usuario_fk_correo
FOREIGN KEY (correo) REFERENCES Usuario (correo);

CREATE TABLE RedSocial(
	nombre VARCHAR(15) PRIMARY KEY
);

CREATE TABLE Evento(
 	ID INT PRIMARY KEY,
	nombre VARCHAR(15),
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
);
ALTER TABLE ContenidoAcumulable ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);

CREATE TABLE Podcast(
	ID INT PRIMARY KEY,
	nombre VARCHAR(15),
	original BOOLEAN,
	fecha DATE,
);

CREATE TABLE Album(
	ID INT PRIMARY KEY,
);
ALTER TABLE Album ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);

CREATE TABLE Episodio(
ID INT PRIMARY KEY,
IDP INT,
temporada INT
);
ALTER TABLE Episodio ADD CONSTRAINT ca_fk_id
FOREIGN KEY (ID) REFERENCES ContenidoAcumulable (ID);
ALTER TABLE Episodio ADD CONSTRAINT podcast_fk_id
FOREIGN KEY (IDP) REFERENCES Podcast (ID);

CREATE TABLE Cancion(
	ID INT PRIMARY KEY,
	genero VARCHAR(10),
	compositor  VARCHAR(15),
);
ALTER TABLE Cancion ADD CONSTRAINT ca_fk_id
FOREIGN KEY (ID) REFERENCES ContenidoAcumulable (ID);

CREATE TABLE Favoritos(
	correo VARCHAR(20),
	ID INT
);
ALTER TABLE Favoritos ADD CONSTRAINT favoritos_pk
PRIMARY KEY (correo, ID);
ALTER TABLE Favoritos ADD CONSTRAINT contenido_fk_id
FOREIGN KEY (ID) REFERENCES Contenido (ID);
ALTER TABLE Favoritos ADD CONSTRAINT usuario_fk_correo
FOREIGN KEY (correo) REFERENCES Usuario (correo);

CREATE TABLE AlmacenaPlaylist(
	IDP INT,
	IDCA INT
);
ALTER TABLE AlmacenaPlaylist ADD CONSTRAINT ap_pk
PRIMARY KEY (IDP, IDCA);
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
	correo VARCHAR(20),
	nombreRed VARCHAR(10),
	username VARCHAR(10)
);
ALTER TABLE TieneRedes ADD CONSTRAINT tr_pk
PRIMARY KEY (correo, nombreRed);
ALTER TABLE TieneRedes ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE TieneRedes ADD CONSTRAINT red_fk_nombre
FOREIGN KEY (nombreRed) REFERENCES RedSocial (nombre);

CREATE TABLE TieneEventos(
	correo VARCHAR(20),
	ID INT
);
ALTER TABLE TieneEventos ADD CONSTRAINT te_pk
PRIMARY KEY (correo, ID);
ALTER TABLE TieneEventos ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE TieneEventos ADD CONSTRAINT evento_fk_id
FOREIGN KEY (ID) REFERENCES Evento (ID);

CREATE TABLE AlmacenaAlbum(
	IDC INT,
	IDA INT
);
ALTER TABLE AlmacenaAlbum ADD CONSTRAINT aa_pk
PRIMARY KEY (IDC, IDA);
ALTER TABLE AlmacenaAlbum ADD CONSTRAINT cancion_fk_id
FOREIGN KEY (IDC) REFERENCES Cancion (ID);
ALTER TABLE AlmacenaAlbum ADD CONSTRAINT album_fk_id
FOREIGN KEY (IDA) REFERENCES Album (ID);

CREATE TABLE CreaAlbum(
	correo VARCHAR(20),
	IDA INT
);
ALTER TABLE CreaAlbum ADD CONSTRAINT ca_pk
PRIMARY KEY (correo, IDA);
ALTER TABLE CreaAlbum ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE CreaAlbum ADD CONSTRAINT album_fk_id
FOREIGN KEY (IDA) REFERENCES Album (ID);

CREATE TABLE CreaCancion(
	correo VARCHAR(20),
	IDC INT
);
ALTER TABLE CreaCancion ADD CONSTRAINT cc_pk
PRIMARY KEY (correo, IDC);
ALTER TABLE CreaCancion ADD CONSTRAINT am_fk_correo
FOREIGN KEY (correo) REFERENCES ArtistaMusical (correo);
ALTER TABLE CreaCancion ADD CONSTRAINT cancion_fk_id
FOREIGN KEY (IDC) REFERENCES cancion (ID);

ALTER TABLE Usuario ALTER COLUMN correo SET NOT NULL;
ALTER TABLE Playlist ALTER COLUMN ID SET NOT NULL;
ALTER TABLE Contenido ALTER COLUMN ID SET NOT NULL;
ALTER TABLE ArtistaMusical ALTER COLUMN correo SET NOT NULL;
ALTER TABLE RedSocial ALTER COLUMN nombre SET NOT NULL;
ALTER TABLE Evento ALTER COLUMN ID SET NOT NULL;
ALTER TABLE ArtistaPodcast ALTER COLUMN correo SET NOT NULL;
ALTER TABLE ContenidoAcumulable ALTER COLUMN ID SET NOT NULL;
ALTER TABLE Podcast ALTER COLUMN ID SET NOT NULL;
ALTER TABLE Album ALTER COLUMN ID SET NOT NULL;
ALTER TABLE Episodio ALTER COLUMN ID SET NOT NULL;
ALTER TABLE Cancion ALTER COLUMN ID SET NOT NULL;
ALTER TABLE Favoritos ALTER COLUMN ID SET NOT NULL;
ALTER TABLE TieneEventos ALTER COLUMN ID SET NOT NULL;
ALTER TABLE TieneEventos ALTER COLUMN correo SET NOT NULL;
ALTER TABLE TieneRedes ALTER COLUMN nombreRed SET NOT NULL;
ALTER TABLE AlmacenaPlaylist ALTER COLUMN IDP SET NOT NULL;
ALTER TABLE AlmacenaPlaylist ALTER COLUMN IDCA SET NOT NULL;
ALTER TABLE Participa ALTER COLUMN correo SET NOT NULL;
ALTER TABLE Participa ALTER COLUMN IDP SET NOT NULL;
ALTER TABLE TieneRedes ALTER COLUMN correo SET NOT NULL;
ALTER TABLE TieneEventos ALTER COLUMN correo SET NOT NULL;
ALTER TABLE AlmacenaAlbum ALTER COLUMN IDC SET NOT NULL;
ALTER TABLE AlmacenaAlbum ALTER COLUMN IDA SET NOT NULL;
ALTER TABLE CreaAlbum ALTER COLUMN correo SET NOT NULL;
ALTER TABLE CreaAlbum ALTER COLUMN IDA SET NOT NULL;
ALTER TABLE CreaCancion ALTER COLUMN correo SET NOT NULL;
ALTER TABLE CreaCancion ALTER COLUMN IDC SET NOT NULL;

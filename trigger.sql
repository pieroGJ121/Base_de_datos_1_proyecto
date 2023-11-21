-- Deletes the inserted object if it the date of the cancion is after the album
CREATE OR REPLACE FUNCTION ActualizarAlmacenaAlbum() RETURNS TRIGGER AS
$$
BEGIN
IF ((SELECT fechaLanzamiento FROM Contenido WHERE ID = NEW.IDC) >=
(SELECT fechaLanzamiento FROM Contenido WHERE ID = NEW.IDA))
THEN
DELETE FROM AlmacenaAlbum A WHERE A.IDC = NEW.IDC AND A.IDA = NEW.IDA;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarAlmacenarAlbum
 AFTER INSERT ON AlmacenaAlbum
FOR EACH ROW EXECUTE FUNCTION ActualizarAlmacenaAlbum();

-- Deletes the inserted object if the date of creation of the event is before the ArtistaMusical was created
CREATE OR REPLACE FUNCTION ActualizarTieneEventos() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fecha FROM Evento WHERE ID = NEW.ID) <
(SELECT fecha_creacion FROM Usuario WHERE correo = NEW.correo))
THEN
DELETE FROM TieneEventos WHERE ID = NEW.ID;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarTieneEventos
 AFTER INSERT ON TieneEventos
FOR EACH ROW EXECUTE FUNCTION ActualizarTieneEventos();

-- Deletes the inserted object if the date of creation of the song is after the album
CREATE OR REPLACE FUNCTION ActualizarAlmacenaAlbumC() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fechaLanzamiento FROM Contenido WHERE ID = NEW.IDC) >
(SELECT fechaLanzamiento FROM Contenido WHERE ID = NEW.IDA))
THEN
DELETE FROM AlmacenaAlbum WHERE IDC = NEW.IDC AND IDA = NEW.IDA;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarAlmacenaAlbum
 AFTER INSERT ON AlmacenaAlbum
FOR EACH ROW EXECUTE FUNCTION ActualizarAlmacenaAlbumC();

-- Deletes the inserted object if the date of creation of the episodio is before the Podcast
CREATE OR REPLACE FUNCTION ActualizarEpisodio() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fechaLanzamiento FROM Contenido WHERE ID = NEW.ID) <
(SELECT fecha_creacion FROM ArtistaPodcast WHERE ID = NEW.IDP))
THEN
DELETE FROM Episodio WHERE ID = NEW.ID;
DELETE FROM ContenidoAcumulable WHERE ID = NEW.ID;
DELETE FROM Contenido WHERE ID = NEW.ID;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarEpisodio
 AFTER INSERT ON Episodio
FOR EACH ROW EXECUTE FUNCTION ActualizarEpisodio();

-- Deletes the inserted object if the date of creation of the playlist is before the user
CREATE OR REPLACE FUNCTION ActualizarPlaylist() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fecha_creeacion FROM Playlist WHERE ID=NEW.ID) <
(SELECT fecha_creacion FROM Usuario WHERE correo=NEW.correo))
THEN
DELETE FROM Playlist WHERE ID=NEW.ID;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarPlaylist
 AFTER INSERT ON Playlist
FOR EACH ROW EXECUTE FUNCTION ActualizarPlaylist();

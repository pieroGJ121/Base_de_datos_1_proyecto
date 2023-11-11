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

-- Deletes the inserted object if the date of creation of the event is after the ArtistaMusical
CREATE OR REPLACE FUNCTION ActualizarTieneEventos() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fecha FROM Evento WHERE ID=NEW.ID) <
(SELECT fecha_creacion FROM ArtistaMusical A JOIN Usuario U ON A.correo = U.correo WHERE A.correo=NEW.correo))
THEN
DELETE FROM TieneEventos E WHERE E.ID=NEW.ID;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarTieneEventos
 AFTER INSERT ON TieneEventos
FOR EACH ROW EXECUTE FUNCTION ActualizarTieneEventos();

-- Deletes the inserted object if the date of creation of the song is after the ArtistaMusical
CREATE OR REPLACE FUNCTION ActualizarAlmacenaAlbumC() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fechaLanzamiento FROM Contenido WHERE ID=NEW.ID) <
(SELECT fecha_creacion FROM ArtistaMusical A JOIN Usuario U ON A.correo = U.correo WHERE A.correo=NEW.correo))
THEN
DELETE FROM AlmacenaAlbum A WHERE A.IDC=NEW.ID;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarAlmacenaAlbum
 AFTER INSERT ON AlmacenaAlbum
FOR EACH ROW EXECUTE FUNCTION ActualizarAlmacenaAlbumC();

-- Deletes the inserted object if the date of creation of the episodio is after the ArtistaMusical
CREATE OR REPLACE FUNCTION ActualizarCreaEpisodio() RETURNS TRIGGER AS
$$
BEGIN
IF((SELECT fechaLanzamiento FROM Contenido WHERE ID=NEW.ID) <
(SELECT fecha_creacion FROM ArtistaMusical A JOIN Usuario U ON A.correo = U.correo WHERE A.correo=NEW.correo))
THEN
DELETE FROM CreaEpisodio CE WHERE CE.ide=NEW.ID;
END IF;
RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER trigger_actualizarCreaEpisodio
 AFTER INSERT ON CreaEpisodio
FOR EACH ROW EXECUTE FUNCTION ActualizarCreaEpisodio();

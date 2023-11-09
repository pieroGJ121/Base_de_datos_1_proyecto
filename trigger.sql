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

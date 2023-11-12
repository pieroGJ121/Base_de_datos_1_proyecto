-- Guiate del proyecto epic games store. Me parece el más completo
-- Para sin indice. Ejecutalo antes de correr. Creo que se debe hacer en cada schema
SET enable_mergejoin to OFF;
SET enable_hashjoin to OFF;
SET enable_bitmapscan to OFF;
SET enable_sort to OFF;

-- Tienes que activar esto despues de cada ejecucion del querry con las tablas usadas
-- P1
VACUUM FULL Evento;
VACUUM FULL TieneEventos;
VACUUM FULL CreaAlbum;
VACUUM FULL Contenido;
VACUUM FULL AlmacenaAlbum;
VACUUM FULL TieneRedes;
-- P2
VACUUM FULL CreaCancion;
VACUUM FULL Episodio;
VACUUM FULL Podcast;
VACUUM FULL Participa;
VACUUM FULL Favoritos;
VACUUM FULL Usuario;
-- P3
VACUUM FULL Participa;
VACUUM FULL Usuario;
VACUUM FULL Favoritos;
VACUUM FULL Episodio;
VACUUM FULL Podcast;
VACUUM FULL ContenidoAcumulable;

-- Con indice
-- Se activan de vuelta. Creo que se debe hacer en cada schema
SET enable_mergejoin to OFF;
SET enable_hashjoin to OFF;
SET enable_bitmapscan to OFF;
SET enable_sort to OFF;
-- P1
CREATE INDEX index_evento on Evento USING hash(lugar)
-- P2
CREATE INDEX index_evento on Usuario USING hash(tipo_suscripcion)
-- P3
CREATE INDEX index_evento on Podcast USING btree(fecha)
CREATE INDEX index_evento on ContenidoAcumulable USING btree(duracion)

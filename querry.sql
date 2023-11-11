-- P1
SELECT DISTINCT Evento.Id, Evento.nombre
FROM Evento NATURAL JOIN tieneEventos
Natural JOIN CreaAlbum JOIN Contenido ON CreaAlbum.ida = Contenido.id
WHERE (lugar = 'Miami'
OR lugar = 'California' OR lugar = 'Las Vegas' OR lugar = 'Chicago') AND
ABS(fecha - fechaLanzamiento) <= 180 AND IDA IN
(SELECT IDA FROM AlmacenaAlbum GROUP BY IDA HAVING COUNT(*) >= 5)
AND correo IN
(SELECT correo FROM TieneRedes GROUP BY correo HAVING COUNT(*) >= 4);
-- P2
-- P3
SELECT DISTINCT correo, username FROM Participa NATURAL JOIN Usuario WHERE IDP IN (SELECT IDP FROM
(SELECT ID, COUNT(*) as cantidad FROM
(SELECT ID, correo FROM Favoritos WHERE ID IN
(SELECT ID FROM Episodio WHERE IDP IN
(SELECT ID FROM Podcast WHERE fecha BETWEEN '2020-01-01' AND '2023-12-30')
AND ID IN (SELECT ID FROM ContenidoAcumulable WHERE  duracion > '01:00:00'))) A GROUP BY ID
ORDER BY COUNT(*) DESC LIMIT 10) E NATURAL JOIN Episodio);

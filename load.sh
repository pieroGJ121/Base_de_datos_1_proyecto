#!/usr/bin/env sh

for table in usuario artistamusical artistapodcast podcast participa contenido contenidoacumulable episodio cancion album almacenaalbum creaalbum creacancion favoritos playlist almacenaplaylist redsocial tieneredes evento tieneeventos; do
    for schema in mil diezmil cienmil millon; do
        psql -U postgres -d bd1_proyecto -a -f "scripts/${schema}_${table}.sql"
    done
done

for table in favoritos participa; do
    for schema in mil diezmil cienmil millon; do
        psql -U postgres -d bd1_proyecto -a -f "scripts/${schema}_${table}.sql"
    done
done

# Deletion of files
# for script in cancion episodio contenido contenidoacumulable album almacenaalbum creaalbum creacancion favoritos; do
# for script in podcast participa; do
#     for table in mil diezmil cienmil millon; do
#         rm "scripts/${table}_${script}.sql"
#     done
# done

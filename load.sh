#!/usr/bin/env sh

for table in podcast; do
    psql -U postgres -d bd1_proyecto -a -f "scripts/mil_$table.sql"
    psql -U postgres -d bd1_proyecto -a -f "scripts/diezmil_$table.sql"
    psql -U postgres -d bd1_proyecto -a -f "scripts/cienmil_$table.sql"
    psql -U postgres -d bd1_proyecto -a -f "scripts/millon_$table.sql"
done

$1bin/cqlsh $4 9042 -f $3

python loaddata.py $2 $4 $5

$1bin/cqlsh -f $3

sudo $1bin/dsetool create_core $5 solrconfig=./setup/solrconfig.xml schema=./setup/schema.xml

python loaddata.py $2 $4 $5

##Intro
This project allows you to supply a cql file, a json file, and a cassandra host and then creates the data model and loads up the JSON (as long as the data model represents all possible JSON fields). Note that this assumes the file provided has a new JSON object on each line, and assumes no nesting. Edit loaddata.py to change the parsing logic.

##Running the project
To run the whole simulation, configure your schema.xml file to the appropriate schema and run:

```
./loadandindex.sh <pathtodseinstall> <json datafile path> <datamodelfile path> <cassandra host ip> <keyspace.table>
```

For example, to run the example in this folder (make sure to add the '/' at the end for the dse install path):

```
./loadandindex.sh ~/dse-4.8.0/ ./setup/data.txt ./setup/datamodel.cql 127.0.0.1 metrics.raw_metrics
```

##Running data load only
The command is the same as above, but use the load.sh script to avoid indexing.
```
./load.sh ~/dse-4.8.0/ ./setup/data.txt ./setup/datamodel.cql 127.0.0.1 metrics.raw_metrics
```

##Indexing after loading
If you decide to index your data after you load it, run:
```
./index.sh <dse install path> <keyspace.table>
```
For example
```
./index.sh ~/dse-4.8.0/ metrics.raw_metrics
```
Remember to edit your schema.xml file before starting indexing.

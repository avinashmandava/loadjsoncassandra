from cassandra.cluster import Cluster
import logging
import time
import datetime
import json
import sys

log = logging.getLogger()
log.setLevel('INFO')

def getvals(items):
    return ', '.join(str(item) for item in items)

def getinsert(keys,values):
    return "INSERT INTO ciscometrics.raw_metrics ("+getvals(keys)+") VALUES ("+getvals(values)+");"

def create_insert(row):
    keys = ['pod']
    values = ["'"+'1'+"'"]
    for key in row.keys():
        keys.append(key)
        if key == 'interval':
            values.append(int(row[key]))
        elif key == 'tx':
            values.append(int(row[key]))
        elif key == 'rx':
            values.append(int(row[key]))
        elif key == 'value':
            values.append(float(row[key]))
        else:
            values.append("'"+str(row[key])+"'")
    return getinsert(keys,values)


class Config(object):
    cassandra_hosts = sys.argv[2]

class SimpleClient(object):

    #Instantiate a session object to be used to connect to the database.
    session = None

    #Method to connect to the cluster and print connection info to the console
    def connect(self, nodes):
        cluster = Cluster(nodes)
        metadata = cluster.metadata
        self.session = cluster.connect()
        log.info('Connected to cluster: ' + metadata.cluster_name)
        for host in metadata.all_hosts():
            log.info('Datacenter: %s; Host: %s; Rack: %s',
                host.datacenter, host.address, host.rack)

    #Close the connection
    def close(self):
        self.session.cluster.shutdown()
        log.info('Connection closed.')

    def load_data(self,datapath):
        datafile = open(datapath)
        for line in datafile:
            self.session.execute(create_insert(json.loads(line)))



def main():
    logging.basicConfig()
    client = SimpleClient()
    client.connect([Config.cassandra_hosts])
    time.sleep(1)
    client.load_data(sys.argv[1])
    client.close()

if __name__ == "__main__":
    main()

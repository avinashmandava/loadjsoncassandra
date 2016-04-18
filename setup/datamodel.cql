CREATE KEYSPACE metrics WITH replication = {'class':'SimpleStrategy', 'replication_factor':1};

CREATE TABLE metrics.raw_metrics (
  pod text,
  type_instance text,
  plugin_instance text,
  plugin text,
  host text,
  interval int,
  time timestamp,
  type text,
  value float,
  read text,
  tx bigint,
  rx bigint,
  write text,
  gauge text,
  derive text,
  PRIMARY KEY((pod,host),time)
);

# Twitter_Streaming_kafka

Kafka is the tool most people use to read streaming 
data like this.  It follows a publish-subscribe model 
where you write messages (publish) and read t
hem (subscribe).  Messages are grouped into topics. 
As messages are consumed, they are removed from Kafka.

## Prerequisites

- Zookeeper
- Kafka
- Tweepy
- Twitter Api Credentials

## Steps

- Create an app in twitter website to get the credentials.
- Install Zookeeper and kafka from apache.org
- Start Zookeeper
```
bin/zookeeper-server-start.sh config/zookeeper.properties

Using config: /home/nineleaps/zookeeper-3.4.14/bin/../conf/zoo.cfg
Starting zookeeper ... STARTED
```
- Start Kafka
```
bin/kafka-server-start.sh config/server.properties

[2020-06-18 13:03:21,767] INFO Registered kafka:type=kafka.Log4jController MBean (kafka.utils.Log4jControllerRegistration$)
...
```
- Create topic
```
 bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test```

Created topic test.
```
- Check topics
```
bin/kafka-topics.sh --list --bootstrap-server localhost:9092
```
## Run

Run kafka_listener.py

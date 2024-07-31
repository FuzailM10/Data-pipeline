from confluent_kafka import Producer

def produce_messages(topic, data):
    conf = {'bootstrap.servers': 'localhost:9092'}
    producer = Producer(conf)
    producer.produce(topic, value=data)
    producer.flush()

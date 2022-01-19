import grpc
import event_coord_pb2
import event_coord_pb2_grpc
from concurrent import futures

import logging
import os
import json

from kafka import KafkaProducer
kafka_url = 'udaconnect-kafka-0.udaconnect-kafka-headless.default.svc.cluster.local:9092'
kafka_topic = 'test'

logging.info('connecting to kafka ', kafka_url)
logging.info('connecting to kafka topic ', kafka_topic)

producer = KafkaProducer(bootstrap_servers=kafka_url)
class EventCoordinateServicer(event_coord_pb2_grpc.ItemServiceServicer):
    def Create(self,request,context):
        request_value = {
            "userId": int(request.userId),
            "latitude": int(request.latitude),
            "longitude": int(request.longitude)

        }
        encoded_data = json.dumps(request_value).encode('utf-8')
        producer.send(kafka_topic,encoded_data)
        producer.flush()
        return event_coord_pb2.EventCoordinatesMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
event_coord_pb2_grpc.add_ItemServiceServicer_to_server(EventCoordinateServicer(), server)
logging.info('starting on port 5005')
server.add_insecure_port('[::]:5005')
server.start()
server.wait_for_termination()
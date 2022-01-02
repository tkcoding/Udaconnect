import grpc
import event_coord_pb2
import event_coord_pb2_grpc
from concurrent import futures
import logging
import os

kafka_url = os.environ['KAFKA_URL']
kafka_topic = os.environ['KAFKA_TOPIC']


class EventCoordinateServicer(event_coord_pb2_grpc.ItemServiceServicer):
    def Create(self,request,context):
        request_value = {
            "userId": int(request.userId),
            "latitude": int(request.latitude),
            "longitude": int(request.longitude)

        }
        encoded_data = json.dumps(request_value).encode('utf-8')
        producer.send(kafka_topic,encoded_data)
        return event_coord_pb2.EventCoordinatesMessage(**request_value)


server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
event_coord_pb2_grpc.add_ItemServiceServicer_to_server(EventCoordinateServicer(), server)
print('starting on port 5005')
server.add_insecure_port('[::]:5005')
server.start()
server.wait_for_termination()
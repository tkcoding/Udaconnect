import grpc

import event_coord_pb2
import event_coord_pb2_grpc

"""
Sample of user sending coordinates to gRPC
"""

print("Coordinates sending...")

channel = grpc.insecure_channel("127.0.0.1:30003")
# channel = grpc.insecure_channel("localhost:5005")
stub = event_coord_pb2_grpc.ItemServiceStub(channel)

# Update this with desired payload
# user_coordinates = event_coord_pb2.EventCoordinatesMessage(
#     userId=300,
#     latitude=-100,
#     longitude=30
# )

# user_coordinates_2 = event_coord_pb2.EventCoordinatesMessage(
#     userId=400,
#     latitude=-100,
#     longitude=30
# )

user_coordinates_3 = event_coord_pb2.EventCoordinatesMessage(
    userId=2,
    latitude=-100,
    longitude=30
)


user_coordinates_4 = event_coord_pb2.EventCoordinatesMessage(
    userId=3,
    latitude=-100,
    longitude=30
)

# response_1 = stub.Create(user_coordinates)
# response_2 = stub.Create(user_coordinates_2)
response_3 = stub.Create(user_coordinates_3)
response_4 = stub.Create(user_coordinates_4)
print("Coordinates sent...")
print(response_3,response_4)
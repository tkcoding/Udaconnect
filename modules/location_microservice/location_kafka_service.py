import json
import os
import psycopg2

from kafka import KafkaConsumer

TOPIC_NAME = "test"
print('started listening ' + TOPIC_NAME)

DB_USERNAME =  "ct_geoconnections"
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]

KAFKA_URL = "udaconnect-kafka.default.svc.cluster.local"

consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=[KAFKA_URL])


def save_in_db(location):
    db_conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    db_cursor = db_conn.cursor()
    person_id = int(location["userId"])
    latitude, longitude = float(location["latitude"]), float(location["longitude"])
   
    sql = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))".format(person_id, latitude, longitude)
    db_cursor.execute(sql)
    db_conn.commit()
    db_cursor.close()
    db_conn.close()

while True:
    for location in consumer:
        message = location.value.decode('utf-8')
        location_message = json.loads(message)
        save_in_db(location_message)
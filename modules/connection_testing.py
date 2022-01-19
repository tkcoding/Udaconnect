import psycopg2

DB_USERNAME = "ct_geoconnections"
DB_NAME= "geoconnections"
DB_HOST = "postgres-geoconnections"
DB_PORT = "5432"
DB_PASSWORD = "d293aW1zb3NlY3VyZQ=="

# engine = create_engine(f"postgresql://localhost:5432/geoconnections", echo=True)
# conn = engine.connect()
db_conn = psycopg2.connect("postgresql://localhost:5432/geoconnections")
# person_id = int(location["userId"])
# latitude, longitude = int(location["latitude"]), int(location["longitude"])
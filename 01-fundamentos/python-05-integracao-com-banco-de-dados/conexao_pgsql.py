import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="fliperama",
    user="postgres",
    password="1q2w3e4r",
    port="5432"
)
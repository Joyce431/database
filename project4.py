import psycopg2

# Replace these with your actual database credentials
connection = psycopg2.connect(
    host="localhost",
    port="5432",
    database="shop",
    user="postgres",
    password="moabi1608"
)

# 3. Select and display data from 'users' table
cursor = connection.cursor()
cursor.execute("SELECT * FROM product;")
dataset= cursor.fetchall()
print("shop table data:")
for data in dataset:
    print(data)

# Cleanup
cursor.close()
connection.close()
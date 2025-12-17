import pymysql

# Step 1: Connect to the Database

connection=pymysql.Connect(
    host='localhost',
    user='root',
    password='root',
    database='world',        # Mysql database is in your mysql database
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor() as cursor:

        # Step 2: Create a table
        create_query="""
        CREATE TABLE IF NOT EXISTS employees(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        )
        """
        cursor.execute(create_query)

        # Step 3: Insert Table

        insert_query="INSERT INTO employees (name,department) VALUES(%s, %s)"
        values=[("John","IT"),("Alice","HR"),("Sanoop","CEO")]
        cursor.executemany(insert_query, values)
        connection.commit()

        # Step 4: Select Data

        select_query="  SELECT * FROM employees"
        cursor.execute(select_query)
        result=cursor.fetchall()

    with open("output_database.txt","w") as f:
        for row in result:
            f.write(f"{row}\n")

finally:
    connection.close()
        


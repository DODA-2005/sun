import mysql.connector

def fetch_records():
    try:
        # Replace these with your actual database credentials
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="your_database"
        )

        # Replace 'field1, field2, ...' with the actual fields you want to fetch
        fields_to_fetch = 'field1, field2, field3'
        
        query = f"SELECT {fields_to_fetch} FROM your_table"

        cursor = db_connection.cursor(dictionary=True)
        cursor.execute(query)

        # Fetch all records
        records = cursor.fetchall()

        # Display the fetched records
        for record in records:
            print(record)

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

# Call the function to fetch records
fetch_records()

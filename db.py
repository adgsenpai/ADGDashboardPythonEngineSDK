import pyodbc

# Update these values with your database details
connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=<ip>,<port>;"
    "DATABASE=<dbname>;"
    "UID=<username>;"
    "PWD=<password>;"
    "TrustServerCertificate=yes;"
)

def get_connection():
    """Establish and return a database connection."""
    try:
        conn = pyodbc.connect(connection_string)
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
        return None

def execute_query(query):
    """
    Executes a query that doesn't return a result (e.g., INSERT, UPDATE, DELETE).
    
    Parameters:
      query (str): The SQL query to execute.
    """
    conn = get_connection()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("Query executed successfully.")
    except Exception as e:
        print("Error executing query:", e)
    finally:
        cursor.close()
        conn.close()

def get_records_as_column(query, column_name):
    """
    Executes a query and returns a list of values for the specified column.
    
    Parameters:
      query (str): The SQL query to execute.
      column_name (str): The column name whose values will be returned.
    
    Returns:
      list: A list of values from the specified column.
    """
    conn = get_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        # Retrieve column names from cursor description
        columns = [desc[0] for desc in cursor.description]
        if column_name not in columns:
            print(f"Column '{column_name}' not found in the query results.")
            return []
        col_index = columns.index(column_name)
        records = [row[col_index] for row in cursor.fetchall()]
        return records
    except Exception as e:
        print("Error fetching records as column:", e)
        return []
    finally:
        cursor.close()
        conn.close()

def get_records_as_dict(query):
    """
    Executes a query and returns the result as a list of dictionaries.
    
    Parameters:
      query (str): The SQL query to execute.
    
    Returns:
      list: A list where each element is a dictionary representing a row.
    """
    conn = get_connection()
    if conn is None:
        return []
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        # Get the column names
        columns = [desc[0] for desc in cursor.description]
        results = []
        for row in cursor.fetchall():
            row_dict = dict(zip(columns, row))
            results.append(row_dict)
        return results
    except Exception as e:
        print("Error fetching records as dict:", e)
        return []
    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    # Example usage:

    # Define a sample query (update table name as needed)
    sample_query = "SELECT * FROM [User]"

    # Fetch records as a list of dictionaries
    records_dict = get_records_as_dict(sample_query)
    print("Records as dict:")
    for record in records_dict:
        print(record)

    # Fetch a specific column (e.g., 'email') as a list
    column_records = get_records_as_column(sample_query, 'email')
    print("\nEmail column records:")
    print(column_records)

    # Execute an update query (adjust the query as per your table structure)
    update_query = "UPDATE [User] SET country = 'Canada' WHERE id = 1"
    execute_query(update_query)

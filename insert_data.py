from db_connection import connect_db

connection = connect_db()

if connection:
    cur = connection.cursor()
    
    # Insert data into the inventary table.
    cur.execute("INSERT INTO sales (product_name, quantity_sold) VALUES (?, ?)", ("Tablet LG", 5))
    connection.commit() # Save changes.

    # Querying data from inventary table.
    cur.execute("SELECT * FROM inventory")
    products = cur.fetchall()
    cur.execute("SELECT * FROM sales")
    sales = cur.fetchone()

    print(products)
    print(sales)

    # Close connection
    cur.close()
    connection.close

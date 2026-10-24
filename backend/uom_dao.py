def get_uom(connection ):
    cursor = connection.cursor()

    query = ("SELECT * FROM uom;") 

    cursor.execute(query) # they cursor.execute() method is used to execute the query and fetch the data from the database

    response = []

    for(uom_id, uom_name) in cursor: # the for loop use append method to add the data to the response list and return the response list
        response.append({
            "uom_id": uom_id,
            "uom_name": uom_name
        })

    
    return response

if __name__ == "__main__":    # if and main method is used to test the function and check if the connection to the database is successful or not
    from sql_connection import get_sql_connection

    connection = get_sql_connection()        #they delete product
    print(get_uom(connection))
#   print(get_all_products(connection))
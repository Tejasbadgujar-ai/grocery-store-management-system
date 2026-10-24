import mysql.connector
from sql_connection import get_sql_connection  #connect the sql_connection.py file to this file to get the connection to the database

def get_all_products(connection): # these fuction works to get all the products from the product table and returns a list of products
    cursor = connection.cursor()

    query = ("SELECT product.product_id, product.name, product.uom_id, product.price_per_unit,"
     "uom.uom_name FROM product INNER JOIN uom ON uom.uom_id = product.uom_id;") 

    cursor.execute(query) # they cursor.execute() method is used to execute the query and fetch the data from the database

    response = []

    for(product_id, name, uom_id, price_per_unit, uom_name) in cursor: # the for loop use append method to add the data to the response list and return the response list
        response.append({
            "product_id": product_id,
            "name": name,
            "uom_id": uom_id,
            "price_per_unit": price_per_unit,
            "uom_name": uom_name
        })

    print("GS Connected")
    return response

#that fuction insert new product into the product table and returns the last inserted id of the product
def insert_new_product(connection, product):
    cursor = connection.cursor()
    
    query = ("insert into product(name, uom_id, price_per_unit) values (%s, %s, %s);") #//parameterzed query using %s to prevent SQL injection
    data = (product["name"], product["uom_id"], product["price_per_unit"])
    cursor.execute(query, data)
    connection.commit()  # commit() method is used to save the changes made to the database
    return cursor.lastrowid
    

def delete_product(connection, product_id): # this function delete the product from the product table based on the product_id and returns the number of rows affected
    cursor = connection.cursor()
    
    query = ("delete from product where product_id =" + str(product_id)) 
    data = (product_id,)
    cursor.execute(query)
    connection.commit()  
    
    return cursor.lastrowid  


if __name__ == "__main__":    # if and main method is used to test the function and check if the connection to the database is successful or not
    connection = get_sql_connection()        #they delete product
    print(delete_product(connection, 14)) 
   
   
   # print(insert_new_product(connection,{   #they add produt
    #}))                      


#final all over to add new product and dictionary to the product table and return the last inserted id of the product
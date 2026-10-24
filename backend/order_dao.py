from sql_connection import get_sql_connection
from datetime import datetime

def insert_order(connection, order):
    cursor = connection.cursor()

    #insert order into orders table
    order_query = ("insert into orders "
                   "(customers_name, total, datetime)"
                   "VALUES (%s, %s, %s)")
    
    order_data =(order['customers_name'], order['total'], datetime.now())
    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid
    #connection.commit()
    #return order_id

    order_detail_query = """insert into order_detail 
                   (order_id, product_id, quantity, total_price)
                    VALUES (%s, %s, %s, %s)"""


    # insert order derails into order_details table
    order_detail_data = []
    for order_detail_record in order['order_detail']:
        order_detail_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            order_detail_record['total_price']
        ]) 

    cursor.executemany(order_detail_query, order_detail_data)
    
    connection.commit()
    return order_id


def get_all_orders(connection):
    cursor = connection.cursor()

if __name__ == "__main__":
    connection = get_sql_connection()  
    print (get_all_orders(connection))
    print(insert_order(connection, {
        'customers_name': 'basic',
        'total': '100',
        'order_detail': [
            {
                'product_id': 1,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 3,
                'quantity': 1,
                'total_price': 30
            }
        ]
        
    }))
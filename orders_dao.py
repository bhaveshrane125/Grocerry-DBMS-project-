from sql_conector import get_sql_connection
from datetime import datetime
from customer_dao import create_customer,check_customer,get_total,increment_total




def create_order( data ):
    con = get_sql_connection()

    mycursor = con.cursor()

    customer_data ={
        'customer_phone':data['customer_phone'],
        'customer_name':data['customer_name']
    }

    if not check_customer(customer_data):
        create_customer(customer_data)


    query = ("INSERT INTO orders "
             "(customer_phone, total, datetime)"
             "VALUES (%s, %s, %s)")
    order_data = (data['customer_phone'], data['grand_total'], datetime.now())


    mycursor.execute(query,order_data)
    order_id = mycursor.lastrowid

    cost_increment_data = {
        'customer_phone':data['customer_phone'],
        'grand_total':float(data['grand_total'])+(get_total(data))
    }
    increment_total(cost_increment_data)


    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")
    order_details_data = []
    for order_detail_record in data['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    print(order_details_data)
    mycursor.executemany(order_details_query, order_details_data)



    con.commit()


    return order_id




def get_order_details():
    con = get_sql_connection()
    query = "select orders.order_id,customer.phone_no,customer.customer_name,orders.datetime as all_details,order_details.product_id,products.product_name,orders.total from orders join customer on customer.phone_no = orders.customer_phone join order_details on order_details.order_id = orders.order_id join products on order_details.product_id = products.product_id;"
    mycursor = con.cursor()
    mycursor.execute(query)

    orders_data = dict()

    for (order_id, phone_no, customer_name, date, product_id, product_name,total) in mycursor:
        if order_id not in orders_data.keys():
            orders_data[order_id] = {'order_id':order_id,'customer_name':customer_name, 'phone_no':phone_no,'date':date,'products':[product_name],'total':total}
        else:
            orders_data[order_id]['products'].append(product_name)

    data = []
    for i in orders_data:
        data.append(orders_data[i])
    return sorted(data, key = lambda i:i['date'],reverse=True)




if __name__ == '__main__':
    data = {
        'customer_phone':9637946438,
        'customer_name':"Bhavesh Rane",
        "grand_total":"1000",
        'order_details':[{'product_id': '3', 'quantity': '1', 'total_price': '35.00'},
                        {'product_id': '2', 'quantity': '1', 'total_price': '15.00'}]
    }
    xxx = get_order_details()
    for i in xxx:
        print(i)


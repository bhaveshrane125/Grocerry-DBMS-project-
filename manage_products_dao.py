from sql_conector import get_sql_connection


def get_products(con):

    mycursor = con.cursor()

    data = []
    query = "SELECT products.product_id, products.product_name, products.unit_id, products.price, unit_table.unit_name " \
            "FROM products INNER JOIN unit_table on products.unit_id=unit_table.unit_id;"

    mycursor.execute(query)

    for (product_id, product_name, unit_id, product_price, unit_name) in mycursor:
        data.append(
            {
                "product_id": product_id,
                "product_name": product_name,
                "unit_id": unit_id,
                "price": product_price,
                "unit_name": unit_name
            }
        )

    return data


def insert_new_product(con, product):
    mycursor = con.cursor()
    query = ("INSERT INTO products "
             "(product_name, unit_id, price)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price'])
    mycursor.execute(query, data)

    con.commit()
    return mycursor.lastrowid



def delete_product(con, product_id):
    mycursor = con.cursor()
    query = (f"DELETE FROM products WHERE product_id={product_id}")
    mycursor.execute(query)
    con.commit()

    return mycursor.lastrowid



if __name__ == '__main__':
    con = get_sql_connection()
    print(insert_new_product(con, {
        'product_name': 'potatoes',
        'unit_id': '1',
        'price': 10
    }))
    print(get_products(con))

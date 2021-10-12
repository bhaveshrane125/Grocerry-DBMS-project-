from sql_conector import get_sql_connection



def create_customer( data ):
    con =  get_sql_connection()
    query = ("INSERT INTO customer "
             "(phone_no, customer_name)"
             "VALUES (%s, %s)")
    mycursor = con.cursor()
    data = (data['customer_phone'], data['customer_name'])
    mycursor.execute(query,data)
    con.commit()

    return mycursor.lastrowid


def increment_total(data):
    con = get_sql_connection()
    query = ("UPDATE customer "
             f"SET total_cost = {data['grand_total']} "
             f"WHERE customer.phone_no = {data['customer_phone']}")
    print(query)
    mycursor = con.cursor()
    mycursor.execute(query)
    con.commit()
    return mycursor.lastrowid



def get_total(data):
    con = get_sql_connection()
    query = f"select total_cost from customer where customer.phone_no = {data['customer_phone']};"
    mycursor = con.cursor()
    mycursor.execute(query)
    total_cost=[]

    for i in mycursor:
        total_cost.append(i[0])

    if total_cost[0]!=None:
        return total_cost[0]
    return 0



def check_customer(data):
    con = get_sql_connection()
    query = f"select * from customer where customer.phone_no = {data['customer_phone']};"
    mycursor = con.cursor()

    mycursor.execute(query)
    ans = []
    for (customer_phone,customer_name,total) in mycursor:
        ans.append(
            {
                'customer_phone': customer_phone,
                'customer_name' : customer_name,

            }
        )

    if len(ans)==0:
        return False

    return True



def get_customer():
    con = get_sql_connection()
    query = f"select * from customer;"
    mycursor = con.cursor()

    mycursor.execute(query)
    ans = []
    for (customer_phone, customer_name, total) in mycursor:
        ans.append(
            {
                'customer_phone': customer_phone,
                'customer_name': customer_name,
                'total':total
            }
        )
    return ans

if __name__ == '__main__':
    data = {
        "phone_no":9401231232,
        "customer_name":"Parth Joshi",

        "total_cost":5000,
    }
    data2 = {
        "customer_phone":9860797991
    }

    print(get_total(data2))

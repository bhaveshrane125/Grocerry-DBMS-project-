from sql_conector import get_sql_connection
from customer_dao import create_customer
def get_units(con):
    mycursor=con.cursor()
    query = "select * from unit_table;"
    units_data = []
    mycursor.execute(query)

    for (u_id, unit_name) in mycursor:
        units_data.append(
            {
                "u_id":u_id,
                "unit_name":unit_name,
            }
        )
    return units_data



if __name__ == '__main__':
    con = get_sql_connection()
    print(get_units(con))
    data = {
        "phone_no":9860797991,
        "customer_name":"Om Mahajan",
        "customer_email":"om.mahajan5@gmail.com",
        "total_cost":4000,
    }

    print(create_customer(data))
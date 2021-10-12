import mysql.connector as msc

__cnx = None


def get_sql_connection():
    global __cnx
    if __cnx is None:
        __cnx = msc.connect(host="localhost", user="root", passwd="bhavesh", database="grocery_store",
                           auth_plugin="mysql_native_password")

    return __cnx







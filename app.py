from flask import Flask, render_template, request, redirect, url_for,jsonify
import manage_products_dao as mp
import unit_table_dao as ut
from sql_conector import get_sql_connection
import orders_dao,customer_dao
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/manage_products')
def manage_products():
    con = get_sql_connection()
    data = mp.get_products(con)


    return render_template("manage_products.html", data=data)


@app.route('/add_products')
def add_products():
    con = get_sql_connection()
    units = ut.get_units(con)
    try:
        return render_template("add_products.html",data = units)
    except:
        return render_template("add_products.html",data = units)


@app.route("/delete_entry", methods=['POST'])
def delete_product():
    con = get_sql_connection()
    response = dict()

    try:
        post_data = json.loads(request.get_data())

        mp.delete_product(con, post_data['product_id'])
        response['value'] = True

    except:

        response['value'] = False

    return json.dumps(response)


@app.route('/save_product',methods=['POST'])
def save_product():
    if request.method == "POST":
        con = get_sql_connection()
        data = json.loads(request.get_data())
        response = dict()
        try:
            finalx = mp.insert_new_product(con,data)
            response['value'] = True
        except:
            response['value'] = False

        return json.dumps(response)
    else:
        return redirect(url_for("add_product"))




@app.route('/create_order')
def create_order():
    con = get_sql_connection()
    data = mp.get_products(con)

    return render_template('order.html')

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.create_order(request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/getProducts',methods=['GET'])
def get_products_list():
    con = get_sql_connection()
    data = mp.get_products(con)
    send = jsonify(data)
    return send


@app.route('/all_customers')
def all_customers():
    data = customer_dao.get_customer()
    return render_template('all_customers.html',data = data)

@app.route('/order_details')
def order_details():
    data = orders_dao.get_order_details()
    return render_template('order_details.html',data = data)


if __name__ == "__main__":
    app.run(debug=True)

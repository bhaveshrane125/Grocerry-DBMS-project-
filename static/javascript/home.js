$(document).ready(function () {
        $("#manage_products_btn").on('click',function () {
            window.location.replace('/manage_products')
        })
        $("#orders_btn").on('click',function () {
            window.location.replace('/create_order')
        })
        $("#all_customers_btn").on('click',function () {
            window.location.replace('/all_customers')
        })
        $("#order_details_btn").on('click',function () {
            window.location.replace('/order_details')
        })
})
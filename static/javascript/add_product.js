function add_product(){
    let errorx = false;
    product_name= document.getElementById('product_name').value
    price = document.getElementById('price').value
    unit_id=document.querySelector('input[name="unit"]:checked').value
    
    if (product_name =="" || price == "" || unit_id=="")
    {
        alert("Fill all details")
        console.log("Fill all details")
        
    }
    else{
        send_data();
    }
}

function send_data(){

    
    data = {

        'product_name' : document.getElementById('product_name').value,
        'price' : document.getElementById('price').value,
        'unit_id' :document.querySelector('input[name="unit"]:checked').value
    }

    

    let xhr = new XMLHttpRequest();
    xhr.open('POST','/save_product',true);
    xhr.onload = function(){
        let res =JSON.parse(xhr.responseText);
        if (res)
        {
            window.location.href = "/manage_products";
        }
        else{
            window.location.href = "/add_products";
        }
    }
    xhr.send(JSON.stringify(data))
}
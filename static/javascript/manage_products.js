function delete_entry(x){
    let data = {
        'product_id' : x
    }
    console.log(data)
    let xhr = new XMLHttpRequest();
    xhr.open('POST', "/delete_entry",true);
    xhr.onload = function(){
        if (xhr.status==200){
            console.log("Deleted: "+x);
            let res =JSON.parse(xhr.responseText)
            if (res){
                window.location.reload()
            }
            else{
                console.log("Not able ot delete entry")
            }
            
        }
        else{
            console.log("Error occured...");
        }
    }
    let yy = JSON.stringify(data);
    console.log(yy)
    xhr.send(yy)
}


function add_products_page(){
    window.location.replace("/add_products")
}
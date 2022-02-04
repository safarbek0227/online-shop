
window.addEventListener('load', send)
function send() {
    let data = localStorage.getItem('item')
    if (window.XMLHttpRequest) {
        var xhttp = new XMLHttpRequest();
    } else {  // code for IE6, IE5
        var xhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    xhttp.onreadystatechange = function () {
        if (xhttp.readyState === 4 && xhttp.status === 200) {
            var data = JSON.parse(this.responseText);
            let elem = ''
            for (let i = 0; i < data.success.length; i++) {
                products = data.success[i]
                elem += `<div class="row m-5">
                <div class="col-md-2">
                <img src="/media/${products.image}" alt="" width="90px">
                </div>
                <div class="col-md-2 p-1 mb-3">
                <h1 class="name">${products.name}</h1>
                </div>
                <div class="col-md-3 p-1 mb-3">
                <h1 class="d-inline">Price: $<span class="price">${products.price}</span></h1>
                </div>
                <div class="col-md-3 mb-3">
                <h2 class="d-inline">Count: <span class="count">1</span></h2>
                <br class="d-block d-lg-none">
                <button class="btn btn-warning" onclick="plus()">+</button>
                <button class="btn btn-warning" onclick="minus()">-</button>
                </div>
                <div class="col-md-1 mb-3">
                <h2 class="d-inline">
                $<span class="recent-price">${products.price}$</span>
                </h2>
                </div>
                </div>
                <a href="/card/" class="btn btn-danger d-inline" onclick=remove(${products.id})>X</a>
                <hr>`
                
            }
            document.querySelector('.cart').innerHTML = elem
        }
        
    }
    var url = "/addcard/"
    xhttp.open("GET", url + `?data=${data}`, true);
    xhttp.send();
    console.log('send')
}

function plus() {
    Element = event.target.parentElement.parentElement
    count = Element.querySelector('.count')
    price = Element.querySelector('.price').innerText
    recent = Element.querySelector('.recent-price')
    if (parseInt(count.innerText) > 25) {
        alert('its is ful')
    }
    else {
        count.innerText = parseInt(count.innerText) + 1
        recent.innerText = parseInt(price) * parseInt(count.innerText)
    }
}
function minus() {
    Element = event.target.parentElement.parentElement
    count = Element.querySelector('.count')
    price = Element.querySelector('.price').innerText
    recent = Element.querySelector('.recent-price')
    if (parseInt(count.innerText) < 2) {
        alert(' it is not')
    }
    else {
        count.innerText = parseInt(count.innerText) - 1
        recent.innerText = parseInt(price) * parseInt(count.innerText)
    }
}



function submit() {
    user = document.getElementById('name').value
    phone = document.getElementById('phone').value
    get = JSON.parse(localStorage.getItem('item'))
    cart = document.querySelectorAll('.count')
    if (user != '' && phone != '') {
        var text = []
        text.push(user)
        text.push(phone)
        arr =[]
        for (let i = 0; i < get.length; i++) {
            arr.push([get[i], parseInt(cart[i].innerText)])
        }
        text.push(arr)
        text = JSON.stringify(text)
        var xhttp = new XMLHttpRequest();
        var url = "/check/"
        xhttp.open("GET", url + `?data=${text}`, true);
        xhttp.send();
        localStorage.clear('item')
    }
    else {
        alert('please write your name and phone')
    }
    
}
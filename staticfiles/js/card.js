 window.addEventListener('load', calculator)
    let all = document.querySelectorAll('.recent-price')
    let total = document.querySelectorAll('.total')[0]
    let all_price = 0


    function calculator() {
        all_price = 0
        for (var i = 0; i < all.length; i++) {
            all_price += parseInt(all[i].innerText)
        }
        total.innerText = all_price
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
        calculator()
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
        calculator()
    }
    function pay(){
        text = ''
        count = document.querySelectorAll('.count')
        price = document.querySelectorAll('.price')
        recent = document.querySelectorAll('.recent-price')
        productname = document.querySelectorAll('.name')
        if (0<count.length){
            for(var i = 0; i < count.length; i++){
                text += `${productname[i].innerText}: ${count[i].innerText}ta ${price[i].innerText}$  Jami:${recent[i].innerText}$ \n`
            }
        }
        else{ 
            alert('siz haliyab biror bir ovqat zakaz qilmadiz')
        }
        console.log(text)
    }
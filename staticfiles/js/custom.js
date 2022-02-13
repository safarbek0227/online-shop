
// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// isotope js
$(window).on('load', function () {
    $('.filters_menu li').click(function () {
        $('.filters_menu li').removeClass('active');
        $(this).addClass('active');

        var data = $(this).attr('data-filter');
        $grid.isotope({
            filter: data
        })
    });

    var $grid = $(".grid").isotope({
        itemSelector: ".all",
        percentPosition: false,
        masonry: {
            columnWidth: ".all"
        }
    })
});

// nice select
$(document).ready(function () {
    $('select').niceSelect();
});

/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: false,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});

$(".product_owl-carousel").owlCarousel({
    loop: true,
    margin: 0,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    responsive: {
        0: {
            items: 1
        },
        768: {
            items: 2
        },
        1336: {
            item: 3
        },
        1340: {
            items: 4
        }
    }
});
let arr = []
if (JSON.parse(localStorage.getItem('item'))) {
    arr = JSON.parse(localStorage.getItem('item'))
}
else {
    arr = []
    localStorage.setItem('item', JSON.stringify([]))
}
function AddCart(id) {
    if (arr.includes(id) != true) {
        arr.push(id)
        localStorage.setItem('item', JSON.stringify(arr))
        //if add to cart btn clicked
        
    }
    else {
    }
}

function remove(id) {
    a = arr.indexOf(id)
    console.log(a)
    arr.splice(a, a + 1)
    localStorage.setItem('item', JSON.stringify(arr))
    send()
}

let count = 0;
$('.cart-btn').on('click', function () {
    // find the img of that card which button is clicked by user
    let imgtodrag = $(this).parent('.detail-box').parent('.box').find("img").eq(0);
    fly_cart(imgtodrag)
});
$('.product-btn').on('click', function () {
    // find the img of that card which button is clicked by user
    let imgtodrag = $(this).parent('.detail-box').parent('.col-md-6').parent('.row').find("img").eq(0);
    fly_cart(imgtodrag)  
});

  
$('.corusel-btn').on('click', function () {
    // find the img of that card which button is clicked by user
    let imgtodrag = $(this).parent('div').parent('div').parent('div').find("img").eq(0)
    fly_cart(imgtodrag)
});


function fly_cart(imgtodrag){
    let cart = $('.cart-nav');
    if (imgtodrag) {
        // duplicate the img
        var imgclone = imgtodrag.clone().offset({
            top: imgtodrag.offset().top,
            left: imgtodrag.offset().left
        }).css({
            'opacity': '0.8',
            'position': 'absolute',
            'height': '150px',
            'width': '150px',
            'z-index': '10000'
        }).appendTo($('body')).animate({
            'top': cart.offset().top + 20,
            'left': cart.offset().left + 30,
            'width': 75,
            'height': 75
        }, 1500, 'easeInOutExpo');
  
        setTimeout(function () {
            count = count +1
            $(".cart-nav").text(count);
        }, 1500);
  
        imgclone.animate({
            'width': 0,
            'height': 0
        }, function () {
            $(this).detach()
        });
    }   
}
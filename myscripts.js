
var items = [];

function myFunction() {



    var input, filter, ul, li, a, i;
    input = document.getElementById("search");

    // if (input.innerHTML == "") {
    //     items = [];
    // }

    filter = input.value.toUpperCase();
    ul = document.getElementById("menu");
    li = ul.getElementsByTagName("li"); 

    
    for (var item in items) {
        item.style.display = "block";
    }


    for (i = 0; i < li.length; i++) {
        a = li[i].children[0];
        if (a.innerHTML.indexOf(filter) > -1) {
            li[i].style.display = "block";
            items.push(li[i]);
        } else {
            li[i].style.display = "none";
        }
    }


  }


function profile() {
    document.getElementById("myDropdown").classList.toggle("show");
}
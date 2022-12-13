
function creds(){
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    console.log(username);
    console.log(password);

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/");
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {"username": username, "password": password};
    console.log(body);
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function(){

        console.log("success")
        const typeUser = xhttp.responseText;

        if(typeUser == 'NORMAL'){
            window.location.href = "http://127.0.0.1:5000/normalaccount";
        }
        else if(typeUser == 'BUSINESS'){
            window.location.href = "http://127.0.0.1:5000/business";
        }
        else if(typeUser == 'nah') {
            window.location.href = "http://127.0.0.1:5000/";
            alert("wrong username or password");
        }
    };
}



function displayall(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";  
    const url = "http://127.0.0.1:5000/printdb";
    const async = true;
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
    };
    xhttp.open(method, url, async);
    xhttp.send();
}


function avabCar(){
    const carid = document.getElementById("check").value;
    console.log(carid);
    const xhttp = new XMLHttpRequest();
    const method = "GET"; 
    const url = "http://127.0.0.1:5000/avab/"+carid;
    const async = true;
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
        };
    xhttp.open(method, url, async);
    xhttp.send();
}

function prevPurchases(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";  
    const url = "http://127.0.0.1:5000/purchases";
    const async = true;
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
    };
    xhttp.open(method, url, async);
    xhttp.send();

}

function serviceHistory(){
    const xhttp = new XMLHttpRequest();
    const method = "GET";  
    const url = "http://127.0.0.1:5000/services";
    const async = true;
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
    };
    xhttp.open(method, url, async);
    xhttp.send();
}

function search(){
    const make = document.getElementById("make").value;
    const model = document.getElementById("model").value;
    const year = document.getElementById("year").value;
    const color = document.getElementById("color").value;
    const engine = document.getElementById("engine").value;
    const transmission = document.getElementById("transmission").value;
    const classtype = document.getElementById("classtype").value;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/search");
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {"make": make, "model": model, "year": year, "color":color, "engine":engine, "transmission":transmission, "classtype":classtype};
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
    };
}

function createManu(){
    const address = document.getElementById("address").value;
    const phonenumber = document.getElementById("phonenumber").value;
    const email = document.getElementById("email").value;
    const nation = document.getElementById("nation").value;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/manuCreation");
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {"address": address, "phonenumber": phonenumber, "email": email, "nation":nation};
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
    };
}

function createDealer(){
    const manager = document.getElementById("manager").value;
    const email = document.getElementById("email").value;
    const address = document.getElementById("address").value;
    const phonenumber = document.getElementById("phonenumber").value;
    const nation = document.getElementById("nation").value;
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://127.0.0.1:5000/dealerCreation");
    xhttp.setRequestHeader("Content-Type", "application/json");
    const body = {"manager": manager, "email": email, "address": address, "phonenumber":phonenumber, "nation": nation};
    xhttp.send(JSON.stringify(body));
    xhttp.onload = function() {
        document.getElementById("paragraph").innerHTML = this.responseText;
    };
}




// function displayall(){
//     const xhttp = new XMLHttpRequest();
//     const method = "GET";  
//     const url = "http://127.0.0.1:5000/grades";
//     const async = true;
//     xhttp.onload = function() {
//         document.getElementById("paragraph2").innerHTML = this.responseText;
//     };
//     xhttp.open(method, url, async);
//     xhttp.send();
// }

// function getname(){
//     const name = document.getElementById("textinputname").value;
//     const xhttp = new XMLHttpRequest();
//     const method = "GET"; 
//     const url = "http://127.0.0.1:5000/grades/"+name;
//     const async = true;
//     xhttp.onload = function() {
//         document.getElementById("paragraph").innerHTML = this.responseText;
//         };
//     xhttp.open(method, url, async);
//     xhttp.send();
// }

// function addname(){
//     const name = document.getElementById("textinputname").value;
//     const grade = document.getElementById("textinputgrade").value;
//     var xhttp = new XMLHttpRequest();
//     xhttp.open("POST", "http://127.0.0.1:5000/grades");
//     xhttp.setRequestHeader("Content-Type", "application/json");
//     const body = {"name": name, "grade": grade};
//     xhttp.send(JSON.stringify(body));
//     xhttp.onload = function() {
//         getname();
//         displayall();
//     };
// }

// function updatename(){
//     const name = document.getElementById("textinputname").value;
//     const grade = document.getElementById("textinputgrade").value;
//     var xhttp = new XMLHttpRequest();
//     xhttp.open("PUT", "http://127.0.0.1:5000/grades/"+name);
//     xhttp.setRequestHeader("Content-Type", "application/json");
//     // const body = {"name": name, "grade": grade};
//     const body = {"grade": grade};
//     xhttp.send(JSON.stringify(body));
//     xhttp.onload = function() {
//         getname();
//         displayall();
//     };
// }

// function deleteuser(){
//     var xhttp = new XMLHttpRequest();
//     const name = document.getElementById("textinputname").value;
//     xhttp.onload = function() {
//         displayall()
//     };
//     xhttp.open("DELETE", "http://127.0.0.1:5000/grades/"+name);
//     xhttp.send()
// }
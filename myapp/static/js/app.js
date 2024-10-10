function show(d){
    document.getElementById("res").innerHTML += d;
}

function effacer(){
    document.getElementById("res").innerHTML = "";
}

function calculer(){
    let x = document.getElementById("res").innerHTML;
    let result = eval(x)
    document.getElementById("res").innerHTML = result;

    /*if (x == 'cos') {
        let result = Math.cos(x);
        document.getElementById("res").innerHTML = result;
    }
    else if (x == 'sin') {
        let result = Math.sin(x);
        document.getElementById("res").innerHTML = result;
    }*/

}

function cos(){
    let x = document.getElementById("res").innerHTML;
    let result = Math.cos(x);
    document.getElementById("res").innerHTML = result;
}

function sin(){
    let x = document.getElementById("res").innerHTML;
    let result = Math.sin(x);
    document.getElementById("res").innerHTML = result;
}

function tan(){
    let x = document.getElementById("res").innerHTML;
    let result = Math.tan(x);
    document.getElementById("res").innerHTML = result;
}

function SQRT(){
    let x = document.getElementById("res").innerHTML;
    let result = Math.sqrt(x);
    document.getElementById("res").innerHTML = result;
}
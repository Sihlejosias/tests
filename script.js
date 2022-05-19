var load = document.querySelector(".green");
var train = document.querySelector(".orange");
var deploy = document.querySelector(".purple");

// alert("Please note that this is a test website and for presantation purposes.")

load.onclick = function load() {
    window.location.href = "./load.html";
}

train.onclick = function train() {
    window.location.href = "./train.html";
}

deploy.onclick = function deploy() {
    window.location.href = "./deploy.html";
}
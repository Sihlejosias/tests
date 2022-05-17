var load = document.querySelector(".green");
var train = document.querySelector(".orange");
var deploy = document.querySelector(".purple");

load.onclick = function load() {
    alert("Load data clicked");
}

train.onclick = function train() {
    alert("Train model clicked");
}

deploy.onclick = function deploy() {
    alert("Deploy model clicked");
}
var counter = 0

document.getElementById("buttonplus").onclick = function increase(){
    counter++;
    document.getElementById("counter").textContent = counter;
}
document.getElementById("buttonmin").onclick = function decrease(){
    counter--;
    document.getElementById("counter").textContent = counter;
}
document.getElementById("buttonreset").onclick = function reset(){
    counter = 0;
    document.getElementById("counter").textContent = counter;
}
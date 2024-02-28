document.addEventListener("DOMContentLoaded",function(){
    const checkbox1 = document.getElementById("checkbox1");
    const button1 = document.getElementById("button 1");
    const button2 = document.getElementById("button 2");
    const button3 = document.getElementById("button 3");
    const subresult1 = document.getElementById("subresult");
    const result1 = document.getElementById("result");
    const mysubmit1 = document.getElementById("submitbutton");
    mysubmit1.onclick = function(){
        if (checkbox1.checked){
            subresult1.textContent = `Subbed !!!`;
        }
        else {
            subresult1.textContent = `Not Subbed =(`;
        }
        if (button1.checked){
            result1.textContent = `1 pressed`;
        }
        else if (button2.checked){
            result1.textContent = `2 pressed`;
        }
        else if (button3.checked){
            result1.textContent = `3 pressed`;
        }
        else {
            result1.textContent = `Select A button`;
        }
    
}})


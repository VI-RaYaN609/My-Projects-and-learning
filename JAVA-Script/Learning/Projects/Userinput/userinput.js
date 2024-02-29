document.getElementById("button").onclick = function(){
    let name =document.getElementById("userinput").value
    document.getElementById("Title").textContent = `Hello ${name}`
    window.alert(`YOUR GETTING HACKED ${name}`)
}

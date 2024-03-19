const inputs = document.querySelectorAll(".input")
const form = document.getElementById("form")
const checkbox = document.getElementById("check")
const removecookie = document.getElementById("remove")
const alive = 1 
function save(){
    form.addEventListener("submit",event=>{event.preventDefault()})
    if(checkbox.checked && inputs[0].value!="" && inputs[1].value!=""){
        createCookie("username",inputs[0].value,1)
        createCookie("password",inputs[1].value,1)
    }
    if(removecookie.checked){
        deleteCookie("username")
        deleteCookie("password")
    }
    deleteCookie("rayan")
    console.log(document.cookie)
}
function createCookie(name,value,alive){
    const date = new Date()
    date.setTime(date.getTime()+(alive*24*60*60*1000))
    let expires="expires="+date.toUTCString()
    document.cookie=`${name}=${value};${expires};path=/`
}
function deleteCookie(cookieName) {
    createCookie(cookieName,null,null)
}
function getCookie(cookieName){
    const decoded = decodeURIComponent(document.cookie).split("; ");//split cookie into an array
    let result
    decoded.forEach(cookie=>{
        if(cookie.indexOf(cookieName)==0){
            result= cookie.substring(cookieName.length+1)
        }
    })
    return result
}

document.addEventListener("DOMContentLoaded",()=>{
    let username = getCookie("username")
    let password = getCookie("password")
    inputs[0].value=``
    console.log(document.cookie)
    if(username!=null && password!=null){
        inputs[0].value= username
        inputs[1].value= password
    }
})
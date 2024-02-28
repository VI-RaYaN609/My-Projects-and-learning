let username = "Hello man"
let num = username.indexOf(" ")
let firstname = username.slice(0,num)
let lastname = username.slice(num+1)
console.log(firstname)
console.log(lastname)

const email = "example@gmail.com"

let emailname = email.slice(0,email.indexOf("@"))
let mail = email.slice(email.indexOf("@")+1)
console.log(emailname)
console.log(mail)
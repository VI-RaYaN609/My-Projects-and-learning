// const A ;mean A is can't be changed 
// var B ; mean B is a global variable
// let B ; mean we are changing the value of B localy
prompt = require("prompt-sync")()
print = console.log
const helloworld = () =>{
    c = require("prompt-sync")()("HEllo :")
    print(c)
    let A = Number(prompt("Enter A:"))
    var B = Number(prompt("Entere B:"))
    A == 25 ? A++:A-- //if A==25 {}else{}
    sum = A + B
    sub = A - B
    mult = A * B
    div = A / B
    console.log("The Sum of A and B is :"+sum)
    print("The Substraction of A and B is :"+sub)
    print("The Multiplication of A and B is :"+mult)
    print(`The Division of A and B is : ${div}`)
    print(`type of div is :${typeof div}`)
}

const Main = () => helloworld();

Main()
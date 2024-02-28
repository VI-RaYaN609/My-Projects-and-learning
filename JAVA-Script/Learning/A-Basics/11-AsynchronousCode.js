//Asynchronous code allow multiple operations to be run at the same time without blocking the below part of a 
//program  Example :

setTimeout(func1,3000)
console.log("HelloWorld 2")

function func1(){
    console.log("HelloWorld 1")
}
// To Handle Asynchronous code you can use multiple methods such as callbacks,Promies,Async/Await :
// example 

function func4(){
    console.log("HelloWorld 4")
}

function func3(callback){
    setTimeout(()=>{
        console.log("HelloWorld 3")
        callback()
    },3000)
}

func3(func4)
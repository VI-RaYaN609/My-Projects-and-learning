/* Promise = An Object that manages asynchronous operations,
             Wrap a Promise Object around {asynchronous code}
             "I promise to return a value"
             PENDING -> RESOLVED or REJECTED
             
             new Promise( ( resolve,reject ) => {
                asynchronous code;
             }) 
*/

function TASK1(callback){
    setTimeout(() => {
        console.log("TASK 1 Is Completed")
        callback()
    }, 500);    
}
function TASK2(callback,argument){
    setTimeout(() => {
        console.log("TASK 2 Is Completed and "+argument)
        callback()
    }, 500);    
}
function TASK3(callback){
    setTimeout(() => {
        console.log("TASK 3 Is Completed")
        callback()
    }, 500);    
}
function task1(){
    return new Promise((resolve,reject)=>{
    //if you use reject other functions wont start you can try it by replacing resolve with reject and see  
        setTimeout(() => {
            resolve("Task 1 Is Completed or ERRORED if replaced resolve by reject")
        }, 1800);
    })
}
function task2(){
    return new Promise((resolve,reject)=>{
        setTimeout(() => {
            let i = 1 + 3/2
            let result
            try{
                result = 1/i
            }
            catch(error){
                console.error("bruhhhhh , ",error)
            }
            resolve("Task 2 Is Completed + result = "+result)
        }, 1000);
    })
}
function task3(){
    return new Promise((resolve,reject)=>{
        setTimeout(() => {
            resolve("Task 3 Is Completed")
        }, 1000);
    })
}
function delay(){
    return new Promise((resolve,reject)=>{
        setTimeout(() => {
            resolve("This is a delay")
        }, 5000)
    })
}



// This can get a lot longer which make code unreadable (CALLBACK HELL)
TASK1(()=>{
    TASK2(()=>{
        TASK3(()=>{
            console.log("All TASKES using callbacks are finished")
            console.log("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        })
    },`bruh this is so unreadable`)
})

//This way the code is way more readable using promises
task1().then(value =>{console.log(value);return task2()})
       .then(value =>{console.log(value);return task3()})
       .then(value =>{console.log(value);return "RETURNED"})
       .then(value =>{console.log("All Taskes using Promises are complete + "+value+"\n\\\\\\\\\\\\\\\\\\\\")})
       .catch(error =>{console.log(error)}) //catch any rejects from the promises 
       //! IF any of the promises reject then no other functions will execute below it


// You can also use this way

Promise.all([task1(),task2(),task3(),delay()]) //this way it will run all promises and return an array containing
       .then((values)=>{console.log("This is Promise.all",values)})//all resolve values of the promises
       .then(()=>{console.log("\\\\\\\\\\\\\\\\\\\\")})
       .catch((error)=>{console.error(error)})

//! ASYNC/AWAIT
/*Async/Await = Async = make a function return a promise 
                Await = make an async function wait for a promise 
                (you need to use Async function to use Await)

                Allows you to write asynchronous code in a synchronous manner
                Async doesn't have resolve or reject parameters
                Everything after Await is placed in an event queue
                */
function thing1(){
    return new Promise((resolve,reject)=>{
        setTimeout(()=>{
            let idk = true
            if(idk){
                console.log("Thing1 code running ........")
                setTimeout(() => {
                    resolve("Code ran Successfully")
                }, 1500);
            }
            else{
                reject("Code Failed to run")
            }},5000)
    })
}

async function something(){
    try{
        const idk = await thing1() 
        //try to remove await and you will see that this function continue to run
        //without waiting for thing1 function to be complete
        console.log("the async 'something' function result "+idk)
    }
    catch(error){
        console.log("Errored !!!!",error)
    }
}
something()
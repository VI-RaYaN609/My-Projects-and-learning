// destructuring is usefull to use in the function arguments will allows you to pass a array or object
// and split them easly into multiple arguments in the () of the function
//TODO There are two types of destructuring :
//?---1 Array destructuring

const food = ['apple','orange','hamburger','pizza']
const [food1,food2,...food_rest]=food

console.log(food1)
console.log(food2)
console.log(food_rest)
 
console.log("********")
console.log("********")

//?---2 Objects destructuring

const person1={
    name:"SquidWards",
    age:60
}
const person2={
    name:"Patrick",
    age:43,
    job:'DeliveryDriver',
    married:false
}

const {name,age,...rest} = person2;        //replace person1 by person2 or inverse

//! Example of use in function argument

function print({name,age,job="defaultValue",...rest}){
    console.log("Name: "+name+"| Age: "+age+"| job: "+job+"| Rest: ",rest)
}
print(person1)
console.log(".........")
print(person2)
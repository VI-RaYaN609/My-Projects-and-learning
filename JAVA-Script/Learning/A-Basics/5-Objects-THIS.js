//TODO Objects are similar to dictionary in python
this.name = "hello";
const object = {
  // Key : Value  ,
    name : "brian",
    age:30,
    job:'dog',   
    hello1:()=>{console.log(`first function :${this.name}`)},        // This and below it are NOT THE SAME
    hello2:function(){console.log(`second function :${this.name}`)},
}

console.log(object.name)
console.log(object.age)
console.log(object.job)
object.hello1()  // THIS SHOW 'hello' BECAUSE IT TRY TO ACCES THE 'this.name' IN THE GLOBAL SCOPE OUTSIDE THE OBJECT
object.hello2()

//TODO Constructor = special method for defining the properties and methods of objects

function Car(brand,model,year){     //!VERY SIMILAR TO SIMPLE CLASSES IN PYTHON
  this.brand = brand,
  this.model = model,
  this.year = year
}
const car1 = new Car("Ferrari","812SuperFast","2024")
const car2 = new Car("Porshe","911Carrera","2024")
console.log(car1)
console.log(car2)
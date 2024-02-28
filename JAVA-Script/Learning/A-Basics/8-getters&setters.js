//setter make sure that a function argument is within a specific condition
//getter take the function argument if possible and make it usable
class Person{
    constructor(name,age){
        this.name = name
        this.age = age
    }
    set name(newName){
        if(typeof newName ==="string" &&newName.length >0){
            this._name = newName;
        }
        else{console.error("Name Must be a non empty string")}
    }
    set age(newage){
        if(typeof newage ==="number" && newage>0){
            this._age = newage;
        }
        else{console.error("Age must be a number greater than 0")}
    }
    get name(){return this._name}
    get age(){return this._age}
    get nage(){return this.name+this.age}    //you can also use get and have a variable exist without declaring
}                                            // in the constructor

const man = new  Person("Alex",25)
const man2 = new  Person(405,"hotdog")

console.log(man2.name)
console.log(man2.age)
console.log(man.name)
console.log(man.age)
console.log(man.nage)
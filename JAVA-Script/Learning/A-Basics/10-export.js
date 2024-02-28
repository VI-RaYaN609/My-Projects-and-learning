export const value = 5

export function helloworld(){
    console.log("HelloWorld")
}
export class Person{
    constructor(name,age){
        this.name = name
        this.age = age
    }
    set name(newName){
        if(typeof newName ==="string" &&newName.length >0){
            this._name = newName
        }
        else{console.error("Name can only be a not empty string")}
    }
    get name(){
        return this._name
    }
    set age(newAge){
        if(typeof newAge ==="number"&newAge > 0){
            this._age = newAge
        }
        else{console.error("Name can only be a not empty string")}
    }
    get age(){
        return this._age
    }
}
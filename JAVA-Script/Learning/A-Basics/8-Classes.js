//Classes are cleaner and more modern to use objects instead of the constructor functios  
class Parent {
    // IDK WHAT TO TYPE
    ok="bruh"
    uuuuuh(){
        console.log("UUUUUUUUUUH both Parent and hello class have this as a object function")
    }
    static staticparent(){
        console.log("The Parent and hello class have this function as a static function")
    }
}

class hello extends Parent{
    static PI = Math.PI       //Static variables/function are only accessible by the class
    static helloes = 0        // this case " hello.PI " " hello.idk() " ....
    static idk(){
        console.log("IDK")
    }
/********************************************************************************************************************** */
    constructor(name,some){    //same as //! def __init__()
        super()                //same as //! super().__init__()
        this.name = name;
        this.some = some;
        hello.helloes++
    }
    printclass(){              //Class Methods
        console.log("Hello, ",this.name,this.some)
    }
}

const hello1 =new hello('ray','bruh')
hello1.printclass()
hello1.uuuuuh()
console.log("hello1.ok",hello1.ok)

console.log("****************************")
//calling static functions and variables
console.log("Number of hello classes :",hello.helloes)
hello.idk()
hello.staticparent()
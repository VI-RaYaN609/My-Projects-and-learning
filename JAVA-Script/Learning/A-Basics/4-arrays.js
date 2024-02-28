let array = ["number1","number2","number3"]
let numberofelements = array.length

// array.push("number4") //append value to the end
// array.pop() //remove last value of the array
// array.unshift("unShift1","unShift2") //append to start
// array.shift()          //move array to the left
 
console.log(array)
console.log("Number of elements is :"+numberofelements)


 
let numbers = [2,3,1,5,4]
//sort Method 
numbers.sort((a,b)=>a-b)         //This for numerical sorting for alphabetical you need to use this :
            //b-a for reverse    //numbers.sort((a,b)=>a.localeCompare(b))
console.log(numbers)

// ... is 'spread operator' which allow a string or an array
//     to be expanded into separate elements(unpack)

let some = [...array,...numbers]
let max = Math.max(...numbers)
console.log(max)

// ... can also as a 'rest operator' which allow multiple 
// values into a single array

function restoperator(...foods){
    console.log(foods)
}
restoperator("pizza","salad")
// You CAN use objects as elements of an array
const  example = [{num:2,str:"abc"},{num:3,str:"efg"}]
console.log(example)
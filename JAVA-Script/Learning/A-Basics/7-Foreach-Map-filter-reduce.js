//? ForEach Method
// ForEach method loops the elements of an array and apply a function to each of its elements
let array = ['a','b','c','d']
let array2 = [1,3,4,5]
array2.forEach(stringprint)
function stringprint(char){
    console.log(char)
}
function plus(element,index,arrayy){ // the index and array are provided by the 'forEach'
    arrayy[index] = element+1        //! YOU HAVE TO DO THEM IN THAT ORDER 'element,index,array'
}
array2.forEach(plus)
console.log("Array2 + :",array2)

//? Map Method
// similar to forEach but you need to have return statement which return the value of the array at the index
function square(element){
    return Math.pow(element,2)
}
function squaremove(element,i,a){
    element = Math.pow(a[i+1],2)
    return element
}

const squares = array2.map(square)
const squaremoved = array2.map(squaremove)
squaremoved.pop()
console.log("Squares :",squares)
console.log("SquaresMoved :",squaremoved)

//?Filter
//
const numbers= [1,2,3,4,5,6,7]
const oddnum = numbers.filter(odd)
const evennum = numbers.filter(even)

console.log("Odd :",oddnum)
console.log("Even :",evennum)
function even(i){
    return i%2==0 //return true or false
}
function odd(i){
    return i%2!=0 
}
//? Reduce
//reduce function reduces the elements of an array to a single value
const sumnum = numbers.reduce(sum)
const maxnum = numbers.reduce(max)

console.log("Sum of numbers :",sumnum)
console.log("Max of numbers: ",maxnum)

function sum(previous,ele){  //when using reduce it will make the returned value the previous so it does something
    return previous + ele    //until it reachs the final index and then the previous will be the single value
}
function max(previous,ele){
    return Math.max(previous,ele)
}
try{ // Code that might cause an error
  const dividend = require("prompt-sync")()("Enter a dividend: ")
  const divisor = require("prompt-sync")()("Enter a divisor: ")
  if (divisor == 0){
    throw new Error("Can't devide by 0")             //Throw Error so it means it will go to catch section
  }
  else if (isNaN(dividend) || isNaN(divisor)){
    throw new Error("Enter A number please ")
  }
  const result = dividend/divisor
  console.log(result)
}                    
catch(error){//Code That run if error
    console.error(error)  
}
finally{ //(Optional)
    //Code That Always run
    console.log("Finally code")
}
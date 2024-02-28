function first(callback){
    console.log("This First")
    callback()
}
function second(){
    console.log("Then this second")
}
first(second) //This way you make sure that you execute "second"after first being executed
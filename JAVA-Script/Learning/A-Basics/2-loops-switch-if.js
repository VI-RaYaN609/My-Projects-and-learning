print =console.log
function loop(){
    array = [1,2,3]
    for (let i=0;i < array.length; i++) {
        const element = array[i];
        print(element)
    }//This For loop is the same as 
    for (let i of array){
        console.log(i)
    }// As This

    let i = 0
    while (i<4) {
        var element = array[i]
        print(element)
        i++
    }
    i = 5
    do {
        print("HELLO")
    }while(i< 4)
    i=0
    switch (array[i]) {
        case 1:
            console.log("1")
            break;
        case 2:
            console.log("2")
        default:
            break;
    }
}
function main(){
    loop()
}
main()
document.addEventListener("DOMContentLoaded",function(){
    const a = document.getElementById("new")
    let red = 0 ; let RED =false
    let green = 100 ; let GREEN =false
    let blue = 200  ;let BLUE =false
    function RGBanimation(){
        if (red>254){RED=false}
        if(red<1){RED=true}
        if (green>254){GREEN=false}
        if(green<1){GREEN=true}
        if (blue>254){BLUE=false}
        if(blue<1){BLUE=true}
        
        if(RED){red+=4}else{red-=4} 
        if(GREEN){green+=4}else{green-=4} 
        if(BLUE){blue+=4}else{blue-=4} 
        a.style.backgroundColor=`rgb(${red},${green},${blue})`
        a.style.borderColor=`rgb(${red},${green},${blue})`
    }
    setInterval(RGBanimation,10)
            
})

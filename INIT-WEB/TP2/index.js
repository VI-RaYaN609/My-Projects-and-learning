let THEME = 100
let max =80 ; let min = 20
let red = 0 ; let RED =false
let green = 100 ; let GREEN =false
let blue = 200  ;let BLUE =false
let Lightness = 50 ;let LIGHT = false
const header= document.getElementById("header")
const navbar = document.getElementById("navbar")
const ol = document.getElementsByTagName("ol")
const button1 = document.getElementsByClassName("button1")
const button2 = document.getElementsByClassName("button2")

function scrollto(id){
    const element = document.getElementById(id)
    element.scrollIntoView({ behavior: 'smooth', block: 'start' });
}
function DarkTheme(){
    for(let i of document.getElementsByClassName("button1")){
        i.addEventListener("mouseover",function(){
            i.style.backgroundColor=`hsla(160, 7%, 20%,0.4)`;i.style.color=`rgb(150,150,150)`
        })
        i.addEventListener("mouseout",function(){
            i.style.backgroundColor=`hsla(160, 17%, 10%,0.4)`;i.style.color=`white`
        })
    }
    document.body.style.backgroundImage=`url('dark.jpg')`
    navbar.style.backgroundColor=`hsla(160, 17%, 10%,0.6)`
    header.style.color = `rgb(255,255,255)`
    for(let i of ol){i.style.backgroundColor=`hsla(160, 17%, 10%)`}
    for(let i of button2){i.style.backgroundColor=`hsla(160, 17%, 10%,0.6)`;i.style.color=`white`}

    for(let i of button1){i.style.backgroundColor=`hsla(160, 17%, 10%,0.6)`;i.style.color=`white`}
    Lightness = 90
    THEME = 100
    max =100
    min = 80
}
function LightTheme(){
    for(let i of document.getElementsByClassName("button1")){
        i.addEventListener("mouseover",function(){
            i.style.backgroundColor=`hsla(160, 77%, 70%,0.2)`;i.style.color=`rgb(150,150,150)`
        })
        i.addEventListener("mouseout",function(){
            i.style.backgroundColor=`hsla(160, 97%, 90%,0.2)`;i.style.color=`black`
        })
    }
    document.body.style.backgroundImage=`url('Light2.jpg')`
    navbar.style.backgroundColor=`hsla(160, 97%, 90%,0.4)`
    header.style.color = `rgb(0,0,0)`
    for(let i of ol){i.style.backgroundColor=`hsla(160, 87%, 80%)`}
    for(let i of button2){i.style.backgroundColor=`hsla(160, 87%, 80%,0.2)`;i.style.color=`black`}
    
    for(let i of button1){i.style.backgroundColor=`hsla(160, 97%, 90%,0.2)`;i.style.color=`black`}
    Lightness=10
    THEME = 60
    max =20
    min = 0
}
function SpecialTheme(){
    for(let i of document.getElementsByClassName("button1")){
        i.addEventListener("mouseover",function(){
            i.style.backgroundColor=`hsla(160, 97%, 22%,0.4)`;i.style.color=`hsl(160, 100%, 95%)`
        })
        i.addEventListener("mouseout",function(){
            i.style.backgroundColor=`rgba(1, 61, 41,0.1)`;i.style.color=`hsl(160, 100%, 75%)`
        })
    }
    document.body.style.backgroundImage=`url('background.avif')`
    navbar.style.backgroundColor=`rgba(1, 61, 41,0.4)`
    header.style.color = `rgb(14, 102, 117)`
    for(let i of ol){i.style.backgroundColor=`hsla(160, 97%, 22%)`}
    for(let i of button2){i.style.backgroundColor=`hsla(160, 97%, 22%,0.1)`;i.style.color=`hsl(160, 100%, 75%)`}

    for(let i of button1){i.style.backgroundColor=`rgba(1, 61, 41,0.1)`,i.style.color=`hsl(160, 100%, 75%)`}
    Lightness= 50
    THEME = 70
    max =80
    min = 30
}

document.addEventListener("DOMContentLoaded",function(){
    navbar.style.backgroundColor=`rgba(1, 61, 41,0.4)`
    header.style.color = `rgba(14, 102, 117)`
    const H2 = document.getElementsByClassName("RGBanimation")
    
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
        document.getElementById("special").style.color=`rgb(${red}, ${green}, ${blue})`
        document.getElementById("back").style.backgroundColor=`rgb(${red}, ${green}, ${blue})`
        document.getElementById("back").style.borderColor=`rgb(${red}, ${green}, ${blue})`
        for(let h2 of H2){
            h2.style.color=`rgb(${red}, ${green}, ${blue})`
        }
    }

    const ps = document.getElementsByTagName("p")
    function HSLanimation(){
        if (Lightness>max){LIGHT=true}else if (Lightness<min){LIGHT=false}
        if(LIGHT){Lightness-=1}else{Lightness+=1}
        for(let h2 of H2){
            h2.style.backgroundColor=`hsl(160, ${THEME}%, ${Lightness}%)`
        }
        for (let p of ps){
            p.style.color=`hsl(160, ${THEME}%, ${Lightness}%)`
        }
    }



    setInterval(RGBanimation, 10);
    setInterval(HSLanimation, 50);
})
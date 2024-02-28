var hel = Array()
document.addEventListener("DOMContentLoaded",function(){
    const container = document.getElementById("circle-container")
    for(let i=0;i<16;i++){
        if(container.children.length<16){
            let x = Math.random()*60 + 20
            let y = Math.random()*60 + 20
            const pr = document.createElement("div")
            pr.className = "circles"
            let ind = i
            if(i>7){ind-=8}
            let direction = ind
            let entered = false

            if (isNaN(...hel)){
               hel[0]= direction
            }
            else if (hel.includes(direction)){
                let i = hel.indexOf(direction)
                entered =true
                do {
                    direction = parseInt(Math.random()*8)
                }while(hel[i]==direction)
            }
            if(!entered){
                if(hel.length>1){
                hel.shift()
                hel[1]=direction
                }
                else if(hel[0]!=direction){
                    hel[1]=direction
                }
            }
            else{
                    hel.shift()
                    hel[1]=direction
                }
                        
            pr.dataset.direction = direction
            
            container.appendChild(pr)
            
            pr.style.width = `100px`
            pr.style.height = `100px`
            pr.style.left =`${x}%`
            pr.style.top =`${y}%`
      }
    }
    let colx = 73
    let plus = true
    function colorul(){
        if(plus){colx+=0.5; if(colx>=95){plus=false}}
        else{colx-=0.5;if(colx<=33){plus=true}}
        document.getElementById("ul").style.backgroundColor = `hsl(279,${colx}%, 26%)`
    }

    let colx2 = 18
    let plus2 =true
    function colorcircle(){
        if(plus2){colx2+=0.5; if(colx2>=40){plus2=false}}
        else{colx2-=0.5;if(colx2<=9){plus2=true}}
        circles = document.getElementsByClassName("circles")
        for (var okf = 0; okf < circles.length; okf++) {
            circles[okf].style.backgroundColor = `hsl(247, ${colx2}%, 81%)`;
        }
    }

    function check(){
        for(let pr of container.children){
            let x = parseFloat(pr.style.left)
            let y = parseFloat(pr.style.top)
        if (x>100||y>100||x<-10||y<-20){
            if(pr.dataset.direction==8){pr.dataset.direction=0}
            else{pr.dataset.direction++}
           }
        }
       }    
    function animate(){
        for(let pr of container.children){
            let x = parseFloat(pr.style.left)
            let y = parseFloat(pr.style.top)
            let direction = parseInt(pr.dataset.direction)
            switch (direction){
                case 0:
                    y+=0.17
                    break
                case 1:
                    x+=0.125;y+=0.125
                    break  
                case 2:
                    x+=0.17
                    break
                case 3:
                    x+=0.125;y-=0.125
                    break
                case 4:
                    y-=0.17
                    break
                case 5:
                    x-=0.125;y-=0.125
                    break  
                case 6:
                    x-=0.17
                    break
                case 7:
                    x-=0.125;y+=0.125
                    break
            }
            pr.style.left = `${x}%`
            pr.style.top = `${y}%`

        }

}
    function main(){
    setInterval(check,30)
    setInterval(animate,5)
    setInterval(colorul,5)
    setInterval(colorcircle,5)
}
main()
})
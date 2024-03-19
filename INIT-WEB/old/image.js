document.addEventListener("DOMContentLoaded",function(){
    const particleContainer = document.getElementById("particle-container")
    let x,y;
    x=50 ; y= 50;
    function create(){
        let x = Math.random()*20 + 40
        let y = Math.random()*20 + 40
        if(particleContainer.children.length<=150){
        const particle = document.createElement("div")
        particle.className = "particles"

        const size = Math.random()*8 + 5
        const direction = Math.floor(Math.random()*4)
        
        particle.dataset.direction = direction
        particleContainer.appendChild(particle)

        particle.style.backgroundColor=`rgb(${Math.floor(Math.random()*255)},${Math.floor(Math.random()*255)},${Math.floor(Math.random()*255)})`
        particle.style.width = `${size}px`
        particle.style.height= `${size}px`
        particle.style.left = `${x}%`
        particle.style.top = `${y}%`
    }
    }
   function Animate(){
    for(let par of particleContainer.children){
        let x= parseFloat(par.style.left);
        let y= parseFloat(par.style.top)
        const direction = parseInt(par.dataset.direction);
        switch (direction){
        case 0 :
            x-- ; y++
            break
        case 1 :
            x-- ; y--
            break
        case 2 :
            x++ ; y++
            break
        case 3 :
            x++ ; y--
            break
        }
        par.style.top =`${y}%`
        par.style.left =`${x}%`
        if (x>100 ||y>100||x<0||y<0){
            par.remove()
        }
    }
   }
   function generate(){
       setInterval(create,50)
       setInterval(Animate,20)
   }
   generate()
})
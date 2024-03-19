// ALL ESSENSIAL DOCUMENT COMMANDS :
document.addEventListener("DOMContentLoaded",function(){//this will make the code in the function run 
                                                        //when page fully loaded

    const box1= document.getElementById("box1")            //will have the HTML element that has id of box1 (div)
    const boxes = document.getElementsByClassName("box") //will have a collection of HTML elements that has specified ClassName(divs)
    const Divs = document.getElementsByTagName("div") //will have a collection of HTML elements that has specified TagName
    const firstchild = document.querySelector("p")     //will have first of element/s of "p"
    const children = document.querySelectorAll("p")    //will have a nodelist of all element/s with "p"
                                                       //can put # for id and . for class
    //queryselectorall is most used because it has forEach method by default

    firstchild.textContent+=` | First Child`
    console.log("FIRST CHILD",firstchild)

    //HTML collections Utilisasion 
    //? Method 01:
    Array.from(Divs).forEach(div=>{
        div.style.fontSize=`40px`
    })
    //? Method 02:
    for(let box of boxes){
        box.style.backgroundColor=`tomato`
    }

    //NodeList Utilisation 
    //? Method 01:
    children.forEach(child=>{
        child.style.textAlign=`center`
    })

    //? Method 02:
    for(let child of children){
        child.textContent+=" | Children"
        child.style.color=`red`
    }
    console.log("CHILDREN",children)

    //! Element Creation|Removal:{
    //? Element Creation :
    const NewH1 = document.createElement("h1")    //create an element (anything h1,p,a,li,ul....)
    NewH1.id = "hoverID"                          //Set The id for the element
    NewH1.classList = "HoverClass"                //Set The Class for the element
    NewH1.textContent = "hover"                   //Set the textcontent of the element

    //? element.style.(any CSS Proprety [color,font..]):
    NewH1.style.textAlign=`center`                
    NewH1.style.backgroundColor = `rgb(90,90,90)` 
     
    //? appending element to another element (so it would be visible):
    //document.body.appendChild(NewH1)          //Append the element to the body at the end
    //box1.appendChild(NewH1)                   //Append the element to box1 at the end
    document.body.prepend(NewH1)                //Append the element to the body at the start
    //box1.prepend(NewH1)                       //Append the element to box1 at the start
    //document.body.insertBefore(NewH1,box2)    //Append the element to the body before box2
    //box1.insertBefore(NewH1,box2)             //Append the element to the box1 before box2 (ERROR box2 and box1 are siblings)
    
    //? removing element
    //TODO element is in body:
    //document.body.removeChild(Element)
    //TODO element is elsewhere:
    //Parent_element.removeChild(Element)
    
    //! element_here.addEventListener("Event_here",function_here(){})
      // this event listener will listen for events happening and will apply a function given 
      // example :
      NewH1.addEventListener("mouseover",()=>{
          NewH1.style.color=`rgb(95,150,255)`
          NewH1.style.backgroundColor=`rgb(0,0,0)`
          NewH1.textContent = "NICE !!!"
      })
      NewH1.addEventListener("mouseout",()=>{
          NewH1.style.color=`rgb(0,0,0)`
          NewH1.style.backgroundColor = `rgb(90,90,90)`
          NewH1.textContent = "hover"
      })
})
// ALL ESSENSIAL WINDOW COMMANDS
document.addEventListener("DOMContentLoaded",function(){
    console.log("Inner Height "+window.innerHeight)
    console.log("Inner Width "+window.innerWidth)
    console.log("outer Height "+window.outerHeight)
    console.log("outer Width "+window.outerWidth)
    console.log("Scroll X "+window.scrollX)
    console.log("Scroll Y"+window.scrollY)

    console.log("Window href "+window.location.href) 
    //by this you can redirect to other website like <a>hyperlinks OR by doing
    //window.open("https://google.com")
    //its the same as <a href="google.com" target="_blank"></a>

    //window.close() this will close the window

    console.log("Window hostname "+window.location.hostname)
    console.log("Window PathName "+window.location.pathname)
    window.alert("alert")
    window.prompt("Enter Name :")
    window.confirm("confirm")
})
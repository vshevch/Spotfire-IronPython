//change (None) to ALL 
function changeSelection(){
  $("#none2all .sf-element-text-box").each(function(i,e){
   if (e.innerHTML=="(None)") e.innerHTML="All"
  })
}

 //change (None) when dropdown is visible
$("#none2all").on('click',function(){
 a=document.querySelector("#none2all .ListItems:first-child").firstChild
 a.innerText="All"
 setTimeout(changeSelection,500) //if does not work, increase this value
})

 //change (None) first time
changeSelection()

// Get the modal
let join_btn = document.getElementById("joinButton");
let no_btn = document.getElementById("notJoinBtn");
var modal = document.getElementById("myPopupModal");
var url;

// Get the button that opens the modal
var btn = document.getElementById("myPopupBtn");

// Get the <span> element that closes the modal

function openJoinRequestModal() {
  modal.style.display = "block";
 
}
no_btn.onclick = function(event){
  
  modal.style.display = "none";
  console.log("nawagtang");
}



// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

join_btn.onclick = function(event){
  console.log(join_btn);
}
function openJoinModal(i){
  console.log("the thing is: ",i);
  console.log("nagpakita");
  
  document.getElementById("joinButton").value = i;
  // url = "/board/join-board/1"
  url = `/board/join-board/${i}`
  // url = `/board/1`
  console.log(url)
}
function redirect(url){ 
  // window.location.href = url
}
let btn1 = document.getElementById("joinButton")
btn1.onclick =  function(){
  window.location.href = url
  // console.log(url)
}




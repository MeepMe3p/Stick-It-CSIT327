// Get the modal
let join_btn = document.getElementById("joinButton");
var modal = document.getElementById("myPopupModal");
var url;

// Get the button that opens the modal
var btn = document.getElementById("myPopupBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
console.log(span);

// When the user clicks on the button, open the modal
btn.onclick = function() {
  console.log("nagpakita");
  modal.style.display = "block";
}


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
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
  modal.style.display = "block";  
  
  document.getElementById("joinButton").value = i;
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
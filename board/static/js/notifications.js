let popup = document.getElementById("notification-popup");
let close_btn = document.getElementsByClassName("close-notif")[0];
function toggleNotificationPopup() {
    // popup.style.display = popup.style.display === "block" ? "none" : "block";
    // console.log("epressed");
    popup.style.display = "block"

}
window.onclick = function(){
    popup.style.display == "hidden"
    console.log(popup)
    if(popup.style.display == "block"){
    }
    console.log("goes here but off")
}
close_btn.onclick = function(){
    popup.style.display == "hidden"
    console.log("i was ressed")
}

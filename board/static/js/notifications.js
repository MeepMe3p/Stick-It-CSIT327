let popup = document.getElementById("notification-popup");
let close_btn = document.getElementsByClassName("close-notif")[0];

function toggleNotificationPopup() {
    popup.style.display = popup.style.display === "block" ? "none" : "block";
    console.log("pressed open")

}

close_btn.onclick = function () {
    popup.style.display = "none";
    console.log("pressed close")
};




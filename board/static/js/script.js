function toggleNotificationPopup() {
    const popup = document.getElementById("notification-popup");
    popup.style.display = popup.style.display === "block" ? "none" : "block";
    console.log("epressed");
}

document.addEventListener("click", function (event) {
    const popup = document.getElementById("notification-popup");
    console.log(popup)
    if (!popup.contains(event.target)) {
        console.log("wenr here")
        popup.style.display = "hidden";
    }
});


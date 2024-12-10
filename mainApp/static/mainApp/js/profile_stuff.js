// Initialize zoom level
let zoomLevel = 1;  // 100% zoom

// Get board container
const boardContainer = document.querySelector('.board-container');

// Get zoom buttons
const zoomInBtn = document.querySelector('.zoom-in-btn');
const zoomOutBtn = document.querySelector('.zoom-out-btn');
const zoomDisplay = document.querySelector('.zoom-display');

// Function to update zoom
// function updateZoom() {
//     const baseGridSize = 20;  // Set the base size of the grid for 100% zoom

//     // Set transform scale for zooming
//     boardContainer.style.transform = scale(${zoomLevel});

//     // Adjust the background size dynamically based on zoom level
//     boardContainer.style.backgroundSize = ${baseGridSize / zoomLevel}px ${baseGridSize / zoomLevel}px;

//     // Get current scroll position and adjust transform origin for centered zoom
//     const boardRect = boardContainer.getBoundingClientRect();
//     const centerX = boardRect.width / 2;
//     const centerY = boardRect.height / 2;
//     const scrollLeft = window.scrollX + centerX;
//     const scrollTop = window.scrollY + centerY;

//     // Adjust the transform origin to ensure the zoom is centered on the screen
//     boardContainer.style.transformOrigin = ${scrollLeft}px ${scrollTop}px;

//     // Update zoom display percentage
//     zoomDisplay.textContent = ${Math.round(zoomLevel * 100)}%;
// }



// Zoom In Button Click Event
// zoomInBtn.addEventListener('click', function() {
//     if (zoomLevel < 2) {  // Limit zoom-in to 200%
//         zoomLevel += 0.1;
//         updateZoom();
//     }
// });

// Zoom Out Button Click Event
// zoomOutBtn.addEventListener('click', function() {
//     if (zoomLevel > 0.5) {  // Limit zoom-out to 50%
//         zoomLevel -= 0.1;
//         updateZoom();
//     }
// });

// Initial zoom update
// updateZoom();

const circles = document.querySelectorAll('.circle');
const modal = document.getElementById('general-users-mod');

circles.forEach(circle => {
    circle.addEventListener("mouseenter", () => {
        modal.classList.remove('disappear');
        modal.classList.add('appear');
        modal.style.display = 'block'; 
    });
});

// document.addEventListener('click', (event) => {
//     const isClickInsideModal = modal.contains(event.target);
//     circles.forEach(circle => {
//         const isClickInsideCircle = circle.contains(event.target);
//         if (!isClickInsideModal && !isClickInsideCircle) {
//             modal.classList.remove('appear');
//             modal.classList.add('disappear');
//             setTimeout(() => {
//                 modal.style.display = 'none';
//             }, 300);
//         }
//     });
// });

  
function showAdminModal() {
    const modal = document.getElementById('general-users-mod');
    modal.style.display = 'block'; 
}

function hideAdminModal() {
    const modal = document.getElementById('general-users-mod');
    modal.style.display = 'none'; 
}
  
// document.addEventListener("DOMContentLoaded", function () {});
const userIcons = document.querySelectorAll(".board-users-dropdown-item");
const profileModal = document.querySelector(".profile-modal-overlay");
const closeModalBtn = document.getElementById("close-user-profile");

const profileImage = profileModal.querySelector(".board-user-profile");
const boardUser = profileModal.querySelector(".board-user-name");
const boardUserEmail = profileModal.querySelector(".board-user-email");
const userDescription = profileModal.querySelector(".board-user-description");
const facebook = profileModal.querySelector('.board-user-facebook');
const linkedin = profileModal.querySelector('.board-user-linkedin');
const twitter = profileModal.querySelector('.board-user-twitter');

userIcons.forEach(user => {
    user.addEventListener("click", () => {
        console.log("wenttt hereee fuckkingignig")
        const image = user.dataset.image;
        const firstName = user.dataset.firstName;
        const lastName = user.dataset.lastName;
        const name = user.dataset.userName;
        const email = user.dataset.email;
        const description = user.dataset.description;
        const fbLink = user.dataset.facebook;
        const linkedinLink = user.dataset.linkedin;
        const twitterLink = user.dataset.twitter;
        console.log({ name, email, description, fbLink, linkedinLink, twitterLink });

        if (image) {
            profileImage.style.backgroundImage = `url(${image})`;
            profileImage.style.backgroundSize = "cover";
            profileImage.style.backgroundPosition = "center";
            profileImage.textContent = "";
        } else {
            profileImage.textContent = name ? (firstName.charAt(0) + lastName.charAt(0)) : "?"; // Fallback to initials
            profileImage.style.backgroundImage = ""; // Remove any background image
        }

        boardUser.textContent = name || "Unknown User";
        boardUserEmail.textContent = email || "No email provided";
        userDescription.textContent = description && description !== "None" ? description : "No description available";

        facebook.href = fbLink && fbLink !== "None" ? fbLink : "#";
        linkedin.href = linkedinLink && linkedinLink !== "None" ? linkedinLink : "#";
        twitter.href = twitterLink && twitterLink !== "None" ? twitterLink : "#";

        // Hide the social link elements if the link is invalid
        facebook.style.display = fbLink && fbLink !== "None" ? "block" : "none";
        linkedin.style.display = linkedinLink && linkedinLink !== "None" ? "block" : "none";
        twitter.style.display = twitterLink && twitterLink !== "None" ? "block" : "none";

        
        profileModal.classList.remove("disappear");
        profileModal.style.display = "flex";
        profileModal.classList.add("appear");
    });
});

closeModalBtn.addEventListener("click", () => {
    profileModal.classList.remove('appear');
    profileModal.classList.add('disappear');
    setTimeout(() => {
        profileModal.style.display = 'none';
    }, 300);
});
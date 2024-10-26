// Initialize zoom level
let zoomLevel = 1;  // 100% zoom

// Get board container
const boardContainer = document.querySelector('.board-container');

// Get zoom buttons
const zoomInBtn = document.querySelector('.zoom-in-btn');
const zoomOutBtn = document.querySelector('.zoom-out-btn');
const zoomDisplay = document.querySelector('.zoom-display');

// Function to update zoom
function updateZoom() {
    const baseGridSize = 20;  // Set the base size of the grid for 100% zoom

    // Set transform scale for zooming
    boardContainer.style.transform = `scale(${zoomLevel})`;

    // Adjust the background size dynamically based on zoom level
    boardContainer.style.backgroundSize = `${baseGridSize / zoomLevel}px ${baseGridSize / zoomLevel}px`;

    // Get current scroll position and adjust transform origin for centered zoom
    const boardRect = boardContainer.getBoundingClientRect();
    const centerX = boardRect.width / 2;
    const centerY = boardRect.height / 2;
    const scrollLeft = window.scrollX + centerX;
    const scrollTop = window.scrollY + centerY;

    // Adjust the transform origin to ensure the zoom is centered on the screen
    boardContainer.style.transformOrigin = `${scrollLeft}px ${scrollTop}px`;

    // Update zoom display percentage
    zoomDisplay.textContent = `${Math.round(zoomLevel * 100)}%`;
}



// Zoom In Button Click Event
zoomInBtn.addEventListener('click', function() {
    if (zoomLevel < 2) {  // Limit zoom-in to 200%
        zoomLevel += 0.1;
        updateZoom();
    }
});

// Zoom Out Button Click Event
zoomOutBtn.addEventListener('click', function() {
    if (zoomLevel > 0.5) {  // Limit zoom-out to 50%
        zoomLevel -= 0.1;
        updateZoom();
    }
});

// Initial zoom update
updateZoom();

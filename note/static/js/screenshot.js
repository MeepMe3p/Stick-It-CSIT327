// function captureScreenshot(boardId) {
//     const boardElement = document.getElementById(boardId);
    
//     html2canvas(boardElement).then((canvas) => {
//         const imageUrl = canvas.toDataURL("image/png");

//         // const previewContainer = document.getElementById('screenshot-preview');
//         // previewContainer.innerHTML = `<img src="${imageUrl}" alt="Board Screenshot" style="max-width: 100%;"/>`;

//         uploadScreenshot(imageUrl);
//     }).catch((err) => {
//         console.error("Error capturing screenshot:", err);
//     });
// }

// function uploadScreenshot(imageData, boardId) {
//     fetch('/save-screenshot/', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': '{{ csrf_token }}' 
//         },
//         body: JSON.stringify({ screenshot: imageData, board_id: boardId })
//     }).then(response => {
//         if (response.ok) {
//             console.log("Screenshot saved successfully.");
//         } else {
//             console.error("Failed to save screenshot.");
//         }
//     });
// }
let color = document.getElementById('color');
let createBtn = document.getElementById('createBtn');
let list = document.getElementById('list');
// let last_note;
// let last_note_id;
let cursor = {
    x: null,
    y: null
}
let note = {
    dom: null,
    x: null,
    y: null
}

// I GIVE UP ADMIRE LAAAAANG WOHOO
// DJANGO CHANNELS
// Determine the WebSocket protocol based on the application's URL
const websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";
const wsEndpoint = `${websocketProtocol}://${window.location.host}/ws/board_${noteBoardName}/`;

// Create a new WebSocket connection
const socket = new WebSocket(wsEndpoint);

// Successful connection event
socket.onopen = (event) => {
    console.log("WebSocket connection opened!");
};

// Socket disconnect event
socket.onclose = (event) => {
    console.log("WebSocket connection closed!");
};
// DJANGO CHANNELS
// I GIVE UP ADMIRE LAAAAANG WOHOO
function channel_handler(note, state){
    console.log(note)
    socket.send(
        JSON.stringify({
            state : state,
            note : {
                id : note.dataset.id,
                content: note.querySelector('textarea').value,
                borderColor: note.style.borderColor,
                coordinates: { x: note.style.left, y: note.style.top },
                is_finished : note.querySelector('.custom-checkbox-container').querySelector('.btn-check').checked, // Added
                checkbox_id : note.querySelector('.btn-check').id
            }
        }),
    );
}
// open: Fired when the connection to the server is established.
// message: Fired when a message is received from the server.
// error: Fired when there is an error with the WebSocket connection.
// close: Fired when the connection is closed.
// Response from consumer on the server
socket.addEventListener("message", (event) => {
    let response_data = JSON.parse(event.data);
    console.log(response_data.state)
    let state = response_data.state
    let note
    switch(state){
        case "create":
            note = JSON.parse(response_data.note)[0]
            notes_creation({
                id : note.pk,
                ... note.fields
            })
            break
        case "move":
            note = response_data.note
            // note.dom.style.left = (note.x + distance.x) + 'px';
            // note.dom.style.top = (note.y + distance.y) + 'px';
            console.log(note)
            console.log("MOVE! ",document.querySelector(`div[data-id='${note.id}']`))
            document.querySelector(`div[data-id='${note.id}']`).style.left = note.coordinates.x
            document.querySelector(`div[data-id='${note.id}']`).style.top = note.coordinates.y
            break
        case "delete":
            note = response_data.note
            // event.target.parentNode.remove();
            console.log(document.querySelector(`div[data-id='${note.id}']`))
            document.querySelector(`div[data-id='${note.id}']`).remove()
            break
        case "input":
            note = response_data.note
            // console.log("Input: ", document.querySelector(`div[data-id='${note.id}']`).querySelector('textarea'))
            console.log("Textarea: ", note.content)
            document.querySelector(`div[data-id='${note.id}']`).querySelector('textarea').value = note.content
            break
    }

});

// https://stackoverflow.com/questions/105034/how-do-i-create-a-guid-uuid
function uuidv4() {
    return "10000000-1000-4000-8000-100000000000".replace(/[018]/g, c =>
      (+c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> +c / 4).toString(16)
    );
  }
createBtn.onclick = () => {
    // Count the number of existing blank notes
    let blankNotesCount = 0;
    list.querySelectorAll('.note').forEach(note => {
        let content = note.querySelector('textarea').value;
        if (content.trim() === '') {
            blankNotesCount++;
        }
    });

    // If more than 2 blank notes exist, display the alert and block new note creation
    if (blankNotesCount >= 2) {
        Swal.fire("Please fill the first two notes!");
        return;  // Stop the creation of a new note
    }
    let newNote = document.createElement('div');
    newNote.classList.add('note');
    let id = uuidv4();
    newNote.innerHTML = `
    <span class="close">x</span>
    <textarea class="ckeditor" placeholder="Write Content..." rows="10" cols="30"></textarea>
    <div class="custom-checkbox-container">
        <input type="checkbox" class="btn-check" id="${id}" checked autocomplete="off">
        <label class="btn btn-outline-secondary" for="${id}">&#10003;</label><br>
    </div>
    `;
    newNote.style.borderColor = color.value;

    console.log(newNote.querySelector('.custom-checkbox-container').querySelector('.btn-check').checked)
    // list.appendChild(newNote)
    channel_handler(newNote, 'create')
    //  create a note in database with Ajax and use "GET" to get the new created note
    // fetch('/note/save_note/',{
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': csrftoken,
    //     },
        // body: JSON.stringify({
        //     content: newNote.querySelector('textarea').value,
        //     borderColor: color.value,
        //     coordinates: { x: newNote.style.left, y: newNote.style.top },
        //     is_finished : newNote.querySelector('.custom-checkbox-container').querySelector('.btn-check').checked, // Added
        //     checkbox_id :id
        // }),
    // })
    // .then(response => {
    //     if (!response.ok) { // Check if the response is OK (status 200-299)
    //         // window.location.reload(1);
    //         throw new Error('Network response was not ok');
    //     }
    //     return response.json(); 
    // })
    // .then(data => {
    //     console.log('New note created with ID:', data.id); // This should now work
    //     newNote.dataset.id = data.id; // Store the ID in the dataset
    //     // last_note_id = newNote.dataset.id;
    //     // newNote.querySelector('textarea').setAttribute("onblur", `saveOnInput(event, ${newNote.dataset.id})`)
    //     newNote.querySelector('textarea').setAttribute("oninput", `saveOnInput(event, ${newNote.dataset.id})`)
    //     // newNote.setAttribute("onblur", `saveOnInput(event, ${newNote.dataset.id})`)
    //     // console.log(data); // Log the entire response data
        
    //     const checkBox = newNote.querySelector(".custom-checkbox-container").querySelector(".btn-check")
    //     const textArea = newNote.querySelector('textarea')
    //     checkBox.checked = note.is_finished
    //     console.log(textArea)

    //     if(checkBox.checked){
    //         textArea.disabled = true;
    //     }
    //     // checkBox.addEventListener('change', function () {
    //     //     if (this.checked) {
    //     //         textArea.disabled = true; // Disable textarea if checkbox is checked
    //     //     } else {
    //     //         textArea.disabled = false; // Enable textarea if checkbox is unchecked
    //     //     }
    //     // });
    //     textArea.addEventListener('keydown', function(event){
    //         // console.log('Contraceptives', event)
    //         if(checkBox.checked){
    //             event.preventDefault()
    //         }
    //     })
    // })
    // .catch(error => console.error('Error:', error));
}
// When the button is clicked, a new <div> is created with the class note.
// Inside this <div>, a close button (<span class="close">) and a <textarea> for writing content are added.
// The border color of the note is set based on the selected color from the color input.
// Finally, the new note is appended to the list.

// IMPLEMENTED JUST TO KNOWLEDGE++
// CUTE KAAYU SIYA PAG ACQUAINTANCE! HUEHUEHUE MUST PROTEK!


// CAN'T ACCESS THE ID WHEN A NOTE IS LOADED!
document.addEventListener('click', (event) => {
    try {
        if(event.target.classList.contains('close')){
            const noteId = event.target.parentNode.dataset.id;
            fetch(`/note/delete_note/${noteId}/`,{
                method : 'DELETE',
                headers : {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrftoken,
                },
            }).then(response=>{
                if (response.ok) {
                    console.log(`Note with ID ${noteId} deleted successfully.`);
                    console.log(event.target.parentNode)
                    channel_handler(event.target.parentNode, 'delete')
                } else {
                    // window.location.reload(1);
                    console.error('Failed to delete note');
                }
            }).catch(error=>console.error('Error', error))
        }
        // last_note_id = event.target.dataset.id;
    } catch (error) {
        console.log("Clicked outside the note~  ")
    }
})

// CAN'T ACCESS THE ID WHEN A NOTE IS LOADED!
document.addEventListener('mousedown', (event) => {
    try {
        let identification = event.target.parentNode.querySelector(".btn-check").id;
        let checkbox = document.getElementById(identification);
    } catch (error) {
        console.log("Input Check Box Does Not Exist")
    }
    if(event.target.classList.contains('note')){
        cursor = {
            x: event.clientX,
            y: event.clientY
        }
        note = {
            dom: event.target,
            x: event.target.getBoundingClientRect().left,
            y: event.target.getBoundingClientRect().top
        }
        updateNote(event.target.dataset.id, event.target);
    }
})

document.addEventListener('mousemove', (event) => {
    if(note.dom == null) return;
    let currentCursor = {
        x: event.clientX,
        y: event.clientY
    }
    let distance = {
        x: currentCursor.x - cursor.x,
        y: currentCursor.y - cursor.y
    }
    note.dom.style.left = (note.x + distance.x) + 'px';
    note.dom.style.top = (note.y + distance.y) + 'px';
    note.dom.style.cursor = 'grab';
    let newY;
    let newX;
    list.querySelectorAll('.note').forEach(note => {
        if(event.target.dataset.id != note.dataset.id)
            if(isCollide(event.target, note)){
                let xNote = parseInt(note.style.left.replace('px', '')) || 0;
                let yNote = parseInt(note.style.top.replace('px', '')) || 0;
                let xEventNote = parseInt(event.target.style.left.replace('px', '')) || 0;
                let yEventNote = parseInt(event.target.style.top.replace('px', '')) || 0;
                // Determine if the collision is primarily vertical or horizontal
                const deltaX = Math.abs(xNote - xEventNote);
                const deltaY = Math.abs(yNote - yEventNote);

                if (deltaY > deltaX) {
                    // Vertical collision
                    if (yNote > yEventNote) {
                        newY = yNote + 15; // Move down
                    } else {
                        newY = yNote - 15; // Move up
                    }
                    newY = Math.max(0, newY); // Prevent negative Y
                    note.style.top = `${newY}px`; // Update y position
                } else {
                    // Horizontal collision
                    if (xNote > xEventNote) {
                        newX = xNote + 15; // Move right
                    } else {
                        newX = xNote - 15; // Move left
                    }
                    newX = Math.max(0, newX); // Prevent negative X
                    note.style.left = `${newX}px`; // Update x position
                }
                
                updateNote(event.target.dataset.id, event.target);
                updateNote(note.dataset.id, note);
            }
        channel_handler(note, 'move')
    });
})

// checkbox.addEventListener('change', (event) => {
//     // Check if the checkbox is checked or not
//     if (event.target.checked) {
//         console.log('Checkbox is checked!');
//     } else {
//         console.log('Checkbox is unchecked!');
//     }
// });

// document.querySelectorAll('textarea').forEach(textarea=>{
//     textarea.addEventListener('input', (event)=>{
//         console.log(event)
//     });
// })
let saveTimeout; // Variable to store the timeout
function saveOnInput(event, id){
    // console.log("Inside!")
    // console.log(event.returnValue)
    // console.log(event.target.parentNode.dataset.id)
    
    channel_handler(event.target.parentNode, 'input')
    // Clear the previous timeout if the user is still typing
    if (saveTimeout) {
        clearTimeout(saveTimeout);
    }
    saveTimeout = setTimeout(() => {
        // Perform the save operation here
        console.log("Saving data for ID:", id);
        // console.log("Note", event.target.parentNode);
        updateNote(id, event.target.parentNode);
    }, 3000); // 3 seconds delay
    // 
}
document.addEventListener('mouseup', (event) => {
    if( note.dom == null) return;
    note.dom.style.cursor = 'auto';
    note.dom = null;
    updateNote(event.target.dataset.id, event.target)
})
function updateNote(id, note){
    
    fetch(`/note/update_note/${id}/`, {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            content: note.querySelector('textarea').value,
            borderColor: note.querySelector('input[type="color"]'),
            coordinates: { x: note.style.left, y: note.style.top },
            is_finished : note.querySelector(".custom-checkbox-container").querySelector(".btn-check").checked // Added
        }),
    }).then(response => {
        if (!response.ok) { // Check if the response is OK (status 200-299)
            // window.location.reload(1);
            throw new Error('Network response was not ok');
        }
        return response.json(); // Populates the data below kay gwapa siya! muehuehue
    })
    .then(data => {
        console.log("update_note's Data! ", data); // Log the entire response data
        console.log("After: ", data.is_finished)
    })
    .catch(error => console.error('Error:', error));
}
// Function to get the CSRF token from the cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Check if this cookie string begins with the name we want
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Get the CSRF token
const csrftoken = getCookie('csrftoken');


window.onload = () => {
    fetch('/note/get_notes/', {
        method : 'GET',
    })
    .then(response => response.json())
    .then(notes => { 
        // let index = 0;
        // notes.forEach(note => {
        //     console.log(note, index);
        
        //     index++; // Increment the index
        // });
    notes.forEach(note => {
        notes_creation(note)
    });
})
.catch(error => console.error('Error fetching notes:', error));
};
function notes_creation(note){
    
    let newNote = document.createElement('div');
    // console.log(note.is_finished)
    
    newNote.classList.add('note');
    newNote.style.borderColor = note.border_color;
    newNote.style.position = 'absolute'; // Make sure to set position for coordinates
    newNote.style.left = note.coordinates.x; // Set the x position
    newNote.style.top = note.coordinates.y; // Set the y position
    newNote.innerHTML = `
    
    <span class="close" style="border-color: ${note.border_color};">x</span>
    <textarea class="ckeditor" placeholder="Write Content..." rows="10" cols="30">${note.content}</textarea>
    <div class="custom-checkbox-container">
        <input type="checkbox" class="btn-check" id="${note.checkbox_id}" checked autocomplete="off">
        <label class="btn btn-outline-secondary" for="${note.checkbox_id}">&#10003;</label><br>
    </div>
    `;
    const checkBox = newNote.querySelector(".custom-checkbox-container").querySelector(".btn-check")
    const textArea = newNote.querySelector('textarea')
    checkBox.checked = note.is_finished
    // console.log(textArea)

    // if(checkBox.checked){
    //     textArea.disabled = true;
    // }
    // checkBox.addEventListener('change', function () {
    //     if (this.checked) {
    //         // textArea.disabled = true; // Disable textarea if checkbox is checked
    //     } else {
    //         // textArea.disabled = false; // Enable textarea if checkbox is unchecked
    //     }
    // });
    textArea.addEventListener('keydown', function(event){
        // console.log('Contraceptives', event)
        if(checkBox.checked){
            event.preventDefault()
        }
    })
    newNote.dataset.id = note.id;
    newNote.querySelector('textarea').setAttribute("oninput", `saveOnInput(event, ${newNote.dataset.id})`)  
    list.appendChild(newNote);
}
// setTimeout(function(){
//     window.location.reload(1);
//  }, 5000);

function isCollide(a, b) {
    const rect1 = a.getBoundingClientRect();
    const rect2 = b.getBoundingClientRect();
    // console.log("A Rect!", rect1)
    // console.log("B Rect!", rect2)
    return !(
        rect1.right < rect2.left ||  // right side of el1 is left of el2
        rect1.left > rect2.right ||  // left side of el1 is right of el2
        rect1.bottom < rect2.top ||  // bottom of el1 is above el2
        rect1.top > rect2.bottom     // top of el1 is below el2
      );
}
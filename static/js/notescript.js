let color = document.getElementById('color');
let createBtn = document.getElementById('createBtn');
let list = document.getElementById('list');
let last_note;
let last_note_id;
 
// TODO!
// FIRST: ADD boolean is_finished (update model) and design
// SECOND: Dynamic Canvas
// THIRD: Realtime "Get"

// color: Refers to an input element (presumably a color picker) that allows the user to choose a color for the note's border.
// createBtn: Refers to a button that, when clicked, creates a new note.
// list: Refers to a container (like a <div> or <ul>) where the created notes will be appended.
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
        let alertBox = document.createElement('div');
        alertBox.classList.add('alert');
        
        alertBox.innerHTML = `
        <div class="alert">
            <span class="fas fa-exclamation-circle"></span>
            <span class="msg">Warning: This is a warning alert!</span>
            <span class="close-btn">
                <span class="fas fa-times"></span>
            </span>
        </div>
        `;

        document.body.appendChild(alertBox);  // Add the alert to the body or a specific container

        // Add event listener to close the alert when the close button is clicked
        alertBox.querySelector('.close-btn').onclick = function() {
            alertBox.remove();
        };

        return;  // Stop the creation of a new note
    }
    let newNote = document.createElement('div');
    newNote.classList.add('note');
    newNote.innerHTML = `
    <input type="checkbox" class="btn-check" id="btn-check-2-outlined" checked autocomplete="off">
    <span class="close">x</span>
    <textarea placeholder="Write Content..." rows="10" cols="30"></textarea>`;
    newNote.style.borderColor = color.value;
    console.log(newNote.querySelector('#btn-check-2-outlined').checked)
    list.appendChild(newNote)
    //  create a note in database with Ajax and use "GET" to get the new created note
    fetch('/note/save_note/',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            content: newNote.querySelector('textarea').value,
            borderColor: color.value,
            coordinates: { x: newNote.style.left, y: newNote.style.top },
            is_finished : newNote.querySelector('#btn-check-2-outlined').checked // Added
        }),
    }).then(response => {
        if (!response.ok) { // Check if the response is OK (status 200-299)
            // window.location.reload(1);
            throw new Error('Network response was not ok');
        }
        return response.json(); 
    })
    .then(data => {
        console.log('New note created with ID:', data.id); // This should now work
        newNote.dataset.id = data.id; // Store the ID in the dataset
        last_note_id = newNote.dataset.id;

        // console.log(data); // Log the entire response data
    })
    .catch(error => console.error('Error:', error));
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
        last_note_id = event.target.parentNode.dataset.id;
        if(event.target.classList.contains('close')){
            // console.log("Parent", event.target.parentNode)
            // console.log("Target", event.target)
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
                    event.target.parentNode.remove();
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

let cursor = {
    x: null,
    y: null
}
let note = {
    dom: null,
    x: null,
    y: null
}

// CAN'T ACCESS THE ID WHEN A NOTE IS LOADED!
document.addEventListener('mousedown', (event) => {
    if(event.target.checked) console.log("Before: ", event.target.checked)
    // console.log("Parent ", event.target.parentNode)
    if(event.target.classList.contains('note')){
        // last_note_id = event.target.querySelector('span').dataset.id;
        // console.log(last_note_id);
        // console.log(event.target.querySelector('span').dataset.id);
        cursor = {
            x: event.clientX,
            y: event.clientY
        }
        note = {
            dom: event.target,
            x: event.target.getBoundingClientRect().left,
            y: event.target.getBoundingClientRect().top
        }


    last_note = event.target;
    // if(event.target.querySelector('span').dataset.id != null)
    //     last_note_id = event.target.dataset.id;
}
})

// CAN'T ACCESS THE ID WHEN A NOTE IS LOADED!
document.addEventListener('mousemove', (event) => {
    if(note.dom == null) return;
    // last_note_id = event.target.querySelector('span').dataset.id;
    // console.log("mousemove")
    // console.log(event.target.querySelector('span').dataset.id)
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

    last_note = event.target;
    // if(event.target.querySelector('span').dataset.id != null)
})

document.addEventListener('mouseup', (event) => {
    // console.log(event.target)
    if( note.dom == null) return;
    note.dom.style.cursor = 'auto';
    note.dom = null;

    fetch(`/note/update_note/${event.target.dataset.id}/`, {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            content: last_note.querySelector('textarea').value,
            borderColor: last_note.querySelector('input[type="color"]'),
            coordinates: { x: last_note.style.left, y: last_note.style.top },
            is_finished : last_note.querySelector('#btn-check-2-outlined').checked // Added
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
})

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
        let index = 0;
        // notes.forEach(note => {
        //     console.log(note, index);
        
        //     index++; // Increment the index
        // });
    notes.forEach(note => {
        let newNote = document.createElement('div');
        console.log(note.coordinates.x)
        
        newNote.classList.add('note');
        newNote.style.borderColor = note.border_color;
        // newNote.style.position = 'absolute'; // Make sure to set position for coordinates
        newNote.style.left = note.coordinates.x; // Set the x position
        newNote.style.top = note.coordinates.y; // Set the y position
        newNote.innerHTML = `
        <input type="checkbox" class="btn-check" id="btn-check-2-outlined" checked autocomplete="off">
        <span class="close" style="border-color: ${note.border_color};">x</span>
        <textarea placeholder="Write Content..." rows="10" cols="30">${note.content}</textarea>`;
        // Test Check and Uncheck
        // newNote.querySelector('#btn-check-2-outlined').checked = false;
        console.log(newNote.querySelector('#btn-check-2-outlined').checked);
        newNote.dataset.id = note.id;
        list.appendChild(newNote);
        index++;
    });
})
.catch(error => console.error('Error fetching notes:', error));
};

// setTimeout(function(){
//     window.location.reload(1);
//  }, 5000);
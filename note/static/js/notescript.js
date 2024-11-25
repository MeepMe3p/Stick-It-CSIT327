let color = document.getElementById('color');
let createBtn = document.getElementById('createBtn');
let list = document.getElementById('list');
let last_note;
let last_note_id;
// color: Refers to an input element (presumably a color picker) that allows the user to choose a color for the note's border.
// createBtn: Refers to a button that, when clicked, creates a new note.
// list: Refers to a container (like a <div> or <ul>) where the created notes will be appended.
createBtn.onclick = () => {
    let newNote = document.createElement('div');
    newNote.classList.add('note');
    newNote.innerHTML = `
    <span class="close">x</span>
    <textarea placeholder="Write Content..." rows="10" cols="30"></textarea>
    <div class="custom-checkbox-container">
        <input type="checkbox" class="btn-check" id="${id}" checked autocomplete="off">
        <label id="note-btn-style" class="btn btn-outline-secondary" for="${id}">&#10003;</label><br>
    </div>
    `;
    newNote.style.borderColor = color.value;
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
            coordinates: { x: newNote.style.left, y: newNote.style.top }
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

        console.log(data); // Log the entire response data
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
    last_note_id = event.target.parentNode.dataset.id;
    if(event.target.classList.contains('close')){
        console.log("Parent", event.target.parentNode)
        console.log("Target", event.target)
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
    if(event.target.classList.contains('note')){
        // last_note_id = event.target.querySelector('span').dataset.id;
        console.log(last_note_id);
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
    console.log("mousemove")
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
    console.log(event.target)
    if( note.dom == null) return;
    note.dom.style.cursor = 'auto';
    note.dom = null;
    // get the ID of the newnote and store in the database the newNote.innerHTML as a string when the mouse is "up" using the id
    // AND THE X AND Y COORDINATES!
    // QUESTION! does it store the typed "Content"
    // the lofic should be inside a fuunction which whould be called inside here to function? or not not needed?
    // Questiion! is the newNote.innerHTML the whole? like including design or no???

    // // Assuming last_note is the reference to the note element you want to access
    // console.log(last_note); // Logs the entire note element
    // console.log(last_note.querySelector('textarea').value); // Accesses the textarea value
    // // Accesses the left and top style properties
    // console.log(last_note.style.left); // Logs the left position
    // console.log(last_note.style.top); // Logs the top position
    // console.log(last_note_id); // Accesses the data-id attribute
    // // To access the border color from the style
    // console.log(last_note.style.borderColor); // Logs the border color

    fetch(`/note/update_note/${event.target.dataset.id}/`, {
        method : 'POST',
        headers : {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            content: last_note.querySelector('textarea').value,
            borderColor: last_note.querySelector('input[type="color"]'),
            coordinates: { x: last_note.style.left, y: last_note.style.top }
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
    console.log("HMM?")
    fetch('/note/get_notes/', {
        method : 'GET',
    })
    
    .then(response => {
        console.log('Response status:', response);  // Check if the status is OK
        console.log('Response status:', response.json);  // Check if the status is OK
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        return response.json();
    })
    .then(notes => { 
        console.log("wrnt hereeeeeee")
        // let index = 0;
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
        <span class="close" style="border-color: ${note.border_color};">x</span>
        <textarea placeholder="Write Content..." rows="10" cols="30">${note.content}</textarea>`;
        newNote.dataset.id = note.id;
        list.appendChild(newNote);
        index++;
    });
})
.catch(error => console.error('Error fetching notes:', error));
};
function notes_creation(note){
    
    let newNote = document.createElement('div');
    // console.log(note.is_finished)
    
    console.log("nipasok ka diri");

    newNote.classList.add('note');
    newNote.style.borderColor = note.border_color;
    newNote.style.position = 'absolute'; // Make sure to set position for coordinates
    newNote.style.left = note.coordinates.x; // Set the x position
    newNote.style.top = note.coordinates.y; // Set the y position
    newNote.innerHTML = `
    
    
    <span class="close" style="border-color: ${note.border_color};">x</span>
    <textarea placeholder="Write Content..." rows="10" cols="30">${note.content}</textarea>
    <div class="custom-checkbox-container">
        <input type="checkbox" class="btn-check" id="${note.checkbox_id}" checked autocomplete="off">
        <label id="note-btn-style" class="btn btn-outline-secondary" for="${note.checkbox_id}">&#10003;</label><br>
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
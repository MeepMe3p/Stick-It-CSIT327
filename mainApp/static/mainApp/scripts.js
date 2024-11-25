let home_tab = document.querySelector('.home-tab');
let profile_tab = document.querySelector('.profile-tab');
let boards_tab = document.querySelector('.boards-tab');
let home_link = document.querySelector('.home-tab .tab-link');
let profile_link = document.querySelector('.profile-tab .tab-link');
let boards_link = document.querySelector('.boards-tab .tab-link');
let selectedEmails = []; 

const profileInitialValues = {};
const socialInitialValues = {};
const profile_inputs = document.querySelectorAll('.profile-input');
const social_links_inputs = document.querySelectorAll('.socials-input');
const updateP1Btn = document.getElementById('p1-update-btn');
const updateP2Btn = document.getElementById('p2-update-btn');

window.onload = function() {
    const path = window.location.pathname;

    if (path.includes('/home')) {
        home_tab.classList.add('selected');
        home_link.style.color = 'white';
        profile_tab.classList.remove('selected');
        profile_link.style.color = 'black';
        boards_tab.classList.remove('selected');
        boards_link.style.color = 'black';
    } else if (path.includes('/profile')) {
        profile_tab.classList.add('selected');
        profile_link.style.color = 'white';
        home_tab.classList.remove('selected');
        home_link.style.color = 'black';
        boards_tab.classList.remove('selected');
        boards_link.style.color = 'black';
    } else if (path.includes('/my_boards')) {
        boards_tab.classList.add('selected');
        boards_link.style.color = 'white';
        home_tab.classList.remove('selected');
        home_link.style.color = 'black';
        profile_tab.classList.remove('selected');
        profile_link.style.color = 'black';
    }
};

// Arrow rotation in User Icon Click
function profileClickDropwdownFunction() {
    const dropdownMenu = document.getElementById('dropdown-menu');
    const user_icon_arrow = document.querySelector('.dropdown-arrow-main-header');
    // document.querySelector('.m5-user-icon-header-flex').classList.toggle('active');
    if (user_icon_arrow.style.transform === 'rotate(180deg)') {
        user_icon_arrow.style.transform = 'rotate(0deg)';
    } else {
        user_icon_arrow.style.transform = 'rotate(180deg)';
    }
    
    dropdownMenu.classList.toggle('show');
}

window.addEventListener('click', function (event) {
    const userIcon = document.getElementById('user-icon');
    const dropdownMenu = document.getElementById('dropdown-menu');
    
    if (!userIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.classList.remove('show');

        const user_icon_arrow = document.querySelector('.dropdown-arrow-main-header');
        user_icon_arrow.style.transform = 'rotate(0deg)';
    }
});

// Open Create Board Modal 
function openModal() {
    document.getElementById('createBoardModal').style.display = 'flex'; 
}

function closeModal() {
    document.getElementById('createBoardModal').style.display = 'none'; 
}

// 'No Access Permission' Popup
function openPermissionModal() {
    document.getElementById('permissionModal').style.display = 'flex'; 
}

function closePermissionModal() {
    document.getElementById('permissionModal').style.display = 'none'; 
}

window.onclick = function(event) {
    const modal = document.getElementById('permissionModal');
    if (event.target === modal) {
        closePermissionModal();
    }
}

// Create Board Modal Section
function handleCategoryChange() {
    const categorySelect = document.getElementById('category');
    const newCategoryInput = document.getElementById('new-category');
    
    if (categorySelect.value === 'create-new') {
        // categorySelect.get
        newCategoryInput.style.display = 'block';
        newCategoryInput.focus();
    } else {
        newCategoryInput.style.display = 'none';
        newCategoryInput.value = ''; 
    }
}


function toggleDropdown() {
    const dropdownContent = document.getElementById('dropdown-content');
    dropdownContent.style.display = dropdownContent.style.display === 'block' ? 'none' : 'block';
}

function selectUser(email) {
    if (!selectedEmails.includes(email)) {
        selectedEmails.push(email); 
        updateSelectedEmailsDisplay();
    }
}

function updateSelectedEmailsDisplay() {
    const dropdown = document.querySelector('.dropdown');
    const container = document.getElementById('selected-emails-container');
    container.innerHTML = ''; // Clear previous hidden inputs

    // Update displayed text in the dropdown
    dropdown.textContent = "Selected: " + selectedEmails.join(", ");

    // Add hidden inputs for each selected email
    selectedEmails.forEach((email, index) => {
        const input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'selected_emails[]'; // Make the name an array
        input.value = email;
        container.appendChild(input);
    });
}

window.onclick = function(event) {
    if (!event.target.matches('.dropdown')) {
        const dropdowns = document.getElementsByClassName("dropdown-content");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.style.display === 'block') {
                openDropdown.style.display = 'none';
            }
        }
    }
}

// Store initial values of the profile inputs and bio
profile_inputs.forEach(input => {
    profileInitialValues[input.id] = input.value;
});

// Function to check if any value has changed, enable, and highlight the Update button in the Profile Details section
function checkForProfileChanges() {
    let hasChanged = false;

    profile_inputs.forEach(input => {
        if (input.value !== profileInitialValues[input.id]) {
            hasChanged = true;
        }
    });

    if (hasChanged) {
        updateP1Btn.disabled = false;
        updateP1Btn.classList.add('highlight');
    } else {
        updateP1Btn.disabled = true;
        updateP1Btn.classList.remove('highlight');
    }
}

profile_inputs.forEach(input => {
    input.addEventListener('input', checkForProfileChanges);
});


// Store initial values of the inputs and bio
social_links_inputs.forEach(input => {
    socialInitialValues[input.id] = input.value;
});

// Function to check if any value has changed, and enable and highlight the Update button in the Social Profile Details section
function checkForSocialProfileChanges() {
    let hasChanged = false;

    social_links_inputs.forEach(input => {
        if (input.value !== socialInitialValues[input.id]) {
            hasChanged = true;
        }
    });

    if (hasChanged) {
        updateP2Btn.disabled = false;
        updateP2Btn.classList.add('highlight');
    } else {
        updateP2Btn.disabled = true;
        updateP2Btn.classList.remove('highlight');
    }
}

social_links_inputs.forEach(input => {
    input.addEventListener('input', checkForSocialProfileChanges);
});
let home_tab = document.querySelector('.home-tab');
let profile_tab = document.querySelector('.profile-tab');
let boards_tab = document.querySelector('.boards-tab');
let home_link = document.querySelector('.home-tab .tab-link');
let profile_link = document.querySelector('.profile-tab .tab-link');
let boards_link = document.querySelector('.boards-tab .tab-link');
let selectedEmails = []; 
let simple_boards = document.querySelector('.simple-boards-list');
let project_boards = document.querySelector('.project-boards-list');
let main_board_list = document.querySelector('.main-board-list');
let user_brds_btn = document.querySelector('.user-boards-sect');
let shared_brds_btn = document.querySelector('.shared-boards-sect');
let joined_brds_btn = document.querySelector('.joined-boards-sect');
let close_settings = document.getElementById('close-settings-btn');
let open_settings = document.querySelector('.account-settings');
let brd_options = document.querySelector('.more-options');
let profileInitialValues = {};
let socialInitialValues = {};
let profile_inputs = document.querySelectorAll('.profile-input');
let social_links_inputs = document.querySelectorAll('.socials-input');
let updateP1Btn = document.getElementById('p1-update-btn');
let updateP2Btn = document.getElementById('p2-update-btn');

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
        user_brds_btn.classList.add('active');
        shared_brds_btn.classList.remove('active');
    } else if (path.includes('/collaborated_boards')) {
        boards_tab.classList.add('selected');
        boards_link.style.color = 'white';
        home_tab.classList.remove('selected');
        home_link.style.color = 'black';
        profile_tab.classList.remove('selected');
        profile_link.style.color = 'black';
        user_brds_btn.classList.remove('active');
        shared_brds_btn.classList.add('active');
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

brd_options.onclick = function() {
    const boardDropdown = document.getElementById('board-mod-options');
    boardDropdown.classList.toggle('show');
}

window.addEventListener('click', function (event) {
    const userIcon = document.getElementById('user-icon');
    const dropdownMenu = document.getElementById('dropdown-menu');

    const options = document.querySelector('.more-options');
    const boardDropdown = document.getElementById('board-mod-options');
    
    if (!userIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.classList.remove('show');

        const user_icon_arrow = document.querySelector('.dropdown-arrow-main-header');
        user_icon_arrow.style.transform = 'rotate(0deg)';
    }

    if (!options.contains(event.target) && !boardDropdown.contains(event.target)) {
        boardDropdown.classList.remove('show');
    }
});

// Open Create Board Modal 
function openModal() {
    const overlay = document.getElementById('createBoardModal');
    overlay.classList.remove('disappear');
    overlay.classList.add('appear');
    overlay.style.display = 'flex';
}

function closeModal() {
    const overlay = document.getElementById('createBoardModal');
    overlay.classList.remove('appear');
    overlay.classList.add('disappear');
    setTimeout(() => {
        overlay.style.display = 'none';
    }, 300);
}

// 'No Access Permission' Popup
function openPermissionModal() {
    document.getElementById('permissionModal').style.display = 'flex'; 
}

function closePermissionModal() {
    document.getElementById('permissionModal').style.display = 'none'; 
}

open_settings.onclick = function() {
    const overlay = document.querySelector('.as-m-overlay');
    overlay.classList.remove('disappear');
    overlay.classList.add('appear');
    overlay.style.display = 'flex';
}

close_settings.onclick = function() {
    const overlay = document.querySelector('.as-m-overlay');
    overlay.classList.remove('appear');
    overlay.classList.add('disappear');
    setTimeout(() => {
        overlay.style.display = 'none';
    }, 300);
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


//Filter boards in Home Page by Board Type
function handleBoardTypeChange(selectElement) {
    const selectedValue = selectElement.value;

    if (selectedValue === "all") {
        clickMainBoardListFilter();
    } else if (selectedValue === "simple") {
        clickSimpleBoardFilter();
    } else if (selectedValue === "project") {
        clickProjectBoardFilter();
    }
}

function clickSimpleBoardFilter() {
    simple_boards.style.display = 'flex';
    main_board_list.style.display = 'none';
    project_boards.style.display = 'none';
}

function clickProjectBoardFilter() {
    simple_boards.style.display = 'none';
    main_board_list.style.display = 'none';
    project_boards.style.display = 'flex';
}

function clickMainBoardListFilter() {
    simple_boards.style.display = 'none';
    main_board_list.style.display = 'flex';
    project_boards.style.display = 'none';
}

document.addEventListener("DOMContentLoaded", function () {
    // Get all board previews and modal elements
    const boardPreviews = document.querySelectorAll(".board-preview");
    const modal = document.querySelector(".board-modal");
    const closeModalBtn = document.getElementById("close-board-detail");

    // Modal content elements
    const modalTitle = modal.querySelector(".board-title");
    const modalDescription = modal.querySelector(".board-description");
    const modalCategory = modal.querySelector(".category-button");
    const modalCreator = modal.querySelector(".creator-name");
    const viewBoard = modal.querySelector('.view-board-link');
    // const modalOtherUsers = modal.querySelector(".other-users");

    boardPreviews.forEach(preview => {
        preview.addEventListener("click", () => {
            const boardId = preview.dataset.boardId;
            const boardName = preview.dataset.boardName;
            const description = preview.dataset.description;
            const category = preview.dataset.category;
            const creator = preview.dataset.creator;
            // const otherUsers = preview.dataset.otherUsers;

            modal.classList.remove("disappear");
            modal.style.display = "flex";

            modalTitle.textContent = boardName;
            modalDescription.textContent = description;
            modalCategory.textContent = category;
            modalCreator.textContent = `Created by ${creator}`;
            // modalOtherUsers.textContent = `${otherUsers} other users on board`;
            viewBoard.href = `/board/board_view/${boardId}/`;
            
            modal.classList.add("appear");
        });
    });

    // Close modal functionality
    closeModalBtn.addEventListener("click", () => {
        modal.classList.remove('appear');
        modal.classList.add('disappear');
        setTimeout(() => {
            modal.style.display = 'none';
        }, 300);
    });
});
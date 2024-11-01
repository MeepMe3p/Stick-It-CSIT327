function myFunction() {
    const dropdownMenu = document.getElementById('dropdown-menu');
    dropdownMenu.classList.toggle('show');
}

window.addEventListener('click', function (event) {
    const userIcon = document.getElementById('user-icon');
    const dropdownMenu = document.getElementById('dropdown-menu');
    
    if (!userIcon.contains(event.target) && !dropdownMenu.contains(event.target)) {
        dropdownMenu.classList.remove('show');
    }
});


function openModal() {
    document.getElementById('createBoardModal').style.display = 'flex'; 
}

function closeModal() {
    document.getElementById('createBoardModal').style.display = 'none'; 
}


window.onclick = function(event) {
    const modal = document.getElementById('createBoardModal');
    if (event.target === modal) {
        closeModal();
    }
}


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



function openEditProfileModal() {
    // document.getElementsByClassName('about-me-modal')[0].style.display = 'flex';
    document.querySelector('.about-me-modal').style.display = 'flex';
    // document.getElementById('editProfileModal').style.display = 'flex';
}

function closeEditProfileModal() {
    document.querySelector('.about-me-modal').style.display = 'none';
    // document.getElementById('editProfileModal').style.display = 'none';
}

function openEditSocialsModal() {
    document.querySelector('.social-links-modal').style.display = 'flex';
}

function closeEditSocialsModal() {
    document.querySelector('.social-links-modal').style.display = 'none';
}

// window.onclick = function(event) {
//     if (event.target.classList.contains('modal-overlay')) {
//         closeProfileViewModal();
//         closeEditProfileModal();
//     }
// }



// function showProfile() {
//     document.getElementById("profile-section").style.display = "block";
//     document.getElementById("my-boards-section").style.display = "none";
// }

// function showMyBoards() {
//     document.getElementById("my-boards-section").style.display = "block";
//     document.getElementById("profile-section").style.display = "none";
// }

// function showTab(tab) {
//     const tabs = document.querySelectorAll(".tab-content");
//     tabs.forEach(t => t.style.display = "none");
//     document.getElementById(tab).style.display = "block";
// }

// window.onclick = function(event) {
//     if (!event.target.matches('.user-icon')) {
//         var dropdowns = document.getElementsByClassName("dropdown-menu");
//         for (var i = 0; i < dropdowns.length; i++) {
//             var openDropdown = dropdowns[i];
//             if (openDropdown.classList.contains('show')) {
//                 openDropdown.classList.remove('show');
//             }
//         }
//     }
// }


function showProfile() {
    document.getElementById('profile-section').style.display = 'block';
    document.getElementById('my-boards-section').style.display = 'none';
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-btn')[0].classList.add('active');
}

function showMyBoards() {
    document.getElementById('profile-section').style.display = 'none';
    document.getElementById('my-boards-section').style.display = 'block';
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    document.querySelectorAll('.tab-btn')[1].classList.add('active');
}

// function showTab(tabId) {
//     document.querySelectorAll('.tab-content').forEach(tab => tab.style.display = 'none');
//     document.getElementById(tabId).style.display = 'block';
//     document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
//     document.querySelector(`[onclick="showTab('${tabId}')"]`).classList.add('active');
// }

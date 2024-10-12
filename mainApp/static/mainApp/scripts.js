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

// If clicked outside the content, close the modal overlay
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
        newCategoryInput.style.display = 'block';
        newCategoryInput.focus();
    } else {
        newCategoryInput.style.display = 'none';
        newCategoryInput.value = ''; 
    }
}

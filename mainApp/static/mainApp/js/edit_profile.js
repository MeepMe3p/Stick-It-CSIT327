


function openEditProfPicModal() {
    const ppModal = document.querySelector('.profile-pic-form-mod');
    ppModal.classList.remove('disappear');
    ppModal.classList.add('appear');
    ppModal.style.display = 'block';
}
function closeEditProfPicModal() {
    const ppModal = document.querySelector('.profile-pic-form-mod');
    ppModal.classList.remove('appear');
    ppModal.classList.add('disappear');
    setTimeout(() => {
        ppModal.style.display = 'none';
    }, 300);
}
function handleCategoryChange() {
    const categorySelect = document.getElementById('id_category');
    console.log(categorySelect+"safafasfa");
    const newCategoryInput = document.getElementById('new-category');
    const newDescInput = document.getElementById("new-desc");
     
    if (categorySelect.value === 'create-new') {
        newCategoryInput.style.display = 'block';
        newDescInput.style.display = 'block';
        newCategoryInput.focus();
        newDescInput.focus();
    } 
    else {
        newCategoryInput.style.display = 'none';
        newCategoryInput.value = ''; 
        newDescInput.style.display = 'none';
        newDescInput.value = ''; 
    }
}
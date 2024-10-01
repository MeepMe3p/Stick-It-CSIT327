// https://www.youtube.com/watch?v=C4fr3SCqgJQ&t=1364s
// https://www.youtube.com/watch?v=cuEtnrL9-H0
// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
// https://medium.com/@munyaokelvin/how-to-fetch-data-from-an-ajax-fetch-api-in-django-e825a329a36d
const form = document.getElementById('cat-form');
const board_catagories = document.getElementById('id_category')
const new_cat = document.getElementById('new-cat')
const pop_up = document.getElementById('popup-cat')
const body_sheesh = document.getElementById('body-sheesh')
const test_btn = document.getElementById('test_btn')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

console.log("hello worldssss")
console.log(csrf)
console.log(board_catagories)

form.addEventListener('submit', e => {
    e.preventDefault(); // to prevent the site from reloading
    const cat_name = document.getElementById('id_category_name');
    const cat_desc = document.getElementById('id_category_description')
    
    console.log(cat_desc.value)
    
    var url = "";
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'category_name': cat_name.value,
            'category_description': cat_desc.value,
        }) 
    })
    .then((response) => {
  
        return response.json(); // converts response to json
    })
    .then((data) => {
        console.log('data :', data);

        console.log("gana na please fak")
        fetch(url,{
            method : 'GET',
            headers: {
                'Content-Type': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        }).then((response)=>{
            return response.json();
        }).then((data)=>{
            console.log('data: ',data);
            // console.log(data.context) // https://www.w3schools.com/js/js_json_arrays.asp 
            console.log(data.context.at(-1))
            console.log(board_catagories)
            // https://stackoverflow.com/questions/29449828/adding-options-to-an-html-select-element

            // board_catagories.add(data.context.at(-1),1)
            var new_option = document.createElement("option");
            new_option.text = data.context.at(-1).category_name;
            new_option.value = data.context.at(-1).id;
            board_catagories.add(new_option,1)

            
        
        });
    });
    




});
// at csrf django doc
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');


console.log(board_catagories)
console.log(new_cat)
console.log(pop_up)
console.log(body_sheesh)
new_cat.addEventListener('click',e=>{
    console.log("im clicked")
    document.body.style.background = 'yellow'
    pop_up.style.display = 'block'

});




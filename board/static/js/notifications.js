console.log("Hello there");
//for le channels
const websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";
const wsEndpoint = `${websocketProtocol}://${window.location.host}/ws/notification/${loggedIn}/`;
const socket = new WebSocket(wsEndpoint)
console.log(wsEndpoint)
socket.onopen = (event) =>{
    console.log("Websocket abli")
}
socket.onmessage = (event)=>{
    console.log("a message received",event.data)
}
socket.onclose = (event) =>{
    console.log("Websocket sira")
}
document.getElementById('update-form').addEventListener('submit',function(event){
    event.preventDefault();

    const chosen_add_users = document.querySelectorAll('input[name="add_users"]:checked');
    const chosen_remove_users = document.querySelectorAll('input[name="remove_users"]:checked');
    const message_add = `You are inviteted by ${user} to join ${board_name}`;
    const message_removed = `You are removed in the board ${board_name}`;
    const added_users = Array.from(chosen_add_users).map(checkbox => checkbox.value);
    const removed_users = Array.from(chosen_remove_users).map(checkbox => checkbox.value);
    const selectedUserIds = [...added_users,...removed_users];

    const datetime = updateDate();

    console.log("ADDED",{added_users})
    console.log("REMOVED",{removed_users})
    console.log({board});
    socket.send(
        JSON.stringify({
            'message_add':message_add,
            'message_removed':message_removed,
            'sender':`${loggedIn}`,
            'receivers':selectedUserIds,
            "added":added_users,
            "removed":removed_users,
            'board':`${board}`,
            'time_sent':  datetime,
        })
    )
});

socket.addEventListener("message",(event)=>{
    const messageData = JSON.parse(event.data)
    console.log("went hereeeeee")
    console.log(messageData)
});
function updateDate(){
    const now = new Date();
    const datetime = now.toISOString();
    console.log(datetime);
    return datetime;
}
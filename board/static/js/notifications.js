console.log("Hello there");
//for le channels
const websocketProtocol = window.location.protocol === "https:" ? "wss" : "ws";
const wsEndpoint = `${websocketProtocol}://${window.location.host}/ws/notification/${loggedIn}/`;
const socket = new WebSocket(wsEndpoint)

socket.onopen = (event) =>{
    console.log("Websocket opened")
}

socket.onclose = (event) =>{
    console.log("Websocket closed")
}
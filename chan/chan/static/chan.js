socket = new WebSocket("ws://" + window.location.host + "/front/");
socket.onmessage = function(e) {
  console.log("Got response: ", e.data);
}

function log(msg) {
  var parent = document.getElementById("log");
  var p = document.createElement("p");
  p.appendChild(document.createTextNode(msg));
  parent.appendChild(p);
  parent.scrollTop = el.scrollHeight;
}

document.addEventListener("DOMContentLoaded", function(event) {
  log("Initialized; socket: " + socket);
});

socket = new WebSocket("ws://" + window.location.host + "/front/");
socket.onmessage = function(e) {
  log("Got response: " + e.data);
}

function log(msg) {
  var parent = document.getElementById("log");
  var p = document.createElement("p");
  p.appendChild(document.createTextNode(msg));
  parent.appendChild(p);
  parent.scrollTop = parent.scrollHeight;
}

function send_request () {
  var value = parseInt(document.getElementById("seconds").value) || 0;
  socket.send(JSON.stringify({'command': 'count_to',
                              'seconds': value}));
}

document.addEventListener("DOMContentLoaded", function(event) {
  log("Initialized; socket: " + socket);
});

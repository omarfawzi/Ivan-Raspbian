function init() {
    let websocket = new WebSocket('ws://localhost:9090/');
    websocket.onopen = function (evt) {
        onOpen(evt)
    };
    websocket.onclose = function (evt) {
        onClose(evt)
    };
    websocket.onmessage = function (evt) {
        onMessage(evt)
    };
    websocket.onerror = function (evt) {
        onError(evt)
    };
}

function onOpen(evt) {
    console.log('Connected ...')
}

function onClose(evt) {
    console.log("Disconnected ...");
}

function onMessage(evt) {
    console.log(evt.data)
    let message = $.parseJSON(evt.data);
    performAction(message);
}

function onError(evt) {
    console.log('error: ' + evt.data + '\n');
    websocket.close();
}

function doSend(message) {
    websocket.send(message);
}

window.addEventListener("load", init, false);
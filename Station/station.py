import json
from pynput.keyboard import Key, Listener, KeyCode
from websocket import create_connection

ws = create_connection("ws://localhost:9090/")

Current_Stop = 1
Destination_Stop = ''


def on_press(key):
    global Destination_Stop
    if key == Key.enter and Destination_Stop != '':
        ws.send(json.dumps({"origin": Current_Stop, "destination": int(Destination_Stop), "redirect": True}))
        Destination_Stop = ''
    elif key == Key.backspace:
        Destination_Stop = Destination_Stop[0:len(Destination_Stop) - 1]
        ws.send(json.dumps({"origin": Current_Stop, "destination": Destination_Stop, "digit":-1, "redirect": False}))
    else:
        for digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if key == KeyCode(char=digit):
                Destination_Stop += digit
                ws.send(json.dumps({"origin": Current_Stop, "destination": Destination_Stop, "digit": digit, "redirect": False}))


with Listener(on_press=on_press) as listener:
    listener.join()

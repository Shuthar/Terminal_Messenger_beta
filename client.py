import socket
import json
import threading
import time
from colorama import init, Fore


def jsonBuilder(s):
    return json.dumps(s)

def request(content):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 15000))
    sock.send(bytes(content, "utf-8"))
    response = sock.recv(1024)
    result = response.decode()
    sock.close()
    return result

def connection(user_name):
    content = jsonBuilder(({'user_name': user_name}))
    print(request(content))

def send_message(_for, user_name, text):
    content = jsonBuilder(({'for': _for, 'text': user_name + ': ' + text}))
    print(request(content))

def get_message(user_name):
    while True:
        content = jsonBuilder(({"get": user_name}))
        result = request(content)
        if result != "":
            print(" %45s " %  (Fore.GREEN + result + Fore.GREEN))
            time.sleep(5)

init()

user_name = input("Ввудите Ваше имя")
connection(user_name)

thread = threading.Thread(target=get_message(), args=[user_name])
thread.start()

while True:
    _for = input("кому написать сообщение?")
    _text = input("текст сообщения")
    send_message(_for, user_name, _text)
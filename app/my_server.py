import socket
import random
from _thread import *
import threading

print_lock = threading.Lock()


def threaded(c):
    answer_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.",
                   "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.",
                   "Yes", "Signs point to yes.", "Reply hazy, try again.", " Ask again later.",
                   "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
                   "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.",
                   "Very doubtful."]
    answers = {}
    while True:
        questions = c.recv(1024)
        if not questions:
            print('Bye')
            print_lock.release()
            break

        if not answers.get(questions):
            answers[questions] = random.choice(answer_list)

        c.send(answers[questions].encode('ascii'))
    c.close()


def my_server():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(5)

    while True:
        c, addr = s.accept()

        print_lock.acquire()

        start_new_thread(threaded, (c,))
    s.close()


if __name__ == '__main__':
    my_server()
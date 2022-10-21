import socket


def my_client():
    host = '127.0.0.1'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((host, port))

    while True:
        questions = input('\nI am the Magic 8 Ball, ask me a question :')
        s.send(questions.encode('ascii'))

        data = s.recv(1024)

        print('Answer :', str(data.decode('ascii')))

        while True:
            ans = input('\nDo you want to continue(y/n) :')
            if ans == 'y':
                break
            elif ans == 'n':
                break
            else:
                print('else')
                continue
        if ans == 'n':
            break
        else:
            continue
    s.close()


if __name__ == '__main__':
    my_client()
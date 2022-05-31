from random import choice
import tkinter as tk
from tkinter import Tk, Label, Button
"""
# tkinter podstawy


def click_action(button):
    button.config(text=f'Wow!')


def create_command(func, *args, **kwargs):
    def command():
        return func(*args, **kwargs)

    return command()


clicks = 0


def increase_clicks(button):
    global clicks
    clicks += 1
    button.config(text="Wow! x %s" % clicks)


if __name__ == '__main__':

    root = Tk()
    root.title('App')
    root.geometry('600x400')

    label = Label(root, text='Look at me!', font=30, fg='blue')
    label.pack()

    # click_button = Button(root, text='click me!', width=8, command=click_action)
    # lub
    click_button = Button(root, text='click me!', width=8)
    # click_button.config(command=click_action)

    click_button.pack()

    # click_button.config(command=create_command(click_action, click_button))
    # lub
    click_button.config(command=lambda: increase_clicks(click_button))

    root.mainloop()

 


# tkinter marynarzyk

avaliable_choices = ['p', 'k', 'n']
cpu = choice(avaliable_choices)


def play(player, cpu):
    win_with = {'p': 'k', 'k': 'n', 'n': 'p'}
    if player == cpu:
        return None
    elif win_with[player] == cpu:
        return True
    else:
        return False


def play_cmd(player):
    global text_label
    cpu = choice(avaliable_choices)
    is_user_winner = play(player, cpu)
    if is_user_winner is None:
        text_label.config(text='Remis', fg='blue')
    elif is_user_winner:
        text_label.config(text='To bylo zwyciestwo absolutne', fg='green')
    else:
        text_label.config(text='gg ez noob', fg='red')


if __name__ == '__main__':
    root = Tk()
    root.title('Marynarzyk')
    root.geometry('300x150')

    text_label = Label(root, font=40, text='Zagrajmy w marynarza!')
    text_label.pack()

    Button(
        root, text='Papier', font=40, width=10,
        command=lambda: play_cmd('p')
    ).pack()
    Button(
        root, text='Kamien', font=40, width=10,
        command=lambda: play_cmd('k')
    ).pack()
    Button(
        root, text='Nozyce', font=40, width=10,
        command=lambda: play_cmd('n')
    ).pack()

    root.mainloop()

"""

# tkinter z real python

if __name__ == '__main__':
    root = Tk()
    root.geometry('600x400')

    label = tk.Label(
        text="Hello, Tkinter",
        fg="white",  # Set the text color to white
        bg="black",  # Set the background color to black
        width=10,
        height=10
    )

    button = tk.Button(
        text="Click me!",
        width=25,
        height=5,
        bg="blue",
        fg="yellow",
        command=lambda: entry.get()
    )

    entry = tk.Entry(fg="yellow", bg="blue", width=50)

    label.pack()
    button.pack()
    entry.pack()

    sth = entry.get()
    print(sth)

    root.mainloop()


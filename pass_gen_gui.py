import random
from tkinter import *
from tkinter.ttk import *

class PasswordGui(object):
    """Creator: Luka Foy
       17/11/21 - Before work
       GUI class, functioning in creating a little password generator.
       All keys on the keyboard are letters.
       Contains a button - labeled "Generate" and an output box for the password
    """

    def __init__(self, parent, pass_length, characters):
        self.pass_length = pass_length
        self.characters = characters
        self.button = Button(parent, text='Generate Passowrd', command=self.update_label)
        self.button.grid(row=0, column=1, padx=50)
        self.output = Label(parent, text='Press Generate')
        self.output.grid(row=1, column=1, padx=10, pady=10)
    
    def pass_generator(self, size, characters):
        return ''.join(random.choice(self.characters) for char in range(size))    
    
    def update_label(self):
        self.output['text'] = self.pass_generator(self.pass_length, self.characters)


def input_length():
    user_input = input('How many characters? ')
    while user_input.isnumeric() == False:
        user_input = input('How many characters? ')
    return int(user_input)

def main():   
    window = Tk()
    length = input_length()
    characters = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*()~:"<>?{}|_+-=[]\;,./'
    passwordgui = PasswordGui(window, length, characters)
    window.mainloop()
        
main()

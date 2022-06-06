import random

CHARS = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqrRsStTuUvVwWxXyYzZ1234567890!@#$%^&*()~:"<>?{}|_+-=[]\;,./'

def pass_generator(size, characters):
    return ''.join(random.choice(characters) for char in range(size))


def main():
    user_input = int(input("How many characters? "))
    print(pass_generator(user_input, CHARS))

main()
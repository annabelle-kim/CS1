import random

def input_colored(text, color):
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    input(color_codes.get(color, "") + text + color_codes["reset"])
def print_colored(text, color):
    color_codes = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    print(color_codes.get(color, "") + text + color_codes["reset"])
while True:
    random_color=random.choice(["red","green","yellow","blue","magenta","white","cyan"])
    question=input_colored("Ask Magic 8 Ball a Question:","white")
    random_response = random.choice(["Of course!","Definetly Not!","Maybe!","Ask me later!","No way", "Come back another time"])
    print_colored(random_response,random_color)

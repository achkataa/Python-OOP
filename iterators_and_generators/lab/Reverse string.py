def reverse_text(text):
    return (char for char in reversed(text))



for char in reverse_text("step"):
    print(char, end='')
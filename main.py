def interpret(command):
    if command.startswith("print(") and command.endswith(")"):
        content = command[6:-1]
        print(eval(content))
    elif command.startswith("input(") and command.endswith(")"):
        prompt = command[6:-2]
        input(prompt)
    else:
        try:
            result = eval(command)
            print(result)
        except Exception as e:
            print(f"Error: {e}")

def main():
    lang_name = input("Enter your language name: ")
    print(f"Welcome to the {lang_name} Programming Language!")
    while True:
        command = input(f"{lang_name} >>> ")
        if command.lower() in ["exit", "quit"]:
            print(f"Goodbye from {lang_name}!")
            break
        interpret(command)

if __name__ == "__main__":
    main()

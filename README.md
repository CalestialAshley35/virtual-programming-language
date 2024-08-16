**Virtual Programming Language**

**Creator:** Calestial Ashley

**Link:** [Virtual Programming Language on Replit](https://replit.com/@calestialashley/Virtual-Programming-Language?s=app)

**Description:**  
The Virtual Programming Language game lets you explore basic programming. Name your language and use commands like `print("Hello World")`, `input("Name:")`, and arithmetic (e.g., `2 + 2`). It's interactive and fun!

**Features:**
- Customizable language name
- Basic commands for printing, input, and math
- Interactive prompt
- Easy exit with `exit` or `quit`

**How to Use:**
1. Visit the link and run the project.
2. Enter your language name.
3. Use the prompt to type commands.
4. Exit with `exit` or `quit`.

**Example Code:**

```python
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
```

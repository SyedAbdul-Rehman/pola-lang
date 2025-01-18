# **pola-lang** - An Urdu-Based Programming Language

**pola-lang** is a custom programming language designed to make coding more intuitive for Urdu-speaking users. With **pola-lang**, you can write code in Urdu using simple and relatable keywords. It’s powered by Python, making it easy to learn and use for beginners.

## Features

- **Urdu-based Syntax**: Write code using familiar Urdu words.
- **Simple Interpreter**: Execute `.pola` files directly from the terminal.
- **Custom Functions**: Use built-in functions like `jod`, `read`, `write`, etc.
- **Easy Setup**: Installation package that automatically installs Python and sets up everything.

## Installation

### Step 1: Download and Install

1. **Download the Installer**:  
   Download the setup file from the [releases section](https://github.com/SyedAbdul-Rehman/pola-lang/releases).

2. **Run the Installer**:  
   Double-click the installer file to begin the installation process. It will automatically:
   - Install Python if not already installed.
   - Add `pola` to your system PATH, so you can run your `.pola` files directly from the terminal.

### Step 2: Verify the Installation

Open your terminal and run the following command to ensure everything is set up correctly:

```bash
pola --version
```

You should see the version number of your pola-lang interpreter.

### Step 3: Create Your First .pola File
Create a new file with the `.pola` extension, e.g., `hello_world.pola` , and write your first program:

```
kr do "Hello, World!"
```

### Step 4: Run the Program
To execute your `.pola` file, simply type:

```bash
pola hello_world.pola
```

This will run your code and output:

```bash
Hello, World!
```

## Language Syntax

pola-lang allows you to use Urdu keywords in place of common Python constructs. Here’s a list of the most common keywords:

| Urdu Keyword           | Python Equivalent       |
|------------------------|-------------------------|
| chal                    | for                     |
| agar                    | if                      |
| wrna agar               | elif                    |
| wrna                    | else                    |
| kr do                   | print                   |
| pooch                   | input                   |
| jb tk                   | while                   |
| ruk ja                  | break                   |
| chor do                 | continue                |
| koshish kr              | try                     |
| nhi to                  | except                  |
| zaroor                  | finally                 |
| aur                     | and                     |
| ya                      | or                      |
| ult                     | not                     |
| bnao                    | def                     |
| gusa                    | raise                   |
| wapis                   | return                  |
| parho                   | read                    |
| likho                   | write                   |
| agay likho               | append_to_file          |
| bnao folder             | make_folder             |


## Custom Functions

In addition to standard Python functions, pola-lang includes several custom functions. These functions are defined in `custom_functions.py` and can be used in your code:

| Function Name           | Description                                  |
|-------------------------|----------------------------------------------|
| `jod(a, b)`             | Adds two values.                             |
| `parho(file_path)`       | Reads the contents of a file.               |
| `likho(file_path, content)` | Writes content to a file.                 |
| `agay likho(file_path, text)` | Appends text to a file.           |
| `bnao folder(folder_name)` | Creates a new folder.                      |

### Example usage:

```
bnao mera_naam():
    kr do "Mera naam pola-lang hai!"

mera_naam()
```
## Contributors

I’d like to thank someone important for their unwavering support and for keeping me motivated:

- [Hafiza](https://github.com/hafeeza9229) - For your quiet encouragement and motivation, which kept me focused on completing this project.

Thank you for helping make this project a reality!

## Contributing

We welcome contributions to pola-lang! Feel free to fork the repository, submit issues, and create pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## Contact

If you have any questions, feel free to reach out to us through GitHub or contact the project maintainers at:

**Syed Abdul-Rehman**  
Email: [nawazabdulrehman7@gmail.com](mailto:your-email@example.com)






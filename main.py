import subprocess

# Array of commands (Windows and Linux/macOS examples)
commands = [
    'echo Hello, World!',       # Example command for Windows / Linux/macOS
    'dir',                      # List directory (Windows)
    'ipconfig',                 # ip 
]

# Loop over the array of commands and execute each one
for command in commands:
    try:
        # Execute each command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # Print the output of the command
        print(result.stdout)
        print(result.stderr)  # Print any error if occurred
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{command}' failed with exit code {e.returncode}")

import subprocess

# Example shell command
command = "ls -l"

# Execute the command
result = subprocess.run(command, shell=True, capture_output=True, text=True)
droid_command = subprocess.run(
    "droidbot --help", shell=True, capture_output=True, text=True
)

# Print the output
print(result.stdout)
print(droid_command.stdout)

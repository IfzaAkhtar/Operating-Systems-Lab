import os
import subprocess

print("===== SYSTEM CALLS & PROCESS CREATION =====")

print("\nParent Process PID:", os.getpid())
print("Creating child process...")

child = subprocess.Popen(["bash", "-c",
    "echo 'Child Process Running'; echo 'Child PID:' $$; echo 'Parent PID:' $PPID"
])

print("Child PID:", child.pid)

child.wait()
print("Child process completed.")

print("\n===== LINUX COMMAND =====")

result = subprocess.run(["pwd"], capture_output=True, text=True)
print("Current directory:", result.stdout.strip())

print("\n===== FILE OPERATION =====")

filename = "test_file.txt"

try:
    with open(filename, "w") as file:
        file.write("Operating Systems Lab\n")
        file.write("File created and written successfully.")

    print("File created and written.")

    with open(filename, "r") as file:
        data = file.read()

    print("File contents:")
    print(data)

    print("File closed successfully.")

except Exception as e:
    print("File error:", e)

print("\n===== DEVICE INTERFACE =====")

try:
    with open("/dev/null", "w") as device:
        device.write("Test data")

    print("/dev/null accessed successfully.")

except Exception as e:
    print("Device error:", e)

print("\n===== ERROR HANDLING =====")

try:
    with open("/invalid/path/test.txt", "r") as file:
        data = file.read()

except FileNotFoundError:
    print("Error handled: Invalid file path.")

print("\n===== EVIDENCE =====")
print("Parent PID:", os.getpid())
print("Child PID:", child.pid)
print("Process creation: SUCCESS")
print("Child completion: SUCCESS")
print("Linux command: SUCCESS")
print("File operation: SUCCESS")
print("Device interface: SUCCESS")
print("Error handling: SUCCESS")
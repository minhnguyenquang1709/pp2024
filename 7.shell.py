import os
import subprocess

def runCommand(command):
    try:
        # Break down the command
        args = command.split()

        # If input
        if "<" in args:
            # Seperate into parts
            indexInput = args.index("<")
            inputFile = args[indexInput+1]
            args = args[:indexInput]
        else:
            inputFile = None
        # If output
        if ">" in args:
            indexOutput = args.index(">")
            outputFile = args[indexOutput+1]
            args = args[:indexOutput]
        else:
            outputFile = None

        # Execute command
        if inputFile != None:
            with open(inputFile, 'r') as file:
                result = subprocess.run(args, stdin=file, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            result = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if outputFile != None:
            with open(outputFile, "w") as file:
                file.write(result.stdout.decode())
        else:
            print(result.stdout.decode())

        # Error
        if result.returncode != 0:
            print("Error: ", result.stdout.decode())
    except Exception as e:
        print("\n\tError - ", str(e))

def main():
    while True:
        command = input("\nEnter command ('exit' to end): ")
        if command.lower() == "exit":
            break
        else:
            runCommand(command)

        
if __name__ == "__main__":
    main()
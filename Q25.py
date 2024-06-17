'''Write a program that copies the contents of one text file to another'''

source_file = "source.txt"
destination_file = "destination.txt"


with open(source_file, 'w') as src:
    src.write("This is the content of the source file.\n")
    src.write("It will be copied to the destination file.\n")

print(f"Created {source_file} with initial content.")


try:

    with open(source_file, 'r') as src:

        content = src.read()

    with open(destination_file, 'w') as dest:

        dest.write(content)

    print(f"Contents copied from {source_file} to {destination_file} successfully.")
except FileNotFoundError:
    print(f"Error: The file {source_file} does not exist.")
except IOError as e:
    print(f"Error: An IOError occurred. {e}")

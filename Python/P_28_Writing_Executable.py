filename=input("what is the filename ")
content=input("enter the content: ")
with open(filename, 'w') as file:
    file.write(content)
open_file=input("whould youlike to read this files ")
if open_file in ['y', 'n']:
    if open_file=='y':
        with open(filename, 'r') as file:
            print(file.read())
            
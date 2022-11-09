import os
import shutil


def open_file():
    source = str(input('Input source: '))
    if os.path.exists(source):
        os.startfile(source)
    else:
        print('unable to solve request')

def copy_file():
    source = str(input('Input source: '))
    destination1 = str(input('input a destination: '))
    if os.path.exists(source) and os.path.exists(destination1):
        shutil.copy(source, destination1)
    else:
        print('Error: unable to solve request')

def delete_file():
    source = str(input('Input source: '))
    if os.path.exists(source):
        os.remove(source)
    else:
        print('Error: unable to solve request')

def rename_file():
    chosenFile = str(input('Input source: '))
    if os.path.exists(chosenFile):
        # path1 = os.path.dirname(chosenFile)
        # extension=os.path.splitext(chosenFile)[1]
        newName = str(input('enter new name: '))
        # path2 = os.path.join(path1, newName+extension)
        # print(path2)
        os.rename(chosenFile, newName)
    else:
        print('Error: unable to solve request')

def move_file():
    source = str(input('Input source: '))
    destination = str(input('Input destination: '))
    if source == destination:
        print('Error: unable to solve request')
    else:
        shutil.move(source, destination)

def make_folder():
    source = str(input('input source name: '))
    if os.path.exists(source):
        folderName = str(input('Input folder name: '))
        path1 = os.path.join(source, folderName)
        if not os.path.exists(path1):
            os.mkdir(path1)
        else:
            print('Error: unable to solve request')
    else:
        print('Error: unable to solve request')

def delete_folder():
    source = str(input('input source: '))
    if os.path.exists(source):
        os.rmdir(source)
    else:
        print('unable to solve request')

def open_folder():

    source = str(input('input a source: '))
    pathSave = source
    print(os.listdir(source))
    if os.path.exists(source):
        while True:
            command1 = str(input('Input a folder to open: '))
            if command1 == '<':
                print(os.listdir(pathSave))
            elif command1 == 'break':
                break
            else:
                source2 = os.path.join(pathSave, command1)
                print(os.listdir(source2))
    else:
        print('unable to solve request')

def create_file():
    source = str(input('input source: '))
    if os.path.exists(source):
        fileName = str(input('input file name: '))
        createPath = os.path.join(source, fileName)
        print(createPath)
        open(createPath, 'x')
    else:
        print('Error: unable to solve request')

def write_in_file():
    source = str(input('input source: '))
    if os.path.exists(source):
        file1 = open(source, 'a', encoding='utf-8')
        addText = str(input('input a text: '))
        file1.write(addText)
        file1.close()

    else:
        print('Error: unable to solve request')

def read_file():
    source = str(input('input source: '))
    if os.path.exists(source):
        file1 = open(source, encoding='utf-8')
        print(file1.read())
        file1.close()
    else:
        print('Error: unable to solve request')
    
def helpFile():
    print('Here is list of commands: ')
    print('Open_file')
    print('Copy_file')
    print('Delete_file')
    print('Rename_file')
    print('Move_file')
    print('Make_folder')
    print('Delete_folder')
    print('Open_folder')
    print('Create_file')
    print('Write_in_file')
    print('HelpFile')
    print('Enter - stop to exit file manager')


def main():

    print('Here is list of commands: ')
    print('Open_file')
    print('Copy_file')
    print('Delete_file')
    print('Rename_file')
    print('Move_file')
    print('Make_folder')
    print('Delete_folder')
    print('Open_folder')
    print('Create_file')
    print('Write_in_file')
    print('HelpFile')

    command = ''
    while command != 'stop':
        command = str(input("Enter command: "))

        if command == 'Open_file':
            open_file()
        elif command == 'Copy_file':
            copy_file()
        elif command == 'Delete_file':
            delete_file()
        elif command == 'Rename_file':
            rename_file()
        elif command == 'Move_file':
            move_file()
        elif command == 'Make_folder':
            make_folder()
        elif command == 'Delete_folder':
            delete_folder()
        elif command == 'Open_folder':
            open_folder()
        elif command == 'Create_file':
            create_file()
        elif command == 'Write_in_file':
            write_in_file()
        elif command == 'HelpFile':
            helpFile()
        else:
            print('unable to solve request')

if __name__ == '__main__':
    main()


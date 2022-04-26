#!/usr/bin/env python3
import os 
import time

MAIN_BOILEPLATE_WITHOUT_ARGS = "#include <stdio.h>\n\nint main()\n{\n    return 0; \n}"
MAIN_BOILEPLATE_WITH_ARGS = "#include <stdio.h>\n\nint main(int argc, char *argv[])\n{\n    return 0; \n}"
CURRENT_DIRECTORY = os.getcwd()


def create_file(creation_times: int=1, in_separete_directory=False) -> None:
    """
    function to create .c boilerplate file/s
    creation_times -> how many files to be created. default = 1
    in_separate_directory -> should the file/s to be created in new directory inside the currrent directory. default = False
    """
    if in_separete_directory:
        user_input_directory = input("Enter the name of directory: ")
        directory = f"{CURRENT_DIRECTORY}/{user_input_directory}"
        try:
            os.mkdir(directory)
        except OSError as error:
            print(error)
            return -1
        os.chdir(directory)
    user_input = input("Enter your file name: ")
    label = 1
    extension = ".c"
    while (label <= creation_times):
        file = user_input + str(label) + extension
        to_include_arguments = input("Should the main function have arguments? (Y/N) : ").lower()
        if to_include_arguments == 'n':
            with open(file, "w", encoding="utf8") as file:
                file.write(MAIN_BOILEPLATE_WITHOUT_ARGS)
            label+=1
        elif to_include_arguments == 'y':
            with open(file, "w", encoding="utf8") as file:
                file.write(MAIN_BOILEPLATE_WITH_ARGS)
            label+=1
        else:
            print("Invalid input! Please choose between 'y' and 'n'")


create_file()

#!/usr/bin/env python3

import os

CURRENT_DIRECTORY = os.getcwd()

MAIN_BOILEPLATE_WITHOUT_ARGS = "#include <stdio.h>\
        \n\nint main()\n\
        {\n    return 0; \n}"

MAIN_BOILEPLATE_WITH_ARGS = "#include <stdio.h>\
        \n\n\
        int main(int argc, char *argv[])\
        \n{\n    return 0; \n}"

CURRENT_DIRECTORY = os.getcwd()


def create_file(
        creation_times: int = 1,
        in_separete_directory=False,
        incremented_names=False) -> None:
    """
    function to create .c boilerplate file/s

    Args:
        creation_times: int -> how many times files to be created
        Default value 1
        in_separete_directory: bool -> created files to be in directory
        inside the main directory
        Default value False
        incremented_names: bool -> give one file name and every following
        file that is created will have the name {filename(counter+=1).c}
        Default value False
    """
    if in_separete_directory:
        user_input_directory = input("Enter the name of directory: ")
        directory = f"{CURRENT_DIRECTORY}/{user_input_directory}"
        try:
            os.mkdir(directory)
        except FileExistsError:
            # print(error)
            user_input = input(
                    "Directory exist, do you want to enter it?: (y/n) "
                    )
            if user_input == 'y':
                os.chdir(directory)
            else:
                print("Quiting...!")
                return -1
        os.chdir(directory)
    counter = 1
    extension = ".c"
    if incremented_names:
        user_input = input("Enter file name: ")
    while (counter <= creation_times):
        if not incremented_names:
            user_input = input("Enter file name: ")
            file = user_input + extension
        file = user_input + str(counter) + extension
        to_include_arguments = input(
                "Should the main function have arguments? (Y/N) : "
                ).lower()
        while to_include_arguments != 'y' and to_include_arguments != 'n':
            print("Invalid input! Please choose between 'y' and 'n'")
            to_include_arguments = input(
                "Should the main function have arguments? (Y/N) : "
                ).lower()
        if to_include_arguments == 'n':
            with open(file, "w+", encoding="utf8") as file:
                file.write(MAIN_BOILEPLATE_WITHOUT_ARGS)
            counter += 1
        elif to_include_arguments == 'y':
            with open(file, "w+", encoding="utf8") as file:
                file.write(MAIN_BOILEPLATE_WITH_ARGS)
            counter += 1


create_file(
        creation_times=3, in_separete_directory=True, incremented_names=False
)

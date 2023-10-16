# vhdl-parser

## Overview

`vidl-parser` is a simple script that streamlines the process of generating a text file from `.vhd` (VHDL) files. If you find yourself repeatedly copying and pasting VHDL code into a lab writeup or documentation, this tool can help automate the process. 

## Usage

1. Place all your `.vhd` files in the `./files` directory.
2. Run the script using the following command:

'''python main.py'''


3. The script will compile the contents of the `.vhd` files and create an "output.txt" file in the same directory.

You can also customize the number of underlines used at the top of each file to match your document's formatting requirements.

## Motivation

The idea for this script came about from personal frustration. When I was in a class that required me to include VHDL code at the end of my lab writeups, I found the manual process of copying and pasting to be time-consuming and tedious. `vidl-parser` was developed to simplify this task, making it more efficient and less error-prone.

Feel free to use and modify this script to suit your own needs. If you encounter any issues or have suggestions for improvements, please don't hesitate to reach out.

Happy coding! 😄

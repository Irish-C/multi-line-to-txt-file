# multi-line-to-txt-file
A python method that will write multiple line of text contents into a text file mylife.txt. Specifically, this provides a simple GUI for users to add lines of text to a file called "mylife.txt". It uses the PySimpleGUI library to create a window where the user can enter lines of text, view all the lines added so far, and choose to add more lines or finish and save the file.

## Installation
To run the program, you'll need to have [Python 3](https://www.python.org/downloads/) installed on your computer. <br/>
>**Note: This program intended to work for windows os.**
<br/>

I used [VS Code](https://code.visualstudio.com/download) to create and run the program.

## Dependencies
The script requires the following Python packages:

* PySimpleGUI
* pyperclip
<br/>

```pip install PySimpleGUI pyperclip```

# How the code works
1. Clone the repository or download the multiline_py file.
2. Open a terminal and navigate to the directory containing the script:
``cd /path/to/directory``
3. Run the script using python:
``python multiline_writer.py``
4. When prompted, click the text box on the right side of the "Enter line:".
sample line/s:
- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
4. Click "Add this Line" button to add the line you wrote, or "Finish" button to terminate the program.
5. A window will appear and will ask to user if they want to add more line.
6. Click "Yes" button to add line, and "No" button to not add line and the file will be saved.
7. You can now visit the directory where your file is expected to be stored.
> the default path is the current directory of the python method.


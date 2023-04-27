# Import PySimpleGUI module
import PySimpleGUI as sg
import os

# Open the file "mylife.txt" in write mode
with open("mylife.txt", "w") as my_file:
    pass

# Define the function for entering lines
def my_life_txt():
    # Open the file "mylife.txt" in append mode
    with open("mylife.txt", "a") as my_file:
    
    #Create a loop to let user add line/s
        while True:
            # Define the layout for the main window
            layout = [
                [sg.Text("Enter a line:"), sg.InputText()], # Prompt the user to enter a line
                [sg.Button("Add this line"), sg.Button("Finish")],
                [sg.Multiline(size=(80, 20), key="_MULTILINE_")], # Display all the lines added in realtime
            ]
            # Create the main window 
            window = sg.Window("My Life", layout)

            #function call for main window
            event, values = window.read()

            # If the user clicks the "Add this line" button, the entered line will be appended to "mylife.txt"
            if event == "Add this line":
                my_file.write(values[0] + "\n")
               # Append the new line to the existing lines displayed in the Multiline element
                window["_MULTILINE_"].update(value=window["_MULTILINE_"].get() + values[0] + "\n")
                my_file.append(str())
            # If the user clicks the "Exit" button, the program will terminate
            if event == "Finish":
                break
            # If the user closes the window, the program will terminate
            if event == sg.WIN_CLOSED:
                window.close()
                break

# Define the layout for the main window
layout = [[sg.Text("Do you want to enter some lines?")], 
          [sg.Button("Yes"), sg.Button("No")]]

#Create the "Add Line" window
window = sg.Window("My Life", layout)

# Create a loop to continuously prompt the user to add more lines
while True:
    more_event, values = window.read()
    window.close()
    # If the user clicks the "No" button, the program will terminate
    if more_event == "No":
        break
    # If the user clicks the "Yes" button, the function for entering lines will be called
    if more_event == "Yes":
        window.close()
        # Call the function for entering lines
        my_life_txt()
    # If the user clicks the "Save File" button, all the entered lines will be saved to "mylife.txt"
        if more_event == "Save File":
            with open("mylife.txt", "r") as my_file:
                lines = my_file.readlines()
            cwd = os.getcwd()
            save_file_path = os.path.join(cwd, "mylife.txt")
            with open(save_file_path, "w") as save_file:
                save_file.writelines(lines)
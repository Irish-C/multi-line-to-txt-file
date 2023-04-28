import PySimpleGUI as sg
import sys
import time

# Define the function for entering lines
def my_life_txt():
    # Open the file "mylife.txt" in append mode
    with open("mylife.txt", "a") as my_file:
        # Initialize a list to keep track of all the lines added
        lines = []

        # Create a loop to let user add line/s
        while True:
            # Define the layout for the main window
            layout = [
                [sg.Text("Enter a line:"), sg.InputText()], # Prompt the user to enter a line
                [sg.Button("Add this line"), sg.Button("Finish")],
                [sg.Multiline(size=(80, 20), key="_MULTILINE_")], # Display all the lines added in realtime
            ]

            # Create the main window 
            window = sg.Window("My Life", layout)

            # Function call for main window
            event, values = window.read()

            # If the user clicks the "Add this line" button, the entered line will be appended to "mylife.txt"
            if event == "Add this line":
                my_file.write(values[0] + "\n")
                # Append the new line to the existing lines displayed in the Multiline element
                lines.append(values[0])
                # Update the Multiline element to display all the lines
                window["_MULTILINE_"].update(value="\n".join(lines))
                
                # Prompt the user if they want to add more lines
                add_more_layout = [
                    [sg.Text("Do you want to add more lines?")],
                    [sg.Button("Yes"), sg.Button("No")],
                ]
                add_more_window = sg.Window("Add more lines?", add_more_layout)
                add_more_event, add_more_values = add_more_window.read()
                
                # If the user clicks "Yes", continue adding lines
                if add_more_event == "Yes":
                    add_more_window.close()
                    continue
                # If the user clicks "No", exit the loop and close the window
                elif add_more_event == "No":
                    sg.Popup("File saved successfully")
                    add_more_window.close()
                    break

            # If the user clicks the "Finish" button, close the window and exit the loop
            elif event == "Finish":
                sg.Popup("File saved successfully")
                time.sleep(1)
                sys.exit()
                

# Call the function
my_life_txt()

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
    
        # Initialize a list to keep track of all the lines added
        lines = []

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
                lines.append(values[0])
                window["_MULTILINE_"].update(value="\n".join(lines)) 



                # Create a PySimpleGUI pop-up window to display the output

            # If the user clicks the "Exit" button, the program will terminate
            if event == "Finish":
                break

    window.close()

    # # output_layout = [
    # #     [sg.Multiline(my_file, size=(30, 20)),
    # #     [sg.Button("Save File"), sg.Button("OK")]]
    # # ]     
    # # output_window = sg.Window("Output", output_layout)
    # # output_event, output_values = output_window.read()

    # # if output_event == "Save File":
    # #     with open("mylife.txt", "a") as output_file:
    # #         output_file.write(output_values["_MULTILINE_"])

    # # If the user closes the window, the program will terminate
    # if output_event == "OK" or output_event == sg.WIN_CLOSED:
    #     exit()

# Define function for entering more lines 
def more_line_txt():
    # Define the layout for the main window
    more_layout =[
        [sg.Text("Do you want to more lines?")],
        [sg.Button("Yes"), sg.Button("No")]
    ]

    #Create the "Add Line" window
    more_line_window = sg.Window("My Life", more_layout)

    # Create a loop to continuously prompt the user to add more lines
    while True:
        more_event, values = more_line_window.read()
        more_line_window.close()
        # If the user clicks the "No" button, the program will terminate
        if more_event == "No":
            with open("mylife.txt", "r") as my_file:
                lines = my_file.readlines()
            cwd = os.getcwd()
            save_file_path = os.path.join(cwd, "mylife.txt")
            with open(save_file_path, "w") as save_file:
                save_file.writelines(lines)   
            break 
        # If the user clicks the "Yes" button, the function for entering lines will be called
        if more_event == "Yes":
            more_line_window.close()
            # Call the function for entering lines
            my_life_txt()
    more_line_window.close()


# Create while loop for def functions
while True:

    # Define the layout for the initial window
    init_layout =[
        [sg.Text("Hi, I can take notes of your lines for you")],
        [sg.Text("Do you want to proceed?")],
        [sg.Button("Proceed"), sg.Button("Exit")]
    ]

    #Create the "Add Line" window
    init_window = sg.Window("My Life", init_layout)

    init_event, values = init_window.read()
    init_window.close()

    # If the user clicks the "No" button, the program will terminate
    if init_event == "Exit":
        break
    
    # If the user clicks the "Save File" button, all the entered lines will be saved to "mylife.txt"
    if init_event == "Proceed":
        my_life_txt()
        # Define the PySimpleGUI layout for the "File Saved" window
        file_saved_layout = [
            [sg.Text("File saved successfully!", key ="saved")],
            [sg.Button("OK")]
        ]
        # Create the PySimpleGUI window for the "File Saved" message
        file_saved_window = sg.Window("File Location", file_saved_layout)

        # Wait for the user to close the file saved window
        while True:
            file_event, values = file_saved_window.read()
            if file_event in (sg.WINDOW_CLOSED, "OK"):
                break

    # _event == "Save File":
    #     with open("mylife.txt", "r") as my_file:
    #         lines = my_file.readlines()
    #     cwd = os.getcwd()
    #     save_file_path = os.path.join(cwd, "mylife.txt")
    #     with open(save_file_path, "w") as save_file:
    #         save_file.writelines(lines)

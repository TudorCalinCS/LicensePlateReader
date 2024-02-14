from tkinter import filedialog, Tk

def open_file_dialog():
    root = Tk()
    root.withdraw()

    # Prompt the user to select a file
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])

    root.destroy()

    return file_path
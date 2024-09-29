import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Define the path for the blank icon
icon_path = 'C:\\Users\\Frank\\Desktop\\blank.ico'

# Create a function to generate a blank icon
def create_blank_ico(path):
    size = (16, 16)
    image = Image.new("RGBA", size, (255, 255, 255, 0))
    image.save(path, format="ICO")

# Create the blank ICO file
create_blank_ico(icon_path)

# Create the main window
root = tk.Tk()
root.title("Image-to-Icon Tool")
root.geometry("400x200")

# Set custom icon
root.iconbitmap(icon_path)

# Store the selected file path
selected_file_path = None

def select_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(
        title="Select a PNG or JPEG File",
        filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpeg;*.jpg")]
    )
    if selected_file_path:
        file_label.config(text=f"Selected: {selected_file_path}")
        convert_button.config(state=tk.NORMAL)
    else:
        file_label.config(text="No file selected")

def save_ico_file():
    global selected_file_path
    if not selected_file_path:
        messagebox.showerror("Error", "Please select a PNG or JPEG file first.")
        return
    
    # Ask where to save the ICO file
    save_path = filedialog.asksaveasfilename(
        defaultextension=".ico",
        filetypes=[("ICO Files", "*.ico")],
        title="Save ICO File"
    )
    
    if save_path:
        try:
            # Open the image
            img = Image.open(selected_file_path)

            # Use the original size
            ico_size = img.size

            # Save the image as ICO with the original size
            img.save(save_path, format='ICO')
            messagebox.showinfo("Success", f"File saved as {save_path} with size {ico_size}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# UI Elements
file_label = tk.Label(root, text="No file selected")
file_label.pack(pady=10)

select_button = tk.Button(root, text="Select PNG/JPEG", command=select_file)
select_button.pack(pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert to ICO", command=save_ico_file, state=tk.DISABLED)
convert_button.pack(pady=10)

# Run the GUI
root.mainloop()

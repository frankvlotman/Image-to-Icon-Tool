import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Create the main window
root = tk.Tk()
root.title("PNG/JPEG/JFIF to ICO Converter")
root.geometry("400x200")

# Store the selected file path
selected_file_path = None

def select_file():
    global selected_file_path
    selected_file_path = filedialog.askopenfilename(
        title="Select a PNG, JPEG, or JFIF File",
        filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpeg;*.jpg"), ("JFIF Files", "*.jfif")]
    )
    if selected_file_path:
        file_label.config(text=f"Selected: {selected_file_path}")
        convert_button.config(state=tk.NORMAL)
    else:
        file_label.config(text="No file selected")

def save_ico_file():
    global selected_file_path
    if not selected_file_path:
        messagebox.showerror("Error", "Please select a PNG, JPEG, or JFIF file first.")
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

select_button = tk.Button(root, text="Select PNG/JPEG/JFIF", command=select_file)
select_button.pack(pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert to ICO", command=save_ico_file, state=tk.DISABLED)
convert_button.pack(pady=10)

# Run the GUI
root.mainloop()

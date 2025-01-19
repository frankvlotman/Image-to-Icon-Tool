import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Added for custom button styling
from PIL import Image

# Define the path for the blank icon
ICON_PATH = os.path.join(os.path.dirname(__file__), 'blank.ico')  # Saves in the same directory as the script

# Create a blank (transparent) ICO file if it doesn't exist
def create_blank_ico(path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))
    if not os.path.exists(path):
        size = (16, 16)  # Size of the icon
        image = Image.new("RGBA", size, (255, 255, 255, 0))  # Transparent image
        image.save(path, format="ICO")

# Create the blank icon
create_blank_ico(ICON_PATH)

# Create the main window
root = tk.Tk()
root.title("PNG/JPEG/JFIF to ICO Converter")
root.geometry("400x250")  # Increased height to accommodate additional UI elements

# Set the window icon to the blank icon
try:
    root.iconbitmap(ICON_PATH)
except Exception as e:
    messagebox.showwarning("Icon Error", f"Failed to set window icon: {e}")

# Initialize ttk.Style
style = ttk.Style()
style.theme_use("clam")  # Use 'clam' theme for better customization

# Define custom style for buttons
style.configure("Custom.TButton",
                background="#d0e8f1",
                foreground="black",
                borderwidth=1,
                focusthickness=3,
                focuscolor='none',
                padding=6)  # Added padding for better appearance

# Define style map for hover (active) state
style.map("Custom.TButton",
          background=[('active', '#87CEFA')],
          foreground=[('active', 'black')])

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
        convert_button.config(state=tk.DISABLED)  # Disable if no file is selected

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
            
            # Determine the sizes to include in the ICO
            # Common sizes include 16x16, 32x32, 48x48, 64x64, 128x128, 256x256
            sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
            
            # Resize the image to the required sizes
            img_ico = img.convert("RGBA")
            img_ico.save(save_path, format='ICO', sizes=sizes)
            
            messagebox.showinfo("Success", f"File saved as {save_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# UI Elements
file_label = tk.Label(root, text="No file selected", bg="#f0f0f0", fg="#333333", font=("Arial", 11))
file_label.pack(pady=10)

select_button = ttk.Button(root, text="Select PNG/JPEG/JFIF", command=select_file, style="Custom.TButton")
select_button.pack(pady=5)

# Convert button
convert_button = ttk.Button(root, text="Convert to ICO", command=save_ico_file, style="Custom.TButton", state=tk.DISABLED)
convert_button.pack(pady=5)

# Add a note or instructions (optional)
note_label = tk.Label(root, text="Select an image file to convert it to ICO format.", bg="#f0f0f0", fg="#555555", font=("Arial", 9))
note_label.pack(pady=10)

# Configure the main window's background to match widget styles
root.configure(bg="#f0f0f0")

# Run the GUI
root.mainloop()

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        load_image(file_path)

def load_image(file_path):
    global original_image
    original_image = Image.open(file_path)
    original_image.thumbnail((300, 300))  # Resize image to fit in the canvas
    photo = ImageTk.PhotoImage(original_image)
    canvas.itemconfig(image_on_canvas, image=photo)
    canvas.image = photo

def convert_to_sketch():
    global original_image
    if original_image:
        gray_image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2GRAY)
        inverted_gray_image = 255 - gray_image
        blurred_image = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
        inverted_blurred_image = 255 - blurred_image
        final_sketch = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)
        cv2.imshow("Sketch", final_sketch)
    else:
        print("No image loaded")

# Create main window
root = tk.Tk()
root.title("Image to Sketch Converter")

# Create a canvas to display the image
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Create a placeholder for the image on the canvas
image_on_canvas = canvas.create_image(0, 0, anchor=tk.NW)

# Create buttons
open_button = tk.Button(root, text="Open Image", command=open_file)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert to Sketch", command=convert_to_sketch)
convert_button.pack(side=tk.LEFT, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()

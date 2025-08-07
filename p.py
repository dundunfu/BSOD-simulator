import tkinter as tk
import platform
from PIL import Image, ImageTk

root = tk.Tk()
if platform.system() == 'Windows':
    version = platform.version()
    
def show_fullscreen_image(image_path):
    root.config(cursor="none")
    image = Image.open(image_path)
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()
    image.resize((x, y))
    photo = ImageTk.PhotoImage(image)
    canvas = tk.Canvas(root, width=image.width, height=image.height)
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo  
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}")
    root.overrideredirect(True)
    root.mainloop()

def system_version():
    if '10' in version:
        return True
    elif '8.1' in version:
        return True
    elif '8' in version:
        return True
    else:
        return False

if system_version():
    show_fullscreen_image("bluescreen_8+.jpg")
else:
    show_fullscreen_image("bluescreen_7-.jpg")
    

from tkinter import *
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFilter
import random
import os

root = Tk()
root.title("Photoshoppe")
#MAKE THE HEIGHT 466
root.geometry("1000x466")
root.config(bg="teal")

''' MODEL - Functions and Data'''
pic_entry = StringVar()
rect = None
start_x, start_y = 0, 0
end_x, end_y = 0,0


def load_image():
    global loaded_image
    file_name = pic_entry.get()
    try:
        img = Image.open(file_name)
        info_label.config(text = "")
        width, height = img.size
        if width > height:
            loaded_image = img.resize((600, 446), Image.LANCZOS)
        else: 
            multiplier = 446 / height
            loaded_image = img.resize((int(width * multiplier), 446), Image.LANCZOS)
        display_image(loaded_image)
    except FileNotFoundError:
        info_label.config(text = "File not found, check name.")

def display_image(image):
    global loaded_image
    loaded_image = image
    root.photo_image = ImageTk.PhotoImage(loaded_image)
    canvas.create_image(250, 223, image=root.photo_image)

def apply_black_and_white():
    global loaded_image
    if load_image:
        pixels = loaded_image.load()
        for y in range(loaded_image.height):
            for x in range(loaded_image.width):
                r,g,b = pixels[x,y]
                avg = int((r+g+b)/3)
                pixels[x,y]=(avg,avg,avg)
        display_image(loaded_image)

# Save the modified image
def save_image():
    if loaded_image:
        file_name = pic_entry.get()
        base, ext = os.path.splitext(file_name)
        modified_file_name = f"{base}_modified.png"
        loaded_image.save(modified_file_name)
        print(f"Image saved as {modified_file_name}")

def on_click(event):
    global start_x, start_y, loaded_image
    start_x, start_y = event.x, event.y

def on_drag(event):
    global start_x, start_y, rect, end_x, end_y
    canvas.delete(rect)  # Delete the previous rectangle
    rect = canvas.create_rectangle(start_x, start_y, event.x, event.y, outline = "white", dash = (5,5))
    end_x = event.x
    end_y = event.y
    


def sepia():
    global loaded_image
    if load_image:
        image = loaded_image
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                red = pixels[x,y][0]
                blue = pixels[x,y][1]
                green = pixels[x,y][2]
                pixels[x,y] = (int(red*.393 + green*0.769 + blue*0.189),int(red*.349 + green*0.686 +blue*0.168),int(red*.272 + green*0.534 +blue*0.131)
    )
        display_image(image)

def invert():
    global loaded_image
    if load_image:
        image = loaded_image
        pixels = image.load()
        for y in range(image.height):
            for x in range(image.width):
                red = pixels[x,y][0]
                blue = pixels[x,y][1]
                green = pixels[x,y][2]
                pixels[x,y] = (255 - red, 255 - green, 255 - blue)
        display_image(image)

def pixelated():
    global loaded_image, start_x, start_y, end_x, end_y, rect
    if load_image:
        start_x, start_y, end_x, end_y = start_x - (500 - loaded_image.width) // 2, start_y - (446 - loaded_image.height) // 2, end_x - (500 - loaded_image.width) // 2, end_y - (446 - loaded_image.height) // 2
        left = min(start_x, end_x)
        top = min(start_y, end_y)
        right = max(start_x, end_x)
        bottom = max(start_y, end_y)

        image = loaded_image
        pixels = image.load()
        for y in range(top, bottom, 10):
            for x in range(left, right, 10):
                color = (pixels[x,y][0],pixels[x,y][1],pixels[x,y][2])
                #this is the loops for each squares
                for y2 in range(y, y+10):
                    for x2 in range(x, x+10):
                        pixels[x2,y2] = (color[0],color[1],color[2])
        canvas.delete(rect)
        display_image(image)

def crop():
    global loaded_image, start_x, start_y, end_x, end_y, rect
    if load_image:
        start_x, start_y, end_x, end_y = start_x - (500 - loaded_image.width) // 2, start_y - (446 - loaded_image.height) // 2, end_x - (500 - loaded_image.width) // 2, end_y - (446 - loaded_image.height) // 2
        left = min(start_x, end_x)
        top = min(start_y, end_y)
        right = max(start_x, end_x)
        bottom = max(start_y, end_y)

        cropped_image = loaded_image.crop((left, top, right, bottom))

        canvas.delete(rect)
        display_image(cropped_image)


def line_drawing():
    global loaded_image
    if load_image:
        gray_image = loaded_image.convert("L")
        edge_image = gray_image.filter(ImageFilter.FIND_EDGES)
        display_image(edge_image)

def increase_contrast():
    global loaded_image
    enhancer = ImageEnhance.Contrast(loaded_image)
    factor = 2
    loaded_image = enhancer.enhance(factor)
    display_image(loaded_image)


def pointillism():
    global loaded_image
    if load_image:
        image = loaded_image
        pixels = image.load()
        canvas = Image.new("RGB",(image.size[0],image.size[1]), "white")
        for i in range(120000):
                #random pixels and color
                x = random.randint(1, image.width-1)
                y = random.randint(1, image.height-1)
                #draws circles
                size = random.randint(5,8)
                ellipsebox=[(x,y),(x+size,y+size)]
                draw = ImageDraw.Draw(canvas)
                draw.ellipse(ellipsebox,fill=(pixels[x,y][0],pixels[x,y][1],pixels[x,y][2]))
                del draw
        display_image(canvas)



''' CONTROLLERS - Widgets That Users Interact With'''
image_entry = Entry(root, bg = "light blue", fg = "gray", font = ("Times New Roman",20), textvariable=pic_entry)
image_entry.place(x = 40, y = 25, width = 400, height = 50)

load_image_button = Button(root, text = "Load image", command = load_image)
load_image_button.place(x = 25, y = 100, width = 200, height = 50)

save_image_button = Button(root, text = "Save image", command = save_image)
save_image_button.place(x = 250, y = 100, width = 200, height = 50)

#FILTERS

#left collumn
black_white_button = Button(root, text = "Black & White", command = apply_black_and_white)
black_white_button.place(x = 25, y = 200, width = 200, height = 50)

sepia_button = Button(root, text = "Sepia", command = sepia)
sepia_button.place(x = 25, y = 260, width = 200, height = 50)

invert_button = Button(root, text = "Invert", command = invert)
invert_button.place(x = 25, y = 320, width = 200, height = 50)

pointalise_button = Button(root, text = "Pointalise", command = pointillism)
pointalise_button.place(x = 25, y = 380, width = 200, height = 50)

#right collumn
line_drawing_button = Button(root, text = "Draw lines", command = line_drawing)
line_drawing_button.place(x = 250, y = 200, width = 200, height = 50)

crop_button = Button(root, text = "Crop", command = crop)
crop_button.place(x = 250, y = 260, width = 200, height = 50)

increase_contrast_button = Button(root, text = "Increase Contrast", command = increase_contrast)
increase_contrast_button.place(x = 250, y = 320, width = 200, height = 50)

pixelate_button = Button(root, text = "Pixelate", command = pixelated)
pixelate_button.place(x = 250, y = 380, width = 200, height = 50)



''' VIEW - Widgets That Display Visuals'''
canvas = Canvas(root, bg = "gray")
canvas.place(x = 490, y = 10, width = 500, height = 446)

save_load_label = Label(root, bg = "teal", text = "ENTER IMAGE NAME")
save_load_label.place(x = 50, y= 5, width = 400, height = 20)

save_load_label = Label(root, bg = "teal", text = "FILTERS:")
save_load_label.place(x = 50, y= 170, width = 400, height = 20)

info_label = Label(root, bg = "teal", text = "",fg = "orange")
info_label.place(x=100, y=440, width = 300, height = 20)

canvas.bind("<Button-1>", on_click)
canvas.bind("<B1-Motion>", on_drag)

root.mainloop()

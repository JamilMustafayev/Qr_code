import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import qrcode
from PIL import Image, ImageTk
root=tk.Tk()

root.geometry('450x430')
root.title("QR Code Generator")
qrcode_color= "black"

qrcode_image=None
def generate_qr_code():
    global qrcode_image
    text_data=text_box.get(1.0, tk.END)
    qr=qrcode.QRCode(border=1)
    qr.add_data(text_data)
    qr_img_obj=qr.make_image(fill_color= qrcode_color)
    qrcode_image=ImageTk.PhotoImage(qr_img_obj)
    
    #230x230
    if qrcode_image.height()>=230 or qrcode_image.width()>=230: 
   
        resize_qrcode=qr_img_obj.get_image().resize((230,230))
        qrcode_image=ImageTk.PhotoImage(resize_qrcode)
    
    qr_code_lb.config(image=qrcode_image)
        
def change_color(color):
    global qrcode_color
    qrcode_color=color
    generate_qr_code()
    

lb=tk.Label(root, text="Enter Any Information", font=("Bold", 12))
lb.pack(anchor=tk.W, pady=10)

text_box=ScrolledText(root, height=10, width=20, font=("Bold", 12))
text_box.pack(anchor=tk.W, padx=5)

generate_btn=tk.Button(root, text="Generate a QR Code", command=generate_qr_code)
generate_btn.pack(anchor=tk.W, pady=10, padx=5)


qr_frame=tk.Frame(root)

qr_img=tk.PhotoImage(file='image1.png')
qr_code_lb=tk.Label(qr_frame, image=None)
qr_code_lb.pack()

color_1=tk.Button( qr_frame, text="●", fg="red", font=("Bold", 50), bd=0,
                  command= lambda: change_color("red"))
color_1.place(x=0, y=280, width=40, height=40)

color_2=tk.Button( qr_frame, text="●", fg="blue", font=("Bold", 50), bd=0,
                  command= lambda: change_color("blue"))
color_2.place(x=40, y= 280, width=40, height=40)

color_3=tk.Button( qr_frame, text="●", fg="orange", font=("Bold", 50), bd=0,
                  command= lambda: change_color("orange"))
color_3.place(x=80, y=280, width=40, height=40)

color_4=tk.Button( qr_frame, text="●", fg="green", font=("Bold", 50), bd=0,
                  command= lambda: change_color("green"))
color_4.place(x=120, y=280, width=40, height=40)

color_5=tk.Button( qr_frame, text="●", fg="yellow", font=("Bold", 50), bd=0,
                  command= lambda: change_color("yellow"))
color_5.place(x=160, y=280, width=40, height=40)

color_6=tk.Button( qr_frame, text="●", fg="black", font=("Bold", 50), bd=0,
                  command= lambda: change_color("black"))
color_6.place(x=200, y=280, width=40, height=40)

save_qr_btn=tk.Button(qr_frame, text="Save QR Code as a Image")
qr_frame.place(x=200, y=20, width=240, height=400)

root.mainloop()


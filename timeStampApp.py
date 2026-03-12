#!/bin/env python3
# author: ph-u
# script: timeStampApp.py
# desc: click and record timestamp
# in: NA
# out: NA
# arg: NA
# date: 20260310

# https://medium.com/@sauravchakers/turn-your-python-code-into-a-desktop-app-in-four-easy-steps-ee9151b7068c
# http://stackoverflow.com/questions/51631105/ddg#51631176
# https://realpython.com/mobile-app-kivy-python/

import tkinter as tk
#from tkinter import messagebox
import datetime

def tStamp():
    return str(datetime.datetime.now()) #.split(' ')[1].split('.')[0]

##### GUI app #####
def tStamp_button():
    rEc = ";" + str(entry_length.get()) + " " + tStamp()
    entry_num.insert(0, rEc.replace(" ",","))
    return 0

def x2File_button():
    tX = entry_num.get().rstrip().replace(";","\n")
    nOw = tStamp().split('.')[0].replace(" ","_").replace(":","_")
    fNam = str(nam_entry.get()).replace(" ","_") + "_" + nOw + ".txt"
    with open(str(fNam), "w") as fIle:
        fIle.write(tX)
    return 0

def recDel_button():
    entry_num.delete(0, tk.END)
    return 0

## Main window
root = tk.Tk()
root.title("TimeZtamp")
root.geometry("400x500")
root.configure(bg = "maroon")

## Record name
nam_label = tk.Label(root, text = "Station name")
nam_label.pack(pady = 10)
nam_entry = tk.Entry(root)
nam_entry.pack(pady = 5)

## Clear previous timestamps
dd_entry = tk.Button(root, bg = "yellow", text = "Clear timestamps", command = recDel_button)
dd_entry.pack(pady = 20)

## In text
#tXt = tk.Label(root, text = "Boat numbers")
#tXt.grid(column = 0, row = 0)
#tXt_boat = tk.Entry(root, height = 10, width = 10, bg = "lightgray")
#tXt_boat.grid(column = 0, row = 1)
label_length = tk.Label(root, text = "Boat number")
label_length.pack(pady = 10)
entry_length = tk.Entry(root)
entry_length.pack(pady = 5)

## Generate button
button_generate = tk.Button(root, bg = "aqua", text = "Timestamp", command = tStamp_button)
button_generate.pack(pady = 5)
#button_generate.grid(column = 1, row = 1)

## Show timestamp
label_num = tk.Label(root, text = "Recorded timestamp")
label_num.pack(pady = 10)
#label_num.grid(column = 2, row = 0)
entry_num = tk.Entry(root, width = 40)
entry_num.pack(pady = 5)
#entry_num.grid(column = 2, row = 1)

## Copy to clipboard
cp_entry = tk.Button(root, text = "Export", command = x2File_button)
cp_entry.pack(pady = 3)

## Run application
root.mainloop()

##### CMD app #####
#def main():
#    timeStamp = tStamp()
#    print(timeStamp)

#if __name__ == "__main__":
#    main()

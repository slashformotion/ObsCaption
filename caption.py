import tkinter as tk
from tkinter import filedialog
import pathlib as pl


root = tk.Tk()
root.title("Caption")
frame = tk.Frame(root)
frame.pack()

### VARS

file_path = tk.StringVar()

# label = tk.Label(root,text = "A list of Grocery items.")
# label.pack()


def browse_button():
    filename = filedialog.askopenfile()
    file_path.set(filename.name)


def add():
    next_caption = etr_caption.get()
    print(next_caption)
    listbox.insert("end", next_caption)


def switch():
    txt = _get_selected()
    path = pl.Path(file_path.get())
    with path.open("w") as f:
        f.write(txt)


def _get_selected():
    selection = listbox.curselection()
    return listbox.get(selection[0])


def delete():
    selection = listbox.curselection()
    listbox.delete(selection[0])


leftframe = tk.Frame(root)
leftframe.pack(side=tk.LEFT)

rightframe = tk.Frame(root)
rightframe.pack(side=tk.RIGHT)

topframe = tk.Frame(root)
topframe.pack(side=tk.TOP)

lbl_path = tk.Label(topframe, textvariable=file_path)
lbl_path.pack()

etr_caption = tk.Entry(leftframe, width=20)

etr_caption.insert(0, "Caption")
etr_caption.pack(pady=5)

btn_add = tk.Button(rightframe, text="Add", command=add)
btn_delete = tk.Button(
    rightframe,
    text="Delete",
    bg="red",
    relief="groove",
    fg="light blue",
    command=delete,
)
btn_switch = tk.Button(rightframe, text="Switch", command=switch)
btn_add.pack()
btn_delete.pack()
btn_switch.pack()

listbox = tk.Listbox(leftframe)

listbox.pack()


if __name__ == "__main__":
    print(browse_button())
    root.mainloop()

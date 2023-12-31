import tkinter
import tkinter.messagebox
import pickle

root = tkinter.Tk()
root.title("To-Do List by Dipan")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="Warning!", message="You must enter a task.")


def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        if updated_task != "":
            listbox_tasks.delete(task_index)
            listbox_tasks.insert(task_index, updated_task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(title="Warning!", message="You must enter an updated task.")
    except IndexError:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Warning!", message="You must select a task.")


def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_tasks = tkinter.Listbox(frame_tasks, height=30, width=100)
listbox_tasks.pack(side=tkinter.LEFT)

scrollbar_tasks = tkinter.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tkinter.Entry(root,width=90)
entry_task.pack()

button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

button_update_task = tkinter.Button(root, text="Update task", width=48, command=update_task)
button_update_task.pack()


button_save_tasks = tkinter.Button(root, text="Save tasks", width=48, command=save_tasks)
button_save_tasks.pack()

root.mainloop()
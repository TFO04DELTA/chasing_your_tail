import tkinter as tk
import subprocess

def write_slogan():
    print("Checking Status")
    subprocess.call(["lxterminal", "-e", "bash -c '/home/pi/Desktop/chasing_your_tail/cyt/monitor.sh; read -p \"Press Enter to close...\"'"])
    
def func_delete_ignore():
    print("Deleting Ignore Lists")
    subprocess.call(["lxterminal", "-e", "bash -c '/home/pi/Desktop/chasing_your_tail/cyt/delete_ignore_lists.sh; read -p \"Press Enter to close...\"'"])
    
def func_create_ignore():
    print("Creating Ignore Lists")
    subprocess.call(["lxterminal", "-e", "bash -c 'python3 /home/pi/Desktop/chasing_your_tail/cyt/create_ignore_list.py; read -p \"Press Enter to close...\"'"])
    
def func_run_cyt():
    print("Running CYT")
    subprocess.call(["lxterminal", "-e", "bash -c '/home/pi/Desktop/chasing_your_tail/cyt/chasing_your_tail.sh; read -p \"Press Enter to close...\"'"])
    

root = tk.Tk()
root.title('Chasing Your Tail Viewer')
frame = tk.Frame(root)
frame.pack()

button_quit = tk.Button(frame, 
                       text="QUIT", 
                       width=15,
                       height=5,
                       fg="red",
                       relief="groove",
                       command=quit)
button_quit.pack(side=tk.LEFT)

check_status = tk.Button(frame,
                   text="Check Status",
                       width=15,
                       height=5,
                       fg="green",
                       relief="groove",
                       command=write_slogan)
check_status.pack(side=tk.LEFT)

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
    relief="groove",
    text="Delete Ignore Lists",
    width=15,
    height=5,
    fg="red",
    #bg="blue",
    #fg="yellow",
    command=func_delete_ignore)

button.pack(side=tk.LEFT)

create_ignore = tk.Button(frame,
                       width=15,
                       height=5,
                       text="Create Ignore Lists",
                       relief="groove",
                       command=func_create_ignore)
create_ignore .pack(side=tk.LEFT)


butn_run_cyt = tk.Button(frame,
                       width=16,
                       height=5,
                       fg="green",
                       text="Run Chasing Your Tail",
                       relief="groove",
                       command=func_run_cyt)
butn_run_cyt .pack(side=tk.LEFT)


root.mainloop()

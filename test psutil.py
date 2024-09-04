import psutil
import threading
import time
import ttkbootstrap as ttkbs
from tkinter import messagebox
import sys

def quitter_programme():
    if messagebox.askyesno("Quitter", "Voulez-vous vraiment quitter le programme ?"):
        app.destroy()
        sys.exit()

def surveiller_processeur():
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        #print(f"Utilisation du processeur : {cpu_percent}%")
        # update the amount used directly
        processeur_meter.configure(amountused = cpu_percent)
        time.sleep(1)

def surveiller_memoire():
    while True:
        memory_info = psutil.virtual_memory()
        #print(f"Utilisation de la RAM : {memory_info.percent}%")
        # update the amount used directly
        memoire_meter.configure(amountused = memory_info.percent)
        time.sleep(1)

def surveiller_disque():
    while True:
        partitions = psutil.disk_io_counters(perdisk=False)
        print(partitions.read_count)
        print(partitions.write_count)

        # update the amount used directly
        disque_read_meter.configure(amountused = partitions.read_count)
        time.sleep(1)

app = ttkbs.Window(themename="superhero")

# Définition de l'action à effectuer lors de la fermeture de la fenêtre
app.protocol("WM_DELETE_WINDOW", quitter_programme)

processeur_meter = ttkbs.Meter(
    metersize=200,
    amounttotal=100,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="Processeur en %",
    interactive=False,
    meterthickness=10
)
processeur_meter.pack()

memoire_meter = ttkbs.Meter(
    metersize=200,
    amounttotal=100,
    padding=5,
    amountused=25,
    metertype="semi",
    subtext="Mémoire en %",
    interactive=False,
    meterthickness=10
)
memoire_meter.pack()

disque_read_meter = ttkbs.Meter(
    metersize=200,
    amounttotal=50,
    padding=5000000,
    amountused=25,
    metertype="semi",
    subtext="Lecture du disque",
    interactive=False,
    meterthickness=10
)
disque_read_meter.pack()

thread_processeur = threading.Thread(target=surveiller_processeur)
thread_memoire = threading.Thread(target=surveiller_memoire)
thread_disque = threading.Thread(target=surveiller_disque)

thread_processeur.start()
thread_memoire.start()
thread_disque.start()

app.mainloop()

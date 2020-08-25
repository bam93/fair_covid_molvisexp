import struct
import socket
import tkinter as tk
from functools import partial
import zmq


class UMolCommand:
    def __init__(self):
        self.isConnected = False
        
    def connect(self, ip="localhost", port= 5555):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://"+ip+":"+str(port))
        self.isConnected = True

    def disconnect(self, ):
        # if self.isConnected:
            # self.s.close()
        self.isConnected = False

    def send(self, com):
        if self.isConnected:
            encodedCom = com.encode()
            # self.s.send(encodedCom)
            self.socket.send(encodedCom)
            message = self.socket.recv().decode()
            return message


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("UnityMol External UI")
        # self.pack()
        self.create_widgets()
        self.povButtons = []
        self.u = UMolCommand()
        self.u.connect()

    def create_widgets(self):
        self.refreshB = tk.Button(self)
        self.refreshB["text"] = "Load COVID-19 Fair Sharing Example 1"
        self.refreshB["command"] = self.loadFirst
        # self.refreshB.pack(side="top")
        self.refreshB.grid(row=0, column=0)

#        labeltit1 = tk.Label(self, text=" \n ")
#        labeltit1.grid(row=1, column=0)
#        self.refreshB.append(labelpov1)

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        self.rowconfigure(5, pad=3)
        self.rowconfigure(6, pad=3)
        self.rowconfigure(7, pad=3)
        self.rowconfigure(8, pad=3)
        self.rowconfigure(9, pad=3)
        self.rowconfigure(10, pad=3)
        self.pack()

    def loadFirst(self):
        self.u.send("Application.runInBackground = True")
        
        #self.u.send("loadScript('../baaden/ownCloud/fair_covid/ex1_spike/spike1.py')")
        self.u.send("print('Hello, I am connected!')")
        #self.u.send("fetch('1kx2')")

        #sels = self.u.send("getSelectionListString()")
        # self.selections = []

        for i in self.povButtons:
            i.destroy()

### FIRST BUTTON >> sends "0"
        buttopov1 = tk.Button(self)
        buttopov1["text"] = "Ex.1: Show"
        buttopov1["command"] = partial(self.sendPOV, 0)
        self.povButtons.append(buttopov1)
        # buttopov1.pack(side="top")
        buttopov1.grid(row=1, column=0)

        labelpov1 = tk.Label(self, text="spike-ACE2 interaction overview\n ")
        # labelpov1.pack(fill="x", side="right")
        #labelpov1.grid(row=1, column=1)
        labelpov1.grid(row=2, column=0)
        self.povButtons.append(labelpov1)

### SECOND BUTTON >> sends "1"
        buttopov2 = tk.Button(self)
        buttopov2["text"] = "Ex.1: Toggle ACE2 visibility"
        buttopov2["command"] = partial(self.sendPOV, 1)
        self.povButtons.append(buttopov2)
        #  buttopov1.pack(side="top")
        buttopov2.grid(row=4, column=0)
        labelpov2 = tk.Label(self, text="toggle on/off\n ")
        # labelpov1.pack(fill="x", side="right")
        labelpov2.grid(row=5, column=0)
        self.povButtons.append(labelpov2)


### THIRD BUTTON >> sends "2"
        buttopov3 = tk.Button(self)
        buttopov3["text"] = "Ex.1: Viewpoint from top"
        buttopov3["command"] = partial(self.sendPOV, 2)
        self.povButtons.append(buttopov3)
        # buttopov2.pack(side="top")
        buttopov3.grid(row=7, column=0)

        labelpov3 = tk.Label(self, text="spike-ACE2 interaction overview\n ")
        # labelpov2.pack(fill="x", side="right")
        self.povButtons.append(labelpov3)
        labelpov3.grid(row=8, column=0)

### FOURTH BUTTON >> sends "3"
        buttopov4 = tk.Button(self)
        buttopov4["text"] = "Ex.1: Toggle annotation"
        buttopov4["command"] = partial(self.sendPOV, 3)
        self.povButtons.append(buttopov4)
        # buttopov3.pack(side="top")
        buttopov4.grid(row=10, column=0)

        labelpov4 = tk.Label(self, text="toggle on/off\n \n ")
        # labelpov3.pack(fill="x", side="right")
        self.povButtons.append(labelpov4)
        labelpov4.grid(row=11, column=0)

### FIFTH BUTTON >> sends "4"
        buttopov5 = tk.Button(self)
        buttopov5["text"] = "View 2"
        buttopov5["command"] = partial(self.sendPOV, 4)
        self.povButtons.append(buttopov5)
        # buttopov3.pack(side="top")
        buttopov5.grid(row=13, column=0)
        
        labelpov5 = tk.Label(self, text="fusion peptide 2\n ")
        # labelpov3.pack(fill="x", side="right")
        self.povButtons.append(labelpov5)
        labelpov5.grid(row=14, column=0)

        self.pack()

        # if sels and len(sels) > 0:
        #     tmp = sels.replace("[","").replace("]","").split(", ")
        #     self.selections = [i for i in tmp if len(i.strip()) != 0]


        # self.selectionButtons = []
        # curid = 0
        # for i in self.selections:
        #     butto = tk.Button(self)
        #     butto["text"] = i
        #     self.selectionButtons.append(butto)
        #     butto.pack(side="top")
        #     butto["command"] = partial(self.printMe, curid)
        #     curid+=1

    def sendPOV(self, idPov):
        if idPov == 0:
            self.u.send("rep2off()")
            self.u.send("rep1()")
            self.u.send("view1()")
        elif idPov == 1:
            self.u.send("toggleRep('D.ACE','hb')")
        elif idPov == 2:
            self.u.send("view1b()")
            self.u.send("clearSelections()")
        elif idPov == 3:
            self.u.send("annot1(-1)")
        elif idPov == 4:
            self.u.send("rep1off()")
            self.u.send("rep2()")
            self.u.send("view2()")

    # def printMe(self, b):
    #     selName = self.selections[b]
    #     shown = self.u.send("areRepresentationsOn('"+selName+"', 'hb')")
    #     print(shown)
    #     if len(shown) > 0:
    #         shown = shown == "True"
    #     else:
    #         shown = True
    #     if not shown:
    #         command = "showSelection('"+selName+"', 'hb')"
    #     else:
    #         command = "hideSelection('"+selName+"', 'hb')"

    #     res = self.u.send(command)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
app.u.disconnect()
root.destroy()


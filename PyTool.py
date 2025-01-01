from tkinter import *
class Iterator:
    def __init__(self,data):
        self.data=data
        self.position=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.position>=len(self.data):
            raise StopIteration
        result=self.data[self.position]
        self.position+=1
        return result
def TimeFunc(func,type="print"):
    def wrapper(*args,**kwargs):
        import time
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        if type=="print":print("Time:",end-start)
        elif type=="return":return end-start
        elif type=="value":
            global FuncTime
            FuncTime=end-start
        elif type=="GUI":
            try:
                win=Tk()
                win.title("Time")
                win.geometry("200x100")
                Label(win,text="Time:"+str(end-start)).pack()
                win.mainloop()
            except ModuleNotFoundError:
                print("You need to install python")
    return wrapper
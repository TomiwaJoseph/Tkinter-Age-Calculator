from tkinter import *
from tkcalendar import DateEntry
from datetime import datetime
from tkinter.scrolledtext import ScrolledText


root = Tk


class Switch(root):
    def __init__(self):
        root.__init__(self)
        self._frame = None
        self.switch_frame(AgeCalculator)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.place(x=0,y=0,relheight=1,relwidth=1)


class StartPage(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        Frame.configure(self,bg='#222')
        self.root = root
        self.root.title('Intro Page')
        self.root.geometry('400x310')
        self.root.resizable(0,0)
        #======= Title =====================
        Label(self.master,text='Age Calculator',font='montserrat 35',fg='#505050',bg='#fff').place(x=25,y=83)
        Label(self.master,text='Age Calculator',font='montserrat 35',fg='#fff',bg='#222').place(x=25,y=80)
        #=========== Buttons ==================
        Button(self.master,text='Start',font='montserrat 18',bd=0,fg='yellow',bg='#222',command=lambda:self.master.switch_frame(AgeCalculator)).place(x=155,y=150)



class AgeCalculator(Frame):
    def __init__(self,root):
        Frame.__init__(self,root)
        Frame.configure(self,bg='#222')
        self.root = root
        self.root.title('Intro Page')
        self.root.geometry('580x330')
        self.root.resizable(0,0)

        Label(text='Input',bg='#222',fg='#fff',font='montserrat 16').place(x=30,y=20)
        Label(text='Results',bg='#222',fg='#fff',font='montserrat 16').place(x=450,y=20)#280

        self.main_frame = Frame(borderwidth=2,relief='ridge',width=220,height=245,bg='#fff')
        self.main_frame.place(x=20,y=60)
        Label(self.main_frame,text='Date of Birth:',bg='#fff',fg='teal',font='montserrat 12').place(x=30,y=20)
        self.dob_date = DateEntry(self.main_frame,width=12, background='teal',
                font='montserrat 12',foreground='white',borderwidth=5)
        self.dob_date.place(x=30,y=50)

        Label(self.main_frame,text='Target Date:',bg='#fff',fg='teal',font='montserrat 12').place(x=30,y=90)
        self.target_date = DateEntry(self.main_frame,width=12, background='teal',
                font='montserrat 12',foreground='white',borderwidth=5)
        self.target_date.place(x=30,y=120)

        Button(self.main_frame,text='Calculate',fg='#fff',bg='teal',width=13,bd=0,
            font='montserrat 14',command=self.calculate_it).place(x=27,y=160)

        self.result_frame = Frame(borderwidth=2,relief='ridge',width=300,height=245,bg='#fff')
        self.result_frame.place(x=260,y=60)

        self.results = Text(self.result_frame,fg='#fff',bg='#444',font='montserrat 14',
            width=22,height=9)
        self.results.place(x=3,y=2)

    def calculate_it(self):
        dob_date = self.dob_date.get_date()
        target_date = self.target_date.get_date()
        self.results.insert(END, 'something')

if __name__ == '__main__':
    app = Switch()
    app.mainloop()
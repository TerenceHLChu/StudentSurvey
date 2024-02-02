import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class StudentSurvey(tk.Tk): # Inherit from Tk
    def __init__(self):
        tk.Tk.__init__(self) # Invoke parent constructor
        self.title('Centennial College')
                
        frame = tk.Frame(self, width=50)
        frame.grid(row=0, column=0, padx=20, pady=20)
   
        # Display message box after OK is clicked
        def show_details():
            messagebox.showinfo("Information", nameEntry.get() + '\n' + 
                                               progDropdown.get() + '\n' + 
                                               radioRes.get() + '\n' + 
                                               comp100.get() + '\n' + 
                                               comp213.get() + '\n' + 
                                               comp120.get())     
        
        def set_defaults():
            nameEntry.delete(0, 'end')
            nameEntry.insert(0, 'Terence Chu')
            radioRes.set('dom')
            progDropdown.current(2)
            courseCheck1.select() 
            courseCheck2.deselect()
            courseCheck3.deselect()   
        
        surveyLabel = tk.Label(frame, text='ICET Student Survey', font=('Calibri', '24', 'bold', 'italic'))
        
        nameLabel = tk.Label(frame, text='Full name:')
        nameEntry = tk.Entry(frame)
        
        resLabel = tk.Label(frame, text='Residency:')
        radioRes = tk.StringVar()
        resRadio1 = tk.Radiobutton(frame, text='Domestic', variable=radioRes, value='dom')
        resRadio2 = tk.Radiobutton(frame, text='International', variable=radioRes, value='intl')
        
        programLabel = tk.Label(frame, text="Program:")
        program = tk.StringVar()
        progDropdown = ttk.Combobox(frame, textvariable=program)
        progDropdown['values'] = (['AI', 'Gaming', 'Health', 'Software'])
        
        courseLabel = tk.Label(frame, text="Courses:")
        comp100 = tk.StringVar()
        comp213 = tk.StringVar()
        comp120 = tk.StringVar()
        courseCheck1 = tk.Checkbutton(frame, text='Programming I', variable=comp100, onvalue='(COMP100)', offvalue='')
        courseCheck2 = tk.Checkbutton(frame, text='Web Design', variable=comp213, onvalue='(COMP213)', offvalue='')
        courseCheck3 = tk.Checkbutton(frame, text='Software Engineering', variable=comp120, onvalue='(COMP120)', offvalue='')
        
        resetButton = tk.Button(frame, text='Reset', command = set_defaults) # Call set_defaults method to restore form defaults
        okButton = tk.Button(frame, text='OK', command=show_details) # Call show_details method to display message box
        exitButton = tk.Button(frame, text='Exit', command=self.destroy)

        surveyLabel.grid(row=0, column=0, columnspan=3)
        
        nameLabel.grid(row=1, column=0, sticky='W')
        nameEntry.grid(row=1, column=1, sticky='W')
        
        resLabel.grid(row=2, column=0, sticky='W')
        resRadio1.grid(row=2, column=1, sticky='W')
        resRadio2.grid(row=3, column=1, sticky='W')
        
        programLabel.grid(row=4, column=0, sticky='W')
        progDropdown.grid(row=4, column=1, sticky='W')
        
        courseLabel.grid(row=5, column=0, sticky='W')
        courseCheck1.grid(row=5, column=1, sticky='W')
        courseCheck2.grid(row=6, column=1, sticky='W')
        courseCheck3.grid(row=7, column=1, sticky='W')
        
        resetButton.grid(row=8, column=0, sticky='nsew', padx=5)
        okButton.grid(row=8, column=1, sticky='nsew', padx=5)
        exitButton.grid(row=8, column=2, sticky='nsew', padx=5)
        
        # Set the defaults once all UI elements in place
        set_defaults()
        
        # Readjust widget positions as window resizes
        self.columnconfigure(0, weight=100)
        self.columnconfigure(1, weight=100)
        self.columnconfigure(2, weight=100)
        self.rowconfigure(0, weight=100)
        self.rowconfigure(1, weight=100)
        self.rowconfigure(2, weight=100)
        self.rowconfigure(3, weight=100)
        self.rowconfigure(4, weight=100)
        self.rowconfigure(5, weight=100)
        self.rowconfigure(6, weight=100)
        self.rowconfigure(7, weight=100)
        self.rowconfigure(8, weight=100)
            
        self.mainloop()
  
StudentSurvey()

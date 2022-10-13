from tkinter import *
from tkinter import filedialog
import re

special_char=re.compile('/\|')

root = Tk()
#button_9 = Button(label_key,text='9',height=3,width=5,font=('Helvetica','12'))
#button_9.grid(row=0,column=0)
class Calculator:
    def file_upload(self,numbers):
        global operator
        global var
        #self.operator = self.operator + str(numbers)
        #self.var.set(self.operator)
        tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Open Text file", 
        filetypes=(("All Files", "*.mpf"),)
        )
        self.var.set(tf)
        self.file=tf
        tf = open(tf)  # or tf = open(tf, 'r')
        data = tf.read()
        #print (data)
        

    def clear(self):
        if (len (self.file)<=0):
            print('Please Select a file first')
            return
        fil=open(self.file)
        content=fil.read()
        if (len (content)<=0):
            print('Empty File')
            return
        else:
            len1=0
            
            f= open("bazil.mpf","w+")
            print (len(content.split('\n')))
            line=''
            self.var.set("Processing...")
            i=0
            while(True):
                try:
                    print (content[i],end='')
                except IndexError:
                    break
                if (content[i]=='A'):
                    if (content[i+1]=='-'):
                        j=i+1
                        word=''
                        #print('finding negatives')
                        while (content[j]!=' '):
                            # print(content[j])
                            if (content[j]==' '):
                                print ("We are here")
                                break
                            else:
                                word+=content[j]
                            j+=1
                        len1=j-i
                        
                        #content[i]+=word
                        print('Negative Value: ', word)
                        if "\n" in word:
                            #print("New line")
                            wordl=word.splitlines()
                            word=wordl[0]
                            word=str(float(word)+360)
                            print('Optimised Value : ', word)
                            word='A'+word+'\n'+wordl[1]
                            content = content[:i] + word + content[i+len1:]
                        else:
                            word=str(float(word)+360)
                            print('Optimised Value : ', word)
                            word='A'+word
                            content = content[:i] + word + content[i+len1:]
                i+=1            

            f.write(content)
            self.var.set("Finished")

    ''' def delete(self):
        self.operator = str(self.entry.delete(len(self.entry.get())-1))
    '''


    def evaluate(self):
        self.answer =eval(self.entry.get())
        self.var.set(self.answer)
        self.operator = str(self.answer)

    def __init__(self,master):

        self.operator = ""
        self.file = ""
        self.var = StringVar()
        frame_s = Frame(master, height=500, width=500 )
        frame_s.pack(side=TOP, fill=BOTH, expand=True)
        self.entry = Entry(frame_s,textvariable=self.var,bg='grey',width=45,bd=20,insertwidth=4,justify='right',font=('arial',10,'bold'))
        self.entry.pack()
        self.t = Text(self.entry,height=40)



        label_key = Label(root, height=15, width=30,bd=10,bg='gray50')
        label_key.pack(side=LEFT, fill=BOTH, expand=True)

        label_fkey = Label(root, height=15, width=15, bg='gray25')
        label_fkey.pack(fill=BOTH, expand=True)

        label_7 = Label(label_key, bg='black')
        label_7.grid(row=0, column=0)
        button_7 = Button(label_7, text='Adjust Negatives', font=('Helvetica', '16'),command= lambda : self.clear(),bg='black',fg='cyan')
        button_7.pack()



        '''label_del = Label(label_fkey, bg ='black')
        label_del.grid(row=0,column=1,sticky=E)
        button_del = Button(label_del, text='del', font=('Helvetica', '16'),bd=3, height=1, width=3,command=  self.delete)
        button_del.pack()'''

        label_sub = Label(label_fkey, bg='black')
        label_sub.grid(row=1, column=0, sticky=W, pady=10)
        button_sub = Button(label_sub, text='Upload File', font=('Helvetica', '16'), height=1, width=10,command= lambda: self.file_upload('-'),bg='black',fg='cyan')
        button_sub.pack(side=LEFT)



c = Calculator(root)
root.title("Bazil\'s CNC Correction")
root.mainloop()
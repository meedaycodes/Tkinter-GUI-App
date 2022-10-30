## Tkinter-GUI-App

- The front_end.exe file for the app can be downloaded  in the  dist folder a of this repository
. It  also comes with a sqlite database which can be be wiped out and reused for storing other information  

### Design the Interface 
- This was the first task of building the app as it allows for  a pictorial illustration what would be contained in it
 in terms of dimensions of each button and functions we would like to perform on the app such as adding a new entry of 
 record to the database, query the database, delete entry from the database

### Coding The Front-End
- I used the Tkinter Library to build  the whole front end of this app. Tkinter was selected because it allows for building effective 
GUIs for users in short amount of time
- First the library was imported using pip, then a Tkinter window with the code below
```
window =Tk()

window.wm_title("PHONERECORD")

l1 = Label(window, text="Phone Name")
l1.grid(row=0, column=0)

phone_name_text = StringVar()
e1=Entry(window, textvariable=phone_name_text)
e1.grid(row=0,column=1)

list1=Listbox(window, height=8, width=65)
list1.grid(row=2,column=0,rowspan=12, columnspan=2)

b1 = Button(window, text="View All", width=15, command=view_command)
b1.grid(row=3, column=3)

window.mainloop()
``` 
- I created first a window which is an instance of the Tinker class object, then a title is given to the window frame created
- the window class id then populated with the elements (buttons, textboxes, scrollbar) relevant to use the app effectively
- See the front_end.py file for full front end code

### Coding the Back End

- The backend.py file contains the full code that was used to create the database for this application
- Sqlite was used as the database for this project, the sqlite library was first imported , then a connection was made with the sqlite database

```
def connect():
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phonerecord (id INTEGER PRIMARY KEY, phone_name TEXT, camera TEXT, launch_date DATE, battery TEXT, display_size TEXT, price FLOAT)")
    connected.commit()
    connected.close()

def insert(phone_name, camera, launch_date, battery, display_size, price):
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("INSERT INTO phonerecord VALUES (NULL, ?,?,?,?,?,?)",(phone_name, camera, launch_date, battery, display_size, price))
    connected.commit()
    connected.close()

```
### Connecting Front-end to Back-end
- The connection of the front-end to the back-end can be found in the  front-end.py file with series of python functions that gets executed 
when queries are made in the front end
```

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in backend.search(phone_name_text.get(), launch_date_text.get(), camera_text.get(),battery_text.get(), display_size_text.get(), price_text.get()):
        list1.insert(END, row)
```
### Building the .exe file with pyinstaller Library
- On completing the process of connecting both part of the applicattion  pyinstaller was installed to create a downloaded .exe file that can be used 
on both windows and machines. In this repo the .exe file can be found in the dist folder of the  file section

## THANK YOU

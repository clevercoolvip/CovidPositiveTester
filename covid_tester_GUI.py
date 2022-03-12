import pandas as pd

import wikipedia

data = pd.read_csv("covid.csv")
x = data.iloc[:, :-1].values
y = data.iloc[:, 6].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)


from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train, y_train)


from tkinter import *
window = Tk()
window.title("Covid_19")
lbl = Label(window, text="Covid positive tester!", font=("arial", 98, "bold"))
lbl.pack()

fever = Entry(window, bd=5, bg="powder blue", width=60)
fever.insert(0, "Temperature(in farenheit)")
fever.pack()

cold = Entry(window, bd=5, bg="powder blue", width=60)
cold.insert(0, "cold(if not type '0', if ,mild cold type '1', if severe type '2')")
cold.pack()

cough = Entry(window, bd=5, bg="powder blue", width=60)
cough.insert(0, "dry cough, yes type '1' or '0'")
cough.pack()

body_pain = Entry(window, bd=5, bg="powder blue", width=60)
body_pain.insert(0, "body pain(if not type '0', if ,mild cold type '1', if severe type '2'")
body_pain.pack()

aches = Entry(window, bd=5, bg="powder blue", width=60)
aches.insert(0, "Aches(if not type '0', if ,mild cold type '1', if severe type '2')")
aches.pack()

breathing = Entry(window, bd=5, bg="powder blue", width=60)
breathing.insert(0, "Breathing Problem(if not type '0', if ,mild cold type '1', if severe type '2')")
breathing.pack()

def onClick():
    a = fever.get()
    b = cold.get()
    c = cough.get()
    d = body_pain.get()
    e = aches.get()
    f = breathing.get()   
    rip = wikipedia.summary("Corona virus")
    predicted_value = model.predict(([[int(a), int(b), int(c), int(d), int(e), int(f)]]))
    if predicted_value<=0.102:
        
        text.insert(0.0, "Abhi na marra tu\n" + rip)
    elif predicted_value>0.102 and predicted_value<=0.108:
        text.insert(0.0, "Hmm positive ho skta h, check krwale!!\n" + rip)
    elif predicted_value>=0.109:
        text.insert(0.0, "Coffin dance meme!!!\n" + rip)
        
btn = Button(window, text="Predict", bd=10, bg="steel blue", command=onClick)
btn.pack()

text = Text(window, bd=10, bg="powder blue")
text.pack()


window.mainloop()
from tkinter import *
import edit_newspaper

class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


fields = (['ID',''], ['PW',''], ['기자이름','ex) 박진우 기자'], ['email',''])
articles = []

def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field[0], anchor='w')
        ent = Entry(row)
        ent.insert(10, field[1])
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field[0], ent))
    return entries


def showArticles(frame, articles):
    lb = Listbox(frame)
    for i in range(len(articles)):
        print(articles[i][0])
        lb.insert(i, articles[i][0])
    lb.pack(side=RIGHT, fill=X)
    

def set_articles(ent_keyword, frame, stop=50):
    global articles
    # print(keyword.get())
    articles = edit_newspaper.get_articles(ent_keyword.get(), stop)
    showArticles(frame, articles)


if __name__ == '__main__':
    
    root = Tk()
    root.title("따따시 귀찮아 죽겠네")

    ents = makeform(root, fields)
    
    keyword = Frame(root)
    keyword.pack(side=TOP, fill=X, padx=5, pady=5)
    lab_keyword = Label(keyword, width=15, text="용어", anchor='w').pack(side=LEFT)
    ent_keyword = Entry(keyword)
    ent_keyword.pack(side=LEFT, expand=YES, fill=X)
    # keyword_text = ent_keyword.get()
    
    
    
    description = Frame(root)
    description.pack(side=TOP, fill=X, padx=5, pady=5)
    lab_des = Label(description, width=15, height=20, text="설명", anchor='w').pack(side=LEFT)
    
    S = Scrollbar(description)
    T = Text(description, height=4, width=50)
    S.pack(side=RIGHT, fill=Y)
    T.pack(side=RIGHT, fill=Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)

    # print(T.get("1.0",END))
    
    
    article = Frame(root)
    article.pack(side=TOP, fill=X, padx=5, pady=5)
    lab_article = Label(article, width=15, text="기사", anchor='w').pack(side=LEFT)

    butt_search = Button(keyword, text='기사 검색', command=(lambda e=ent_keyword, f=article: set_articles(e, f)))
    butt_search.pack(side=RIGHT, padx=5, pady=5)

    # lng = Checkbar(article, articles)
    # lng.pack(side=TOP, fill=X)
    # lng.config(relief=GROOVE, bd=2)
    
    root.mainloop()

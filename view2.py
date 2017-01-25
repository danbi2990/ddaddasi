import tkinter as tk
import edit_newspaper as news

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fields_user_info = (['ID',''], ['PW',''], ['기자이름','ex) 박진우 기자'], ['email',''])
        self.pack(side="top", fill="both", expand=True)
        self.e_u = self.frame_user_info(self.fields_user_info)  # entries from user input
        self.e_k = self.frame_ddaddasi_keyword()    # entry ddaddasi keyword
        self.e_kd = self.frame_ddaddasi_description()   # entry ddaddasi description
        # print(self.e_u[2])

    def frame_user_info(self, fields):
        entries = []
        for field in fields:
            row = tk.Frame(self)
            lab = tk.Label(row, width=10, text=field[0], anchor='w')

            if field[0] == 'PW':
                ent = tk.Entry(row, show='*')
            else:
                ent = tk.Entry(row)

            ent.insert(0, field[1])
            if field[0] == 'ID':
                ent.focus_set()

            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries.append((field[0], ent.get()))
        return entries

    def frame_ddaddasi_keyword(self):
        row = tk.Frame(self)
        lab = tk.Label(row, width=10, text="용어", anchor='w')
        ent = tk.Entry(row)
        butt = tk.Button(row, text='기사 검색', command=(lambda e=ent: self.frame_articles(e)))

        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        butt.pack(side=tk.RIGHT, padx=5, pady=5)
        return ent.get()

    def frame_articles(self, ent, stop=20):
        # print(ent.get())
        # articles = news.get_articles(ent_keyword.get(), stop)
        articles = (('조선','기사제목1','http://chosun.com'),
                    ('중앙','기사제목2','http://joongang.com'),
                    ('중앙', '기사제목3', 'http://joongang.com'),
                    ('중앙', '기사제목4', 'http://joongang.com'))
        cnt = len(articles)
        isChecked = [tk.IntVar() for _ in range(cnt)]
        art = tk.Frame(self)
        lab = tk.Label(art, width=10, text="기사", anchor='w')
        butt = tk.Button(art, text='선택 완료', 
                         command=(lambda a=articles,c=cnt,i=isChecked: self.set_article_html(a,c,i)))
        
        for i in range(cnt):
            cbox = tk.Checkbutton(art, text=articles[i][0]+': '+articles[i][1]+'\n'+articles[i][2], 
                                  variable=isChecked[i])
            cbox.grid(column=1, row=i)
            # cbox.pack(side=tk.RIGHT)
        art.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.grid(column=0, row=0, sticky=tk.W)
        butt.grid(column=0, row=1)
        # print([x.get() for x in isChecked])

    def set_article_html(self, articles, cnt, isChecked):
        print([articles[x] for x in range(cnt) if isChecked[x].get() == 1])
        

    def frame_ddaddasi_description(self):
        des = tk.Frame(self)
        lab = tk.Label(des, width=10, height=20, text="설명", anchor='w')
        scr = tk.Scrollbar(des)
        tex = tk.Text(des, height=4, width=50)

        scr.config(command=tex.yview)
        tex.config(yscrollcommand=scr.set)

        des.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        scr.pack(side=tk.RIGHT, fill=tk.Y)
        tex.pack(side=tk.RIGHT, fill=tk.Y)

        return tex.get("1.0", tk.END)

    def show_articles(self, frame, articles):
        lb = tk.Listbox(frame)
        for i in range(len(articles)):
            print(articles[i][0])
            lb.insert(i, articles[i][0])
        lb.pack(side=tk.RIGHT, fill=tk.X)

    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("따따시 귀찮아 죽겠네")
    MainApplication(root)
    root.mainloop()

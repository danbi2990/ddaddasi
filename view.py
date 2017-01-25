import tkinter as tk
import webbrowser
import edit_newspaper as news
import upload_ddaddasi as up

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.fields_user_info = (['ID','sooahmin'], ['PW',''], ['기자이름','민수아 기자'], ['email','sooahmin09@gmail.com'])
        self.pack(side="top", fill="both", expand=True)
        self.e_u = [tk.StringVar() for _ in range(len(self.fields_user_info))]
        self.frame_user_info(self.fields_user_info)  # entries from user input
        self.e_k = tk.StringVar()
        self.frame_ddaddasi_keyword()    # entry ddaddasi keyword
        self.e_km = tk.StringVar()
        self.frame_ddaddasi_meaning()   # entry ddaddasi meaning
        self.e_kd = self.frame_ddaddasi_description()   # entry ddaddasi description
        # self.e_kd = tk.StringVar()
        # self.frame_ddaddasi_description()   # entry ddaddasi description
        # print(self.e_u[2])

    def frame_user_info(self, fields):
        entries = {}
        for i in range(len(fields)):
            row = tk.Frame(self)
            lab = tk.Label(row, width=10, text=fields[i][0], anchor='w')

            if fields[i][0] == 'PW':
                ent = tk.Entry(row, show='*', textvariable=self.e_u[i])
            else:
                ent = tk.Entry(row, textvariable=self.e_u[i])

            ent.insert(0, fields[i][1])
            if fields[i][0] == 'ID':
                ent.focus_set()

            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

    def frame_ddaddasi_keyword(self):
        row = tk.Frame(self)
        lab = tk.Label(row, width=10, text="용어", anchor='w')
        ent = tk.Entry(row, textvariable=self.e_k)
        butt = tk.Button(row, text='기사 검색', command=(lambda e=ent: self.frame_articles(e)))

        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        butt.pack(side=tk.RIGHT, padx=5, pady=5)
        # return ent.get()

    def frame_ddaddasi_meaning(self):
        row = tk.Frame(self)
        lab = tk.Label(row, width=10, text="한줄요약", anchor='w')
        ent = tk.Entry(row, textvariable=self.e_km)

        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        # return ent.get()

    def frame_articles(self, ent, stop=20):
        # print(ent.get())
        articles = news.get_articles(ent.get(), stop)
        # articles = (('조선','기사제목1','http://chosun.com'),
        #             ('중앙','기사제목2','http://joongang.joins.com'),
        #             ('중앙', '기사제목3', 'http://joongang.joins.com'),
        #             ('중앙', '기사제목4', 'http://joongang.joins.com'))
        cnt = len(articles)
        isChecked = [tk.IntVar() for _ in range(cnt)]
        art = tk.Frame(self)
        lab = tk.Label(art, width=10, text="기사", anchor='w')
        butt = tk.Button(art, text='업로드', 
                         command=(lambda a=articles,c=cnt,i=isChecked: self.set_article_html(a,c,i)))

        for i in range(cnt):
            cbox = tk.Checkbutton(art, text=articles[i][0]+': '+articles[i][1], variable=isChecked[i])
            link = tk.Label(art, text=articles[i][2], fg="blue")
            link.bind("<Button-1>", lambda event,e=articles[i][2]: self.open_url(event,e))
            cbox.grid(column=1, row=i*2)
            link.grid(column=1, row=i*2+1)
            # cbox.pack(side=tk.RIGHT)
        art.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.grid(column=0, row=0, sticky=tk.W)
        butt.grid(column=0, row=1)
        # print([x.get() for x in isChecked])

    def set_article_html(self, articles, cnt, isChecked):
        # self.fields_user_info = (['ID',''], ['PW',''], ['기자이름','ex) 박진우 기자'], ['email',''])
        # self.e_u; self.e_k; self.e_km; self.e_kd
        selected = [articles[x] for x in range(cnt) if isChecked[x].get() == 1]
        up.upload_ddaddasi(self.e_u[0].get(),self.e_u[1].get(),
                           self.e_u[2].get(),self.e_u[3].get(),
                           self.e_k.get(),self.e_km.get(),
                           self.e_kd.get("1.0", tk.END),selected)
        # print([articles[x] for x in range(cnt) if isChecked[x].get() == 1])

    def open_url(self, event, url):
        webbrowser.open_new(url)

    def frame_ddaddasi_description(self):
        des = tk.Frame(self)
        lab = tk.Label(des, width=10, height=20, text="설명", anchor='w')
        scr = tk.Scrollbar(des)
        # tex = tk.Entry(des, height=4, width=50, textvariable=self.e_kd)
        tex = tk.Text(des, height=4, width=50)

        scr.config(command=tex.yview)
        tex.config(yscrollcommand=scr.set)

        des.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        scr.pack(side=tk.RIGHT, fill=tk.Y)
        tex.pack(side=tk.RIGHT, fill=tk.Y)

        # return tex.get("1.0", tk.END)
        return tex


if __name__ == "__main__":
    root = tk.Tk()
    root.title("따따시 귀찮아 죽겠네")
    MainApplication(root)
    root.mainloop()

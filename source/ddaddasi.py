import pickle as pk
import tkinter as tk
import webbrowser
from multiprocessing import freeze_support
from urllib.parse import quote

from source import ffong_article_factory as af
from source import dda_upload_ddaddasi as up

# venv should be activated
# pyinstaller --onedir --windowed ddaddasi.py
# https://pythonhosted.org/PyInstaller/usage.html


class MainApplication(tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        try:
            fp = open("data.pkl", "rb")
        except FileNotFoundError:
            self.fields_user_info = (['ID', ''], ['PW', ''], ['기자이름', '박진우 기자'], ['email', ''])
        else:
            with fp:
                self.fields_user_info = pk.load(fp)

        self.pack(side="top", fill="both", expand=True)
        self.e_u = [tk.StringVar() for _ in range(len(self.fields_user_info))]
        self.frame_user_info(self.fields_user_info)  # entries from user input
        self.e_k = tk.StringVar()
        self.frame_ddaddasi_keyword()    # entry ddaddasi keyword
        self.e_km = tk.StringVar()
        self.frame_ddaddasi_meaning()   # entry ddaddasi meaning
        self.e_kd = self.frame_ddaddasi_description()   # entry ddaddasi description
        self.frame_article = tk.Frame(self)
        self.frame_article.pack()

    def frame_user_info(self, fields):
        for i in range(len(fields)):
            row = tk.Frame(self)
            lab = tk.Label(row, width=10, text=fields[i][0], anchor='w')

            if fields[i][0] == 'PW':
                ent = tk.Entry(row, show='*', textvariable=self.e_u[i])
            else:
                ent = tk.Entry(row, textvariable=self.e_u[i])

            ent.insert(0, fields[i][1])
            # if fields[i][0] == "ID":
            #     ent.focus_set()

            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)

    def search_definition(self, e):
        eve = None
        quoted_keyword = quote(e.get())
        url_naver = "http://terms.naver.com/search.nhn?query={}&searchType=&dicType=&subject=".format(quoted_keyword)
        url_wiki = "https://ko.wikipedia.org/wiki/{}".format(quoted_keyword)
        self.open_url(eve, url_naver)
        self.open_url(eve, url_wiki)

    def frame_ddaddasi_keyword(self):
        row = tk.Frame(self)
        lab = tk.Label(row, width=10, text="용어", anchor='w')
        ent = tk.Entry(row, textvariable=self.e_k)
        ent.focus_set()

        # butt1 = tk.Button(row, text='정의 검색', command=(lambda e=ent: self.search_definition(e)))
        butt2 = tk.Button(row, text='기사 검색', command=(lambda e=ent: self.search_article(e)))

        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        butt2.pack(side=tk.RIGHT, padx=5, pady=5)
        # butt1.pack(side=tk.RIGHT, padx=5, pady=5)

        # return ent.get()

    def frame_ddaddasi_meaning(self):
        row = tk.Frame(self)
        lab = tk.Label(row, width=10, text="한줄요약", anchor='w')
        ent = tk.Entry(row, textvariable=self.e_km)

        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)
        # return ent.get()

    def popup(self, txt):
        top = tk.Toplevel()
        lab = tk.Label(top, text=txt, height=20, width=50)
        lab.pack()

    def search_article(self, ent):
        # signal_q.put(ent.get())
        # articles = af.get_articles(ent.get(), result_q)
        articles = af.get_articles(ent.get())

        # articles = (('조선','기사제목1','http://chosun.com'),
        #             ('중앙','기사제목2','http://joongang.joins.com'),
        #             ('중앙', '기사제목3', 'http://joongang.joins.com'),
        #             ('중앙', '기사제목4', 'http://joongang.joins.com'))
        cnt = len(articles)
        top = tk.Toplevel()
        top.geometry("%dx%d%+d%+d" % (600, 600, 250, 125))

        if cnt:
            is_checked = [tk.IntVar() for _ in range(cnt)]
            canvas = tk.Canvas(top, borderwidth=0)
            art = tk.Frame(canvas)
            scr = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
            scr.config(command=canvas.yview)
            canvas.config(yscrollcommand=scr.set)
            canvas.bind_all("<MouseWheel>", lambda event: self._on_mousewheel(event, canvas))

            canvas.pack(side="left", fill="both", expand=True)
            art.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            scr.pack(side="right", fill="y")
            canvas.create_window((0, 0), window=art, anchor="nw")

            art.bind("<Configure>", lambda event, canvas=canvas: self.onFrameConfigure(canvas))

            butt = tk.Button(art, text='선택',
                             command=(lambda a=articles, c=cnt, i=is_checked: self.insert_article(a, c, i)))
            butt2 = tk.Button(art, text='닫기', command=lambda w=top: w.destroy())

            for i in range(cnt):
                cbox = tk.Checkbutton(art, text=articles[i]["publisher"]+': '+articles[i]["title"], variable=is_checked[i]) if articles[i]["title"] else tk.Label(art, text=articles[i]["publisher"])
                link = tk.Label(art, text=articles[i]["url"], fg="blue")
                link.bind("<Button-1>", lambda event,e=articles[i]["url"]: self.open_url(event,e))
                cbox.grid(column=1, row=i*2, sticky=tk.W if articles[i]["title"] else tk.N)
                link.grid(column=1, row=i*2+1)

            butt.grid(column=0, row=0)
            butt2.grid(column=0, row=1)
        else:
            lab = tk.Label(top, text="기사가 없습니다.", height=20, width=50)
            lab.pack()

    def onFrameConfigure(self, canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))

    def _on_mousewheel(self, event, canvas):
        canvas.yview_scroll(-1 * (event.delta // 120), "units")

    def insert_article(self, articles, cnt, isChecked):
        art = self.frame_article
        for w in art.winfo_children():
            w.destroy()
        selected = [articles[x] for x in range(cnt) if isChecked[x].get() == 1]

        butt = tk.Button(art, text='업로드',
                         command=(lambda s=selected: self.upload_article(s)))
        butt2 = tk.Button(art, text='종료', command=lambda w=self.parent:w.destroy())

        for idx, article in enumerate(selected):
            lab = tk.Label(art, text=article["publisher"] + ': ' + article["title"])
            link = tk.Label(art, text=article["url"], fg="blue")
            link.bind("<Button-1>", lambda event, e=article["url"]: self.open_url(event, e))
            lab.grid(column=0, row=idx * 2, sticky=tk.W)
            link.grid(column=0, row=idx * 2 + 1)
        butt.grid(column=1, row=0)
        butt2.grid(column=1, row=1)

    def upload_article(self, selected):
        try:
            code = up.upload_ddaddasi(self.e_u[0].get(), self.e_u[1].get(), self.e_u[2].get(),
                                      self.e_u[3].get(), self.e_k.get(), self.e_km.get(),
                                      self.e_kd.get("1.0", tk.END), selected)
            if code == 200:
                top = tk.Toplevel()
                fr = tk.Frame(top)
                lab = tk.Label(fr, text="업로드 완료!", width=20)
                link = tk.Label(fr, text="Click << 확인하기", fg="blue")
                link.bind("<Button-1>",
                          lambda event, e="http://www.danbinews.com/member/myHome.html": self.open_url(event, e))
                butt = tk.Button(fr, text="닫기", command=lambda w=top: w.destroy())
                fr.pack(expand=True, fill=tk.X, padx=5, pady=5)
                lab.pack()
                link.pack()
                butt.pack()

                data = (["ID", self.e_u[0].get()],["PW", self.e_u[1].get()],
                        ["기자이름", self.e_u[2].get()],['email', self.e_u[3].get()])
                f = open("data.pkl", 'bw')
                pk.dump(data, f)
                f.close()

        except Exception as e:
            txt = e.args
            top = tk.Toplevel()
            lab = tk.Label(top, text=txt)
            lab.pack()
            butt = tk.Button(top, text="닫기", command=lambda w=top: w.destroy())
            butt.pack()

    def open_url(self, event, url):
        webbrowser.open_new(url)

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
        tex.pack(side=tk.RIGHT, fill=tk.BOTH, expand=tk.YES)
        return tex


# class WebDrivers(threading.Thread):
#     def __init__(self):
#         super().__init__()
#         self.web_driver = None
#
#     def run(self):
#         self.web_driver = webdriver.PhantomJS('./phantomjs/bin/phantomjs')
#
#
# def new_process(sig_q, res_q):
#     wd = [WebDrivers() for _ in range(4)]
#     for w in wd:
#         w.start()
#
#     for w in wd:
#         w.join()
#
#     # print(len(wd))
#
#     while True:
#         if not sig_q.empty():
#             keyword = sig_q.get()
#             if keyword == "q":
#                 break
#             else:
#                 res_q.put(af.get_articles_child(wd, keyword))
#
#     for w in wd:
#         try:
#             w.web_driver.quit()
#         except OSError:
#             pass


if __name__ == "__main__":
    freeze_support()
    root = tk.Tk()
    root.title("따따시 귀찮아 죽겠네")
    main = MainApplication(root)

    # signal_q = Queue()
    # result_q = Queue()
    # p = Process(target=new_process, args=(signal_q, result_q))
    # p.start()

    root.mainloop()
    # signal_q.put('q')
    # p.join()

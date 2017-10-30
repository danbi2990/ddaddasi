# <span style="color:red">*Warning*</span>: This program is only for the *members* of [danbinews](http://www.danbinews.com/)

# What is it?
It helps the members to upload 'ddaddasi' to the website.  
'ddaddasi' roughly means 'news terminology' in Korean. ([따끈따끈 시사용어](http://www.danbinews.com/news/articleList.html?sc_section_code=S1N10))

# How to build
- Install Python 3.6
- Create & Activate virtual environment
- pip install -r requirements.txt
- Navigate to ddaddasi/source directory
- pyinstaller --onedir --windowed ddaddasi.py
  - https://pythonhosted.org/PyInstaller/usage.html

# How it works
- Assume you want to find info about 'IMF' (International Monetary Fund)
- The program crawls the newspaper websites and scraps articles including the keyword
- Here're the websites it crawls
  - Khan(경향), Hani(한겨래), ChoSun(조선), Joins(중앙), DongA(동아), Seoul(서울), NewSis(뉴시스), HanKyung(한국경제), 
  MaeKyung(매일경제), Herald(헤럴드), NewsOne(뉴스원), MunHwa(문화일보)

# Branch *multiprocessing*
In most cases, it works well with plain *requests* module. However, some websites must be crawled by phantomjs.
(HanKook(한국), KookMin(국민), YonHap(연합), SeoKyung(서울경제))
  
*The problem is that phantomjs slows down the program.* That's why the master branch excludes the functionality.

To mitigate it, the branch *multiprocessing* forks a child process on starting
and the child creates 4 threads of phantoms.
while an user filling inputs, the phantoms will be initialised and ready. 

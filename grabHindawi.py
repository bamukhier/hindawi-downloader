from bs4 import BeautifulSoup
import requests
import os
import shutil
import eel

eel.init("web")
downloaded = 0
progress = 0
one_percent = 1

'''
def update_progress():
    global downloaded, progress, one_percent
    downloaded += 210
    if downloaded % one_percent == 0:
        progress += 10


def set_complete_progress():
    global progress
    progress = 100


@eel.expose
def return_progress():
    global progress
    return progress
'''


@eel.expose
def download(ext):
    dom = "https://www.hindawi.org/books/"
    homepage = requests.get(dom)
    homepage_html = homepage.text
    init_soup = BeautifulSoup(homepage_html, "html.parser")
    num_books_el = init_soup.select('#lnkAllbooks > span[class=count]')[0]
    total_books_num = int(num_books_el.text.strip())
    num_of_pages = -(-total_books_num // 10) + 1
    one_percent = -(-total_books_num // 100)

    currentDir = os.path.dirname(
        os.path.realpath(__file__))  # directory of script
    dir = os.path.join(currentDir, "مكتبة-هنداوي")

    try:
        if os.path.exists(dir):
            shutil.rmtree(dir)
        os.makedirs(dir)
    except OSError:
        pass

    domain = "https://www.hindawi.org"
    for i in range(1, num_of_pages):
        p_num = "/books/{}/".format(i)
        p_url = domain + p_num
        page = requests.get(p_url)
        print(i)
        html = page.text
        soup = BeautifulSoup(html, "html.parser")
        books = soup.select(".details")
        for book in books:
            a_tag = book.find('a')
            extension = ext
            url = domain + a_tag.attrs['href'][:-1] + "." + extension
            print(url)
            mtitle = a_tag.text.translate(
                {ord(c): " " for c in "!@#$%^&*[]{};,:./<>?\|`~=+"})
            title = mtitle.strip()
            mauthor_tag = book.find(class_="author")
            author_tag = mauthor_tag.find('a')
            if (author_tag):
                author = author_tag.text
            else:
                author = "مجهول"

            f_name = "[{}] {} .{}".format(author, title, extension)
            f_path = os.path.join(dir, f_name)
            res = requests.get(url, stream=True)
            with open(f_path, "wb") as file:
                for chunk in res.iter_content(chunk_size=None):
                    if chunk:
                        file.write(chunk)

    return True


eel.start("index.html",  size=(550, 560))

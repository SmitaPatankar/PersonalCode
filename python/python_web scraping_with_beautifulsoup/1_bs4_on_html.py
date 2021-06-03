# pip install beautifulsoup4
# pip install lxml

from bs4 import BeautifulSoup

with open("sample.html", "r") as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.findAll("div", class_="card")
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f"{course_name} costs {course_price}")
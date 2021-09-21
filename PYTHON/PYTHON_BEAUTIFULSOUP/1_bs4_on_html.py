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

# headers = {"User-Agent": "Mozilla/5.0"}
# content is bytes, text is text - content is better
# find, find_all
# select_one, select
# # id
# . class
# tag
# find and .get("attr")

# bs4.element
# bs4.element.ResultSet

# str.ljust(30)

# string="xx"

# find_parents
# find_parent
# .get_text(strip=True)

# ul
# ol
# li

# table
# tr
# th/td

# div section span input a p

# find_next_sibling/s
# find_previous_sibling/s

# find_next()
# find_all_next()

# find_previous()
# find_all_previous()

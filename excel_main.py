from turtle import update
from bs4 import BeautifulSoup

from excel import write_excel, update_excel


with open("test.xml", "r") as f:
    data = f.read()

soup = BeautifulSoup(data, "lxml")

books = [
    [
        "bookmark",
        "p",
        "node",
        "topics",
    ]
]

bookmark = []
tag3 = soup.find_all("w:p")
for key, value in enumerate(tag3):
    bookmark.append({"id": int(key), "value": value.find("w:t")})

# print(subjects)
file_name = "test1"
range_name = "A"
value = bookmark
col_names = [
    {"key": "A", "col": 1, "col_name": "raw_data"},
    {"key": "B", "col": 1, "col_name": "Headings"},
]
excel_write = write_excel(file_name, range_name, col_names, value)

Heading = []
ListParagraph = []
background2 =[]
tag3 = soup.find_all("w:p")
for key, value in enumerate(tag3):
    if "Heading" in str(value):
        Heading.append({"id": key, "value": value.find("w:t")})
    if "ListParagraph" in str(value):
        ListParagraph.append({"id": int(key), "value": value.find("w:t")})
    if "background2" in str(value):
        background2.append({"id": int(key), "value": value.find("w:t")})

# print(subjects)
file_name = "test1"
range_name = "B"
value1 = Heading

col_names = [
    {"key": "A", "col": 1, "col_name": "raw_data"},
    {"key": "B", "col": 1, "col_name": "Headings"},
    {"key": "C", "col": 1, "col_name": "ListParagraph"},
]

excel_update_headings = update_excel(file_name, range_name, col_names, value1)

file_name = "test1"
range_name = "C"
value2 = ListParagraph

col_names = [
    {"key": "A", "col": 1, "col_name": "raw_data"},
    {"key": "B", "col": 1, "col_name": "Headings"},
    {"key": "C", "col": 1, "col_name": "ListParagraph"},
]

excel_update_headings = update_excel(file_name, range_name, col_names, value2)

file_name = "test1"
range_name = "d"
value3= background2

col_names = [
    {"key": "A", "col": 1, "col_name": "raw_data"},
    {"key": "B", "col": 1, "col_name": "Headings"},
    {"key": "C", "col": 1, "col_name": "ListParagraph"},
     {"key": "d", "col": 1, "col_name": "background2"},
]

excel_update_headings = update_excel(file_name, range_name, col_names, value3)

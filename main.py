from bs4 import BeautifulSoup

from gsheets import GSheets
SPREADSHEET_ID = '15pz3wEi5geQmbOLODkcWY1V5k4E1xpVPEhmx9DB2q_A'
RANGE_NAME = 'Sheet2!B2:b'

with open('beginningcplusplusgameprogramming(1).xml', 'r') as f:
    data = f.read()

soup = BeautifulSoup(data, 'lxml')

books = [['bookmark',
          'p',
          'node',
          'topics',
    

]]

bookmark = [['bookmark', ]]
tag3 = soup.find_all('bookmark')
for key, value in enumerate(tag3):
    bookmark.append([str({"id": key, "value": value['title']})])

# print(subjects)
RANGE_NAME = 'Sheet2!a1:A'
gspread = GSheets(SPREADSHEET_ID, RANGE_NAME)
gspread.auth()
gspread.write_from_top(bookmark)

topics = [['topics', ]]
tag2 = soup.find_all('p')
for key, value in enumerate(tag2):
    topics.append([str({"id": key, "value": value})])

# print(topics)
RANGE_NAME = 'Sheet2!b1:b'
gspread = GSheets(SPREADSHEET_ID, RANGE_NAME)
gspread.auth()
gspread.write_from_top(topics)

images = [['figures', ]]
tag4 = soup.find_all('figure')
for key, value in enumerate(tag4):
    images.append([str({"id": key, "value": value})])

print(images)
RANGE_NAME = 'Sheet2!C1:C'
gspread = GSheets(SPREADSHEET_ID, RANGE_NAME)
gspread.auth()
gspread.write_from_top(images)


nodes = [['node', ]]
tag5 = soup.find_all('node')
for key, value in enumerate(tag5):
    nodes.append([str({"id": key, "value": value})])

print(nodes)
RANGE_NAME = 'Sheet2!D1:D'
gspread = GSheets(SPREADSHEET_ID, RANGE_NAME)
gspread.auth()
gspread.write_from_top(nodes)

    




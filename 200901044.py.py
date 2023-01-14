from xml.dom import minidom
import csv
xmldoc = minidom.parse('compiler.xml')
book_list = []
for book in xmldoc.getElementsByTagName('book'):
    BOOK = book.getAttribute('id')
    AUT_NAME = book.getElementsByTagName('author')[0].firstChild.nodeValue
    TIT = book.getElementsByTagName('title')[0].firstChild.nodeValue
    GENRE = book.getElementsByTagName('genre')[0].firstChild.nodeValue
    PRI = book.getElementsByTagName('price')[0].firstChild.nodeValue
    PUBLISH = book.getElementsByTagName('publish_date')[0].firstChild.nodeValue
    DES = book.getElementsByTagName('description')[0].firstChild.nodeValue
    book_list.append([BOOK,AUT_NAME,TIT,GENRE,PRI,PUBLISH,DES])

with open('200901044.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Book_id','Author_Name','Title','Genre','Price','Publish_date','Description'])
    for book in book_list:
        writer.writerow(book)
print("File created")

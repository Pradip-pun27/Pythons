from bs4 import BeautifulSoup

with open('web.html','r') as file:
    contents =file.read()
    soup=BeautifulSoup(contents,'lxml')
    p_tags_contents=soup.find_all('p')
    print(f"Paragraphs  are")
    for paragraph in p_tags_contents:
        print(paragraph.text)

    print(f"\nHeadings are")
    h_tags_contents=soup.find_all('h1')
    for heading in h_tags_contents:
        print(heading.text)

    for heading in h_tags_contents:
        position =heading.text.split()[-2]
        print(position)
    
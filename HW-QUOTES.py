

from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
# pip install plotly
# pip install pandas
import plotly.express as px


# Request in case 404 Forbidden error


#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}



# print(soup.title.text)

quotes = []
authors = []
tags = []

for i in range(1,11):
    url = 'http://quotes.toscrape.com/page/'+str(i)+'/'
    # print(url)
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    table_quote = soup.findAll("span", {"class":{"text"}})
    table_author = soup.findAll("small", {"class":{"author"}})
    table_tags = soup.findAll("a", {"class":{"tag"}})
    # below is before I realized I didn't have to link tags to authors+quotes. Phew!
    # table_tags = soup.findAll("a", "content")
    # print(table_tags)
    # table_tags = soup.findAll("meta", {"class":{"keywords"}})
    # print(table_tags[1].content, ":D")

    for z in range(len(table_quote)):
        # url = 'http://quotes.toscrape.com/page/1/'
        
        temp_tags_list = []
        quotes.append(table_quote[z].text)
        authors.append(table_author[z].text)
        # below is again my many attempts at linking tags to authors
        # temp_tags_list.append(table_tags[z].text)
        # tags.append(temp_tags_list)
        # print(table_tags[z].text)
        # for y in table_tags[z]:
        #     print(table_tags[z].text)
        #     input()
        #     temp_tags_list.append(y.text)
        # tags.append(table_tags[z].text)
        # print(":D")
        # tags.append(temp_tags_list)
    for z in range(len(table_tags)):
        tags.append(table_tags[z].text)

# print(quotes)
# print(authors)
# print(tags)

# Author Statistics

# make a dictionary

authordict = {}

for i in authors:
    if i in authordict:
        tempnum = authordict[i]
        tempnum += 1
        authordict.update({i:tempnum})
    else:
        authordict.update({i:1})
    
# sort it

authordict_sorted = sorted(authordict.items(), key = lambda x:x[1], reverse = True)

print(f"Author with the maximum amount of quotes: {authordict_sorted[0][0]}, Amount of quotes: {authordict_sorted[0][1]}\n")
print(f"Author with the minimum amount of quotes: {authordict_sorted[-1][0]}, Amount of quotes: {authordict_sorted[-1][1]}\n")

# Quote analysis
longestquote = ""
shortestquote = "Put a lot of words here so that the shortest quote isn't just an empty string. There's probably a better way around this that I haven't found."
lenallquotes = 0
for i in quotes:
    lenallquotes += len(i)
    if len(i)>len(longestquote):
        longestquote = i
    if len(i)<len(shortestquote):
        shortestquote = i

meanallquotes = lenallquotes/len(quotes)

print(f"Mean length of all quotes: {meanallquotes} characters\n")
print(f"Shortest quote: {longestquote}\n")
print(f"Longest quote: {shortestquote}\n")

# tag analysis

tagdict = {}
for i in tags:
    if i in tagdict:
        tempnum = tagdict[i]
        tempnum += 1
        tagdict.update({i:tempnum})
    else:
        tagdict.update({i:1})
    # print(i)

# print(tagdict)

tagdict_sorted = sorted(tagdict.items(), key = lambda x:x[1], reverse = True)

print(f"Number of tags used across quotes: {len(tagdict_sorted)}")
# print(tagdict_sorted)
print(f"Most popular tag: {tagdict_sorted[0][0]}, number of times used: {(tagdict_sorted)[0][1]}")

# print(authordict.values(), authordict.keys())

first10authors = []
first10authorsquotes = []

for i in authordict_sorted[0:9]:
    first10authors.append(i[0])
    first10authorsquotes.append(i[1])
fig = px.bar(x=first10authors, y=first10authorsquotes)
fig.update_xaxes(type='category')
fig.show()

first10tags = []
first10tagsnumber = []

for i in tagdict_sorted[0:9]:
    first10tags.append(i[0])
    first10tagsnumber.append(i[1])
fig = px.bar(x=first10tags,y=first10tagsnumber)
fig.update_xaxes(type='category')
fig.show()
# authordict = {"person":1}

# if "person" in authordict:
#     tempnum = authordict["person"]
#     tempnum += 1
#     authordict.update({"person":tempnum})

# print(authordict)

# for i in range(len(authors)):
#     pass
# for i in table_rows:
#     print(i.text)
#     print(":D")

# for i in table_quote:
#     print(i.text)

# for i in table_author:
#     print(i.text)

    # for j in i:
    #     print(j.text)
    #     print("HI")
    #     for k in j:
    #         print(str(k).replace("\n", ""))
    #         print(":D")
from bs4 import BeautifulSoup
import requests

# with open("website.html") as f:
#     contents = f.read()

# soup = BeautifulSoup(contents, "html.parser")

# if you need to use lxml parser instead:
# import lxml
# soup = BeautifulSoup(contents, "lxml")

# print(soup)  # print entire html content
# print(soup.prettify())  # prints it with indenting
# print(soup.title)  # <title>Angela's Personal Site</title>
# print(soup.title.name)  # title
# print(soup.title.string)  # Angela's Personal Site

# print(soup.a)  # returns the FIRST anchor tag it finds
# print(soup.p)  # returns the FIRST <p> tag it finds

# print(soup.find_all(name="a"))  # find all anchor tags, returns as a list
# print(soup.find_all(name="p")[1])

# for tag in soup.find_all(name="a"):
#     # print(tag.getText())  # print text inside each anchor tag
#     print(tag.get("href"))  # get all href attributes

# print(soup.find(name="h1", id="name"))  # find first match
# print(soup.find(id="name"))  # find first match

# when search for classes need to use class_ (with underscore) in order
# to not clash with class attribute
# heading = soup.find(name="h3", class_="heading")  # find first match
# print(heading)
# print(heading.name)
# print(heading.string)
# print(heading.getText())
# print(heading.get("class"))

# find an <a> tag inside a <p> tag and return the first result:
# company_url = soup.select_one(selector="p a")
# print(company_url)

# find id=name
# print(soup.select_one(selector="#name"))

# find first class="heading"
# print(soup.select_one(selector=".heading"))

# find all class="heading"
# print(soup.select(selector=".heading"))


response = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(response.text, "html.parser")

# get title of each article:
# article_titles = soup.select(".storylink")
# for title in article_titles:
#     print(title.getText())

# first_article_a_tag = soup.find(name="a", class_="storylink")
# article_title = first_article_a_tag.getText()
# article_link = first_article_a_tag.get("href")
# print(article_title)
# print(article_link)

# score = soup.find(name="span", class_="score")
# article_score = score.getText()

# print(article_score)


articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article in articles:
    article_texts.append(article.getText())
    article_links.append(article.get("href"))

# scores = soup.find_all(name="span", class_="score")
# article_scores = [int(score.getText().split()[0]) for score in scores]

# Method above is from course
# this this actually failed as there was a new article posted with no score
# so length of lists don't align
# logic error in how it is parsed does not account for this scoreless entry

# method below from course somments works:

subtexts = soup.find_all(name="td", class_="subtext")
article_scores = []
for subtext in subtexts:
    score = subtext.find(name="span", class_="score")
    if score:
        article_scores.append(int(score.getText().split()[0]))
    else:
        article_scores.append(0)


# print(article_texts)
# print(article_links)
# print(article_scores)

# get highest score:
high_score_index = article_scores.index(max(article_scores))
print(article_texts[high_score_index])
print(article_links[high_score_index])

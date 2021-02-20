from bs4 import BeautifulSoup

import requests


# URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# sometime after Feb 5, 2021 the site chagned and requires a JS script
# to excute in order to present list, as such using requests.get
# on the above URL wwon't get any content.  So instead we'll use
# the internet archive wayback machine:
# included page in git as "page.html" for futuren reference incase it
# changes again or goes away from web archive

URL = (
    "https://web.archive.org/web/20210205074131/"
    "https://www.empireonline.com/movies/features/best-movies-2/"
)
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

# to avoid multiple hits on site as I am building and testing copy
# site to file, the open and scrape from file during development:

# with open("page.html", "w") as f:
#     f.write(soup.prettify())

# with open("page.html") as f:
#     soup = BeautifulSoup(f.read(), "html.parser")


titles_tags = soup.find_all(name="h3")
titles = [title.getText().strip() for title in titles_tags]
titles.reverse()

# could of  used `titles[::-1]` instead

# could just write the above, but ...
# some titles aren'it fomratted correctly, so we can fix that
# 1 and 49 have no number
# 12 has : instead of )
# 93 has number 2

titles_only = []
for index, title in enumerate(titles):
    if title[0].isnumeric():
        titles_only.append(f"{index+1}) {title.split(' ', 1)[1]}\n")
    else:
        titles_only.append(f"{index+1}) {title}\n")


with open("movies.txt", "w") as f:
    f.writelines(titles_only)

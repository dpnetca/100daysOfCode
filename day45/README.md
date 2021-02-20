# Day 45

Back to Python

today we are doing web scraping with Beautiful Soup

For the final challenge, our project is to scrape https://www.empireonline.com/movies/features/best-movies-2/ to get a list of the top 100 movies, and save them to a txt file from 1 - 100. However, sometime after Feb 5, 2021 the site changed and requires a JS script to excute in order to present list, as such using requests.get on the above URL won't get the desired content. So instead we'll use the internet archive wayback machine: "https://web.archive.org/web/20210205074131/https://www.empireonline.com/movies/features/best-movies-2/"

I included the results of this page in this repo as "page.html" for future reference incase it changes again or goes away from web archive

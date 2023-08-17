# %%
# import plotly
# import plotly.graph_objs as go

# import pandas as pd
# import numpy as np
# import json
# import plotly.express as px

# import requests
# from bs4 import BeautifulSoup
# import random

# %%

def get_medium_articles():

    # urls={'medium':'https://medium.com/@jaden09/list/mlops-b4ecfadf718c/archive/{0}/{1:02d}/{2:02d}'}

    # def convert_day(day):
    #     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #     m = 0
    #     d = 0
    #     while day > 0:
    #         d = day
    #         day -= month_days[m]
    #         m += 1
    #     return (m, d)
    
    # def get_claps(claps_str):
    #     if (claps_str is None) or (claps_str == '') or (claps_str.split is None):
    #         return 0
    #     split = claps_str.split('K')
    #     claps = float(split[0])
    #     claps = int(claps*1000) if len(split) == 2 else int(claps)
    #     return claps

    # url='https://medium.com/@jaden09/list/mlops-b4ecfadf718c'
    # response=requests.get(url)
    # data = []

    # Check if the request was successful
    # if response.status_code == 200:
    # Parse the HTML content using Beautiful Soup
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     articles = soup.find_all(
    #         "div",
    #         class_="postArticle postArticle--short js-postArticle js-trackPostPresentation js-trackPostScrolls")
    #     Find a specific element by tag and class
    #     for article in articles:
    #         title = article.find("h3", class_="graf--title")
    #         if title is None:
    #             continue
    #         title = title.contents[0]
    #         subtitle = article.find("h4", class_="graf--subtitle")
    #         subtitle = subtitle.contents[0] if subtitle is not None else ''
    #         reading_time = article.find("span", class_="readingTime")
    #         reading_time = 0 if reading_time is None else int(reading_time['title'].split(' ')[0])
    #         claps = get_claps(article.find_all("button")[1].contents[0])
    #         article_url = article.find_all("a")[3]['href'].split('?')[0]

    #         data.append(title,subtitle,reading_time,claps,article_url)


    data = {'titles':['Tom', 'Brad', 'Kyle'],
        'links':['a1', 'a2', 'a3'],
        }
    outputs=zip(tuple(data['titles']),tuple(data['links']))
    return outputs
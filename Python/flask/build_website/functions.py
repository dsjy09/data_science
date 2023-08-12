
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

def medium_articles():

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

    data = {'titles':['Tom', 'Brad', 'Kyle'],
        'links':['a1', 'a2', 'a3'],
        }
    outputs=zip(tuple(data['titles']),tuple(data['links']))
    return outputs
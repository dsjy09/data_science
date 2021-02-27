import matplotlib.pyplot as plt
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import iplot, init_notebook_mode
from plotly import figure_factory as ff
from plotly.subplots import make_subplots

class data_visulization():

    def __init__(self,project_name,dataset_name,work_project_name):
        self.project=project_name
        self.dataset=dataset_name
        self.workdir=work_project_name
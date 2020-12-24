#%% [markdown]

# ## Dash and plotly- interactive dashboard for data quality
# ### created on 2020/05/27, updated on 2020/12/17

#%% 
from collections import namedtuple
from google.cloud import bigquery
import pandas as pd
import IPython
import re
import matplotlib.pyplot as plt

import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.offline import iplot, init_notebook_mode
from plotly import figure_factory as ff
from plotly.subplots import make_subplots

# Using plotly + cufflinks in offline mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)

# Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
from jupyter_dash import JupyterDash
from dash.dependencies import Input, Output

# Click
import click
import sys

#%%

#@click.command()
#@click.option('--cdm_project_id',default='som-rit-phi-starr-prod', help='CDM data location')
#@click.option('--work_project_id ',default='som-rit-phi-starr-dev', help='name of google cloud project')
#@click.option('--work_dataset_id',default='jaden_extensive_qc', help='name of the working dataset under gcp')

cdm_project_id = 'som-rit-phi-starr-prod'
#cdm_project_id = 'som-rit-starr-training'
work_project_id = 'som-rit-phi-starr-dev'
#work_project_id = 'som-nero-phi-rit'
work_dataset_id = 'Jaden_extensive_qc'

client = bigquery.Client(project=work_project_id)

client1 = bigquery.Client(project=cdm_project_id)
project1=client1.project
datasets=list(client1.list_datasets())
print(project1)

lst=[]
##List Datasets and Tables in project
if datasets:
    for dataset in datasets:  # API request(s)
        lst.append(format(dataset.dataset_id))
# %%
prefix='starr_omop_cdm5_deid_1pcent_lite'
num=-5

cdm_alldatasets=[]
for i in lst:
    if i.startswith(prefix) and re.search(r'\d{4}_\d{2}_\d{2}$',i):
        cdm_alldatasets.append(i)
cdm_dataset_id_list=cdm_alldatasets[num:]
n=len(cdm_dataset_id_list)
cdm_dataset_id_list
# %% [markdown]
# ## Demographics

person_counts=pd.DataFrame(columns=['date','counts'])
ageds=pd.DataFrame(columns=['date','age_in_years'])
gender_counts=pd.DataFrame(columns=['date','gender','counts','percent'])
race_counts=pd.DataFrame(columns=['date','race','counts','percent'])
eth_counts=pd.DataFrame(columns=['date','ethnicity','counts','percent'])

for i in range(0,n):
    cdm_dataset_id=cdm_dataset_id_list[i]
    print(cdm_dataset_id)
    date=cdm_dataset_id.split('_')[-3]+'_'+cdm_dataset_id.split('_')[-2]+'_'+cdm_dataset_id.split('_')[-1]
    
    # Number of people
    sql="""
    select 
     '{date}' as date,
     row_count as counts
     from 
     `{cdm_project_id}.{cdm_dataset_id}.__TABLES__`
     where table_id='person'
    """.format_map({'cdm_project_id': cdm_project_id,
                    'cdm_dataset_id': cdm_dataset_id,
                    'date': date})
    query_job =client.query(sql)
    countds=query_job.to_dataframe()
    person_counts=person_counts.append(countds)   

    if i==n-1:
        # Age distribution
        sql= """
        SELECT
        '{date}' as date,
        date_diff(current_date,date(birth_DATETIME),year) as age_in_years
        FROM `{cdm_project_id}.{cdm_dataset_id}.person`
        """.format_map({'cdm_project_id': cdm_project_id,
                        'cdm_dataset_id': cdm_dataset_id,
                        'date': date})
    
        query_job =client.query(sql)
        agetmpds=query_job.to_dataframe()
        ageds=ageds.append(agetmpds)  

        # Number of people by gender
        sql="""
            SELECT
            '{date}' as date,
            concept.CONCEPT_NAME AS gender,
            COUNT(person.person_ID) AS counts
            FROM
            `{cdm_project_id}.{cdm_dataset_id}.person` as person
            INNER JOIN
            `{cdm_project_id}.{cdm_dataset_id}.concept` as concept
            ON
            person.GENDER_CONCEPT_ID = concept.CONCEPT_ID
            GROUP BY concept.CONCEPT_NAME
        """.format_map({'cdm_project_id': cdm_project_id,
                        'cdm_dataset_id': cdm_dataset_id,
                        'date': date})
        query_job =client.query(sql)
        countds=query_job.to_dataframe()
        countds=countds[countds['gender']!='No matching concept']
        countds['percent']=round(countds['counts']/sum(countds['counts'])*100,1)
        gender_counts=gender_counts.append(countds)

        # Number of people by race
        sql="""
            SELECT
            '{date}' as date,
            concept.CONCEPT_NAME AS race,
            COUNT(person.person_ID) AS counts
            FROM
            `{cdm_project_id}.{cdm_dataset_id}.person` as person
            INNER JOIN
            `{cdm_project_id}.{cdm_dataset_id}.concept` as concept
            ON
            person.race_CONCEPT_ID = concept.CONCEPT_ID
            GROUP BY concept.CONCEPT_NAME
        """.format_map({'cdm_project_id': cdm_project_id,
                        'cdm_dataset_id': cdm_dataset_id,
                        'date': date})
        query_job =client.query(sql)
        countds=query_job.to_dataframe()
        countds=countds[countds['race']!='No matching concept']
        countds['percent']=round(countds['counts']/sum(countds['counts'])*100,1)
        race_counts=race_counts.append(countds)

        # Number of people by ethnicity
        sql="""
            SELECT
            '{date}' as date,
            concept.CONCEPT_NAME AS ethnicity,
            COUNT(person.person_ID) AS counts
            FROM
            `{cdm_project_id}.{cdm_dataset_id}.person` as person
            INNER JOIN
            `{cdm_project_id}.{cdm_dataset_id}.concept` as concept
            ON
            person.ethnicity_CONCEPT_ID = concept.CONCEPT_ID
            GROUP BY concept.CONCEPT_NAME
        """.format_map({'cdm_project_id': cdm_project_id,
                        'cdm_dataset_id': cdm_dataset_id,
                        'date': date})
        query_job =client.query(sql)
        countds=query_job.to_dataframe()
        countds=countds[countds['ethnicity']!='No matching concept']
        countds['percent']=round(countds['counts']/sum(countds['counts'])*100,1)
        eth_counts=eth_counts.append(countds)

#%%
totalpatfig = px.bar(person_counts, x="date", y="counts",text='counts')
totalpatfig .update_traces(texttemplate='%{text:.2s}',textposition='outside')
totalpatfig.show()

#%%
gender_counts=gender_counts.sort_values(by=['percent'],ascending=True)
genderfig = px.bar(gender_counts, x="date", y="counts", color="gender",text='percent',width=600)
genderfig.update_layout(barmode='group')
genderfig.update_layout(legend=dict(orientation="h", yanchor="bottom",y=1.02,xanchor="right",x=1))
genderfig.show()

#%%
race_counts=race_counts.sort_values(by=['percent'],ascending=True)
racefig = px.bar(race_counts, x="date", y="counts", color="race",text='percent')
racefig.update_layout(barmode='group')
racefig.update_layout(legend=dict(orientation="h", yanchor="bottom",y=1.02,xanchor="right",x=1))
racefig.show()

eth_counts=eth_counts.sort_values(by=['percent'],ascending=True)
ethfig = px.bar(eth_counts, x="date", y="counts", color="ethnicity",text='percent')
ethfig.update_layout(barmode='group')
ethfig.update_layout(legend=dict(orientation="h", yanchor="bottom",y=1.02,xanchor="right",x=1))
ethfig.show()

agefig = px.box(ageds, x="date", y="age_in_years")
agefig.show()
# %%
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = JupyterDash('YourAppExample',external_stylesheets=external_stylesheets)

app.layout = html.Div([
    
    html.H1(children='Starr omop interactive data dashboard application',style={'textAlign':'center'}),
    
    dcc.Tabs(id="tabs",children=[
        dcc.Tab(label='Starr Omop general information', value='tab-1'),
        dcc.Tab(label='Demographics of stanford omop population', value='tab-2'),
        dcc.Tab(label='Condition occurrence', value='tab-3'),
        dcc.Tab(label='Device exposure',value='tab-4'),
        dcc.Tab(label='Drug exposure',value='tab-5'),
        dcc.Tab(label='Measurement',value='tab-6'),
        dcc.Tab(label='Procedure occurrence',value='tab-7'),
        dcc.Tab(label='Visit detail',value='tab-8'),
        dcc.Tab(label='Other tables',value='tab-9')
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])

def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            
            html.H4('Observation medical outcomes partnership common data model (OMOP CDM)'),
            html.Div([
                html.Label(['The OMOP Common Data Model allows for the systematic analysis of disparate observational databases. The concept behind this approach is to transform data contained within those databases into a common format (data model) as well as a common representation (terminologies, vocabularies, coding schemes), and then perform systematic analyses using a library of standard analytic routines that have been written based on the common format. More details about OHDSI and OMOP please refer ', html.A('link', href='https://www.ohdsi.org/')]),
                html.Br()
            ]),

            html.H4('Starr Omop-observational medical outcomes partnership stanford research data repository'),
            html.Div([
                html.Label(['A new clinical data platform, which is first fully de-identified EHR data from Epic clarity in observational health data science informatics (OHDSI) observational medical outcomes partnership (OMOP) common model. More details about starr omop please refer: ', html.A('link', href='https://med.stanford.edu/starr-omop.html')]),
                html.Br(),
                html.Label(['Starr omop training tutorials: ', html.A('link', href='https://www.youtube.com/channel/UC6iGiAO1dKwuC2wOrxnKiNw')]),
                html.Br(),
                html.P('Starr omop office hour: Every other Wednesday 3-4pm')
            ]),                
                
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Number of people'),
            
            dcc.Graph(id='total',
                figure=totalpatfig
            ),
            
            html.H3('Gender distribution'),
            
            dcc.Graph(id='gender',
                figure=genderfig
            ),
            
            html.H3('Race distribution'),
            
            dcc.Graph(id='race',
                figure=racefig
            ),
            
            html.H3('Ethnicity distribution'),
            
            dcc.Graph(id='eth',
                figure=ethfig
            ),
            
            html.H3('Age distribution'),
            
            dcc.Graph(id='age',
                figure=agefig
            ),
            
        ])    
app.run_server(mode='external')
# %%

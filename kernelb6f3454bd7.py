# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from google.cloud import bigquery

import bq_helper
from bq_helper import BigQueryHelper
stackOverflow = bq_helper.BigQueryHelper(active_project="bigquery-public-data",
                                   dataset_name="stackoverflow")

bq_assistant = BigQueryHelper("bigquery-public-data", "stackoverflow")
bq_assistant.list_tables()
tables = ['badges','comments','post_history','post_links','posts_answers','posts_moderator_nomination','posts_orphaned_tag_wiki','posts_privilege_wiki','posts_questions','posts_tag_wiki','posts_tag_wiki_excerpt','posts_wiki_placeholder','stackoverflow_posts','tags','users','votes']
for t in tables:
    tag=bq_assistant.head(t, num_rows=5000)
    tag.to_csv('stackoverflow_'+t+'.csv') 


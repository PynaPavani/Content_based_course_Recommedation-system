
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity,linear_kernel
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer

st.title('Course Recommendation App')
st.header('Get Recommendations foe given course!')
df=pd.read_csv('Coursera.csv')
df.rename(columns={'Course Name':'Name','Course Description':'Description'},inplace=True)
df['final']=df['Name']+' '+df['Description']+' '+df['Skills']

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf=TfidfVectorizer(stop_words='english')
df['final']=df['final'].fillna(' ')
mat=tfidf.fit_transform(df['final'])
score=cosine_similarity(mat)
index=pd.Series(df.index,index=df['Name']).drop_duplicates()

def get_recommendations(title, cosine_sim=score):
    idx = index[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:4]
    courses = [i[0] for i in sim_scores]

    return (df['Name'].iloc[courses],df['Course URL'].iloc[courses])

title=st.text_input('Enter Course Name','')
if title:
    st.write(get_recommendations(title))



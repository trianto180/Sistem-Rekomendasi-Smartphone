from django.shortcuts import render, redirect
from rekomendasi.models import Smartphone
from rekomendasi.models import smartphone_recomm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings

import pandas as pd
import pymysql
import os
from sqlalchemy import create_engine
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer


# Create your views here.
def smartphone(request):
    smartphones = Smartphone.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(smartphones, 10)
    try:
        smartphones = paginator.page(page)
    except PageNotAnInteger:
        smartphones = paginator.page(1)
    except EmptyPage:
        smartphones = paginator.page(paginator.num_pages)


    konteks = {
        'smartphones': smartphones,
    }
    return render(request, 'smartphone.html', {'smartphones': smartphones}, konteks)

def res(request):
    smartphone_l=[]
    smartphone_id_var=int(request.GET['smartphone_id'])
    num_recomm_var=int(request.GET['num_recomm'])
  
    

    print(os.getcwd())
    db_connection_str = 'mysql+pymysql://root:@localhost/smartphone'
    db_connection = create_engine(db_connection_str)
    smartphone_df = pd.read_sql('SELECT * FROM rekomendasi_smartphone', con=db_connection)    
    
    smartphone_df['metadata'] = smartphone_df[['storage', 'cpu', 'gpu','os','weight','battery','display']].agg(' '.join, axis=1)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(smartphone_df['metadata'])
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    results = {}

    for idx, row in smartphone_df.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[:-1000:-1]
        similar_items = [(cosine_similarities[idx][i], smartphone_df['id'][i]) for i in similar_indices]

        results[row['id']] = similar_items[1:]
    
    print('done!')


    def item(id):
        return smartphone_df.loc[smartphone_df['id'] == id]['model'].tolist()[0].split('br')[0]
    
    # Just reasmartphone_df the results out of the dictionary.
    def recommend(item_id, num):
        print("Recommending " + str(num) + " products similar to " + item(item_id) + "...")
        recs = results[item_id][:num]
        
        for rec in recs:
            print("Recommended: " + item(rec[1]) + " (score:" + str(rec[0]) + ")")
            smartphone_l.append(item(rec[1]))
            t=smartphone_recomm(smartphone_name=item(rec[1]),ram=item(rec[1]), cos_sim=float(rec[0]))
            t.save()
    recommend(smartphone_id_var,num_recomm_var)
    d={'smartphone_id':smartphone_l}
    print('Over')
    print(smartphone_l)

    smartphones=smartphone_recomm.objects.order_by('-date')[:6]
    print(smartphones)
    

    return render(request,'rekomendasi.html',{'smartphones_dict':smartphones})



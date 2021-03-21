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
    if 'q' in request.GET:
        q=request.GET['q']
        smartphones=Smartphone.objects.filter(model__icontains=q)
    else:
        smartphones = Smartphone.objects.all()
    page = request.GET.get('page')

    paginator = Paginator(smartphones, 10)
    try:
        smartphones = paginator.page(page)
    except PageNotAnInteger:
        smartphones = paginator.page(1)
    except EmptyPage:
        smartphones = paginator.page(paginator.num_pages)
    smartphone_obj=paginator.get_page(smartphones)
    return render(request, 'smartphone.html', {'smartphones': smartphone_obj})

 
def res(request):
    smartphone_l=[]
    smartphone_id_var=int(request.GET['smartphone_id'])
    num_recomm_var=int(request.GET['num_recomm'])

    print(os.getcwd())
    db_connection_str = 'mysql+pymysql://root:@localhost/smartphone'
    db_connection = create_engine(db_connection_str)
    smartphone_df = pd.read_sql('SELECT * FROM rekomendasi_smartphone', con=db_connection)    
    
    smartphone_df['metadata'] = smartphone_df[['storage','ram','cpu', 'gpu','os','battery','display']].agg(' '.join, axis=1)
    tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
    tfidf_matrix = tf.fit_transform(smartphone_df['metadata'])
    cosine_similarities = linear_kernel(tfidf_matrix, tfidf_matrix)

    results = {}

    for idx, row in smartphone_df.iterrows():
        similar_indices = cosine_similarities[idx].argsort()[-7::1]
        similar_items = [(cosine_similarities[idx][i], smartphone_df['id'][i]) for i in similar_indices]

        results[row['id']] = similar_items[1:]

    def item(id):
        return smartphone_df.loc[smartphone_df['id'] == id]['id']
        
    # Just reasmartphone_df the results out of the dictionary.
    def recommend(item_id, num):
        recs = results[item_id][:num]
        
        for rec in recs:
            smartphone_l.append(item(rec[1]))
            t=smartphone_recomm(smartphone_id=float(rec[1]), cos_sim=float(rec[0]))
            t.save()
    recommend(smartphone_id_var,num_recomm_var)
    d={'smartphone_id':smartphone_l}

    smartphones = smartphone_recomm.objects.order_by('-id')[:6]
    smart = smartphone_recomm.objects.order_by('-id')[:1]

    return render(request,'rekomendasi.html',{'smartphones_dict':smartphones, 'smart':smart})
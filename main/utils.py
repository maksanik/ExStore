# from django.db import models
from django.db.models import Q

def q_search(products, query: str):
    keywords = [word for word in query.split() if len(word) > 2]
    
    q_objs = Q()
    for token in keywords:
        q_objs |= Q(name__icontains=token)
        q_objs |= Q(description__icontains=token)
    
    return products.filter(q_objs)
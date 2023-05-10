from django.shortcuts import render
from .search_call import search
from newsapi import NewsApiClient

def search_index(request):
    results = []
    search_term = ""
    context = {'results': {}, 'count': 0, 'search_term': 'empty'}
    if request.GET.get('keyword'):
        search_term = request.GET['keyword']
        results = search(query = search_term, topN = 20)
        print(results)
        context = {'results': results[1], 'count': results[0], 'search_term':  search_term}
    return render(request,  'index.html',  context)

def home(request):
    newsapi = NewsApiClient(api_key='867e32f683c34cd2a89ffd7be01ed367')
    top = newsapi.get_top_headlines(sources='techcrunch')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'home.html', context={"mylist": mylist})
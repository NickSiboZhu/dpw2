from django.shortcuts import render
from .search_call import search
# from newsapi import NewsApiClient
# from serpapi import BaiduSearch


def search_index(request):
    return render(request,  'index.html')


def search_results(request):
    results = []
    search_term = ""
    context = {'results': {}, 'count': 0, 'search_term': 'empty'}
    if request.GET.get('keyword'):
        search_term = request.GET['keyword']
        results = search(query = search_term, topN = 20)
        print(results)
        context = {'results': results[1], 'count': results[0], 'search_term':  search_term}
    return render(request, 'result.html', context)


from serpapi import BaiduSearch

from serpapi import BaiduSearch

def news(request):
    params = {
        "engine": "baidu",
        "q": "小米",
        "device": "mobile",
        "api_key": "56cf54155fb9f8d738c3452372112c053c6218be01833cdb1be5d864289c9022"
    }

    search = BaiduSearch(params)
    results = search.get_dict()

    # Print the results dictionary
    print(results)

    # Check if 'news_results' is in the dictionary before trying to access it
    if 'news_results' in results:
        news_results = results["news_results"]
    else:
        news_results = []  # If not, use an empty list

    news = []
    desc = []
    img = []
    link = []

    for result in news_results:
        news.append(result.get('title'))
        desc.append(result.get('source'))
        img.append(result.get('thumbnail'))
        link.append(result.get('link'))

    mylist = zip(news, desc, img, link)

    return render(request, 'news.html', context={"mylist": mylist})





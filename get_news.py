from newsapi import NewsApiClient

# Initialize newsapi
newsapi = NewsApiClient(api_key='5559eb5deca648729d54101cdac5f192')

def get_news(name):
    top_headlines = newsapi.get_everything(q=name,
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)
    return(top_headlines)
import requests

from PyInquirer import prompt, print_json


def display_news():

    question = [
        {
            'type': 'list',
            'name': 'news_source',
            'message': 'what is your favourite news source',
            'choices': [

                    {
                        'name': 'cbc-news'
                    },
                {
                        'name': 'abc-news'
                },
                {
                        'name': 'al-jazeera-english'
                },
                {
                        'name': 'hacker-news'
                }
            ]
        },

        {
            'type': 'confirm',
            'name': 'news',
            'message': 'are you sure'

        }
    ]
    answers = prompt(question)
    new = answers['news_source']  # getting key
    if len(new) == 0:
        raise ValueError("you didnt select a news source")

    print(new)

    news = ['cbc-news', 'abc-news', 'al-jazeera-english', 'hacker-news']
    for source in news:
        if source == new:
            url = 'https://newsapi.org/v2/top-headlines?sources=' + \
                new+'&apiKey=7fef7425eb0b42bdbd842220fa9ff604'
            rdata = requests.get(url)
            if rdata.status_code == 400:
                return ('headlines not aviable')

            print('status:', rdata.status_code)
            response_data = rdata.json()
            headlinearticles = response_data['articles']

            for article in headlinearticles:
                print("Title : ", article['title'])
                print("Description : ", article['description'])
                print("url : ", article['url'], "\n")


display_news()

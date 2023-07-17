import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.titleline > a')
votes = soup.select('.score')

soup2 = BeautifulSoup(res2.text, 'html.parser')
links2 = soup2.select('.titleline > a')
votes2 = soup2.select('.score')

mega_links = links + links2
mega_subtext = votes + votes2
#subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
  return sorted(hnlist, key= lambda k:k['votes'], reverse=True)

def create_custom_hn(links,votes):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get('href',None)
        score = votes[idx].getText()
      #  vote = subtext[idx].select('.score')
        if len(score):
            points = int(score.replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': score})
    return sort_stories_by_votes(hn)

print(create_custom_hn(mega_links,mega_subtext))

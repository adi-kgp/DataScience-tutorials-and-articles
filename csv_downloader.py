import requests
url = 'https://raw.githubusercontent.com/WillKoehrsen/Data-Analysis/35b18efab2925357ad1c9385c0d5ed300297c835/plotly/data/blue_jays.csv'
res = requests.get(url, allow_redirects=True)
with open('sales_team.csv','wb') as file:
    file.write(res.content)
    

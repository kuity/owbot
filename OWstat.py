import requests

lootboxURL = 'https://api.lootbox.eu/'

def getUserStats(tag, platform='pc', region='us', mode='competitive-play', hero='allHeroes'):
    rstring = '{}{}/{}/{}/{}/{}/'.format(lootboxURL, platform, region, tag, mode, hero)
    print(rstring)
    r = requests.get(rstring)
    print(r.status_code)
    print(r.headers['content-type'])
    print(r.text)
    print(r.json())

getUserStats('Starblaze-3945')

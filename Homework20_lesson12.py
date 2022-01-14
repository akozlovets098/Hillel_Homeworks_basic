import json

with open('DPPBVV1U.json') as file:
    source = json.loads(file.read())
    list_of_episodes = source['_embedded']['episodes']
    print('Total duration of all episodes is', sum([list_of_episodes[i]['runtime'] for i in range(len(list_of_episodes))]), 'minutes', end='\n\n')
    for episode in list_of_episodes:
        print(episode['season'], episode['number'], sep='/')
        print(episode['name'], )
        print(episode['summary'].strip('</p>'))
        print(episode['url'])
        print('*******************************', end='\n')

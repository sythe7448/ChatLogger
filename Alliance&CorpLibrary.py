import evelink.api

charNames = 'anna niedostepny,lquid drisseg'
b = 'lquid drisseg,'

eve = evelink.eve.EVE()
charResponse = eve.character_ids_from_names(charNames)
#print charResponse.result

ids = charResponse.result

#print ids['Anna niedostepny']

eve = evelink.eve.EVE()
affResponse = eve.character_info_from_id(ids['Anna niedostepny'])
print affResponse.result['name']
print affResponse.result['alliance']['name'], affResponse.result['alliance']['id']
print affResponse.result['corp']['name'], affResponse.result['corp']['id']

import evelink.api

charNames = [
    'Anna niedostepny',
    'Lquid Drisseg'
]

charNamesString = ','.join(charNames)

eve = evelink.eve.EVE()
charResponse = eve.character_ids_from_names(charNamesString)
print charResponse.result

ids = charResponse.result
charIds = []

# for characterName, characterId in charResponse.result.items():
#     charIds.append(str(characterId))
#     charIdstring = ','.join(charIds)
#     print charIdstring

for characterName, characterId in charResponse.result.items():
    eve = evelink.eve.EVE()
    affResponse = eve.character_info_from_id(characterId)
    print affResponse.result['name']
    print affResponse.result['alliance']['name'], affResponse.result['alliance']['id']
    print affResponse.result['corp']['name'], affResponse.result['corp']['id']


#print ids['Anna niedostepny']

# eve = evelink.eve.EVE()
# affResponse = eve.character_info_from_id(charIdstring)
# print affResponse.result['name']
# print affResponse.result['alliance']['name'], affResponse.result['alliance']['id']
# print affResponse.result['corp']['name'], affResponse.result['corp']['id']

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
shitfuck = []

for characterName, characterId in charResponse.result.items():
    shitfuck.append(characterId)
    charIds.append(str(characterId))
    charIdstring = ','.join(charIds)
    print charIdstring

# for characterName, characterId in charResponse.result.items():
#     eve = evelink.eve.EVE()
#     affResponse = eve.character_info_from_id(characterId)
#     print affResponse.result
#     print affResponse.result['alliance']['name'], affResponse.result['alliance']['id']
#     print affResponse.result['corp']['name'], affResponse.result['corp']['id']

eve = evelink.eve.EVE()
affResponse = eve.affiliations_for_characters(charIdstring)
#print affResponse.result

for item in shitfuck:
    print affResponse.result[item]['name'], affResponse.result[item]['alliance'], affResponse.result[item]['corp']




# print affResponse.result['characters']
# print affResponse.result['alliance']['name'], affResponse.result['alliance']['id']
# print affResponse.result['corp']['name'], affResponse.result['corp']['id']

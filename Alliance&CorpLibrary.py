import evelink.api

api = evelink.api.API()
response = api.get('eve/AllianceList')
for a in response.result.find('rowset').findall('row'):
    print a.get('name')
    print a.get('allianceID')
import requests
import json
import time

def getProfessors(startIndex):
	response = requests.get('http://search.mtvnservices.com/typeahead/suggest/?solrformat=true&rows=2500&callback=noCB&q=*%3A*&defType=edismax&qf=teacherfirstname_t%5E2000+teacherlastname_t%5E2000+teacherfullname_t%5E2000+autosuggest&bf=pow(total_number_of_ratings_i%2C2.1)&sort=total_number_of_ratings_i+desc&siteName=rmp&fl=pk_id+teacherfirstname_t+teacherlastname_t+total_number_of_ratings_i+averageratingscore_rf+schoolid_s&fq=', params={'start': startIndex})
	responseJSON = json.loads(response.text.replace('noCB(', '').replace(');', ''))
	professors = responseJSON['response']['docs']
	return professors
#issues: 155, 399

for i in range(652,691):
	if i % 50 == 0:
		time.sleep(60)
	print(i)
	while True:
		try:
			professors = getProfessors(i*2500)
			break
		except:
			print("Error")
			time.sleep(60)

	f = open(str(i) + '.json', 'w')
	f.write(json.dumps(professors))

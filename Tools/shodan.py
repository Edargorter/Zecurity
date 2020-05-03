import shodan
import time
import os

def shodan_search():

    SHODAN_API_KEY = ""
    SEARCH = "mqtt alarm"
    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        results = api.search(SEARCH)
        file1 = open("results.txt")
        
        for result in results['matches']:
            searching = result['ip_str']
            file1.write(searching + '\n')
            file1.close()

    except shodan.APIError:
        pass

if __name__ == "__main__":
    shodan_search()

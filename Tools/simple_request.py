import requests

username = '1414769'
password = ''

url = 'https://wits-e.wits.ac.za/portal/xlogin' # Set destination URL here
post_fields = {'eid': '1414769', 'pw': 'Th30ldWolf777', 'Submit': 'Log In'}     # Set POST fields here
cookies = {'_ga':'GA1.3.1501807586.1556025125', 'PS_DEVICEFEATURES':'width:1280 height:800', 'pixelratio':'2', 'touch':'0', 'geolocation':'1', 'websockets':'1', 'webworkers':'1', 'datepicker':'1', 'dtpicker':'1', 'timepicker':'1', 'dnd':'1', 'sessionstorage':'1', 'localstorage':'1', 'history':'1', 'canvas':'1', 'svg':'1', 'postmessage':'1', 'hc':'0', 'maf':'0', 'pasystem_timezone_ok':'true'}


response = requests.post(url, params=post_fields, cookies=cookies)
if not response: print("Error.")
print(response.text)

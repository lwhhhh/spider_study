import urllib.request

'''
    example: http://www.pm25.in/api/querys/pm2_5.json?city=珠海&token=xxxxxx
'''

BASE_URL = 'http://www.pm25.in/api/querys/aqi_ranking.json'

def dowload(url):
    response_data = urllib.request.urlopen(url).read()
    response_data = response_data.decode('utf8')
    return response_data
    
def set_url():
    app_key = '5j1znBVAsnSf5xQyNQyq'
    args = '?token=' + app_key
    url = BASE_URL + args
    return url
    
def parser(data_to_parser):
    print(data_to_parser)

if __name__ == '__main__':
    dowload_url = set_url()
    data_to_parser =  dowload(dowload_url) 
    parser(data_to_parser)    

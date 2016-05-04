import os
import urllib.request
import json

'''
    example: http://www.pm25.in/api/querys/pm2_5.json?city=珠海&token=xxxxxx
'''

BASE_URL = 'http://www.pm25.in/api/querys/aqi_ranking.json'
SAVE_PATH = os.getcwd() + '/response_data'

def save_json(response_data):
    '''
        API只能调用一次
        珍惜机会所以把下载到的数据先保存一份到磁盘上
    '''
    with open(SAVE_PATH,w) as fp:
        fp.write(response_data)
    
def dowload(url):
    response_data = urllib.request.urlopen(url).read()
    save_json(response_data)
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

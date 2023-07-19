# import urllib.request as request
import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.ptt.cc/bbs/movie/index.html';

# url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
# with request.urlopen('https://www.ptt.cc/bbs/movie/M.1689770726.A.E4F.html') as response:
    # 需要注意編碼
    # print(response.status)
    # page_data = response.read().decode("utf-8");     
# print(page_data)

def countGoodOpinion(data, content):
    count = 0
    for item in content:
        opinionType = item.getText()
        if opinionType and opinionType.strip() == '推':
            count += 1

    data['goodOpinionCount'] = count;
    
    return data

    data['goodOpinion'] = count
def handleMainInfo(data, header):
    for item in header:
        topic = item.find('span', class_="article-meta-tag")
        skip_item = False;
        if topic.getText() == '標題':
            title = item.find('span', class_="article-meta-value")
            if title:
                data['title']  = title.getText();
        if topic.getText() == '時間':
            time_text = item.find('span', class_="article-meta-value")
            if time_text:
                data['time']  = time_text.getText();
    return data


def handleEveryPost(url):
    response = requests.get('https://www.ptt.cc/' + url)
    data = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        header = soup.select(".article-metaline")
        content = soup.select(".push-tag")
        data = handleMainInfo(data, header)
        data = countGoodOpinion(data, content)
    return data

result = []

def handleEveryPage(pageUrl):
    response_list = requests.get(pageUrl)
    soup_list = BeautifulSoup(response_list.text, "html.parser")
    if response_list.status_code == 200:
        post_list = soup_list.select('.title')

    for item in post_list:
        if not item.select_one('a'):
            continue;
        post_url = item.select_one('a').get('href')
        post_result = handleEveryPost(post_url)
        result.append(post_result)

def getPreviousPageUrl(PageUrl):
    index = requests.get(PageUrl)
    soup_index = BeautifulSoup(index.text, "html.parser")
    paging_list = soup_index.select('.btn.wide')
    previous_page_url = "";
    for paging in paging_list:
        if paging.getText() == '‹ 上頁':
            previous_page_url = paging.get('href');

    return 'https://www.ptt.cc/' + previous_page_url;

def generateCsv(data):
    with open('movie.txt', mode='w', encoding='utf-8') as file:
        for item in data:
            file.write(item['title']);
            file.write(',');
            file.write(str(item['goodOpinionCount']));
            file.write(',');
            file.write(item['time']);
            file.write('\n');


count = 3;

while(count > 0):
    handleEveryPage(url);
    url = getPreviousPageUrl(url);
    count -= 1;
print(result);

generateCsv(result);
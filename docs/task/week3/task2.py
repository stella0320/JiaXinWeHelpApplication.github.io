import urllib.request as request
# import requests
from bs4 import BeautifulSoup
import json


url = 'https://www.ptt.cc/bbs/movie/index.html';
headers = {'User-Agent': 'Mozilla/5.0'} # 信任網站參數

# 計算推文數
def countGoodOpinion(data, content):
    count = 0
    for item in content:
        opinionType = item.getText()
        if opinionType and opinionType.strip() == '推':
            count += 1

    data['goodOpinionCount'] = count;
    
    return data

# 處理每一則貼文的標題與時間'
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

# 處理每一則貼文，打開url，並找到標題&時間，並計算推文數
def handleEveryPost(url):
    page_request = request.Request('https://www.ptt.cc/' + url, headers=headers);
    response = request.urlopen(page_request)
    data = {}
    if response.status == 200:
        soup = BeautifulSoup(response.read().decode('UTF-8'), "html.parser")
        header = soup.select(".article-metaline")
        content = soup.select(".push-tag")
        data = handleMainInfo(data, header)
        data = countGoodOpinion(data, content)
    return data

result = []

# 處理每一頁，解析出每一條post的url，再個別打開解析頁面資訊
def handleEveryPage(pageUrl):
    main_request = request.Request(pageUrl, headers=headers);
    response_list = request.urlopen(main_request)
    
    soup_list = BeautifulSoup(response_list.read().decode('UTF-8'), "html.parser")
    if response_list.status == 200:
        post_list = soup_list.select('.title')

    for item in post_list:
        if not item.select_one('a'):
            continue;
        post_url = item.select_one('a').get('href')
        post_result = handleEveryPost(post_url)
        result.append(post_result)

# 在貼文清單頁面中，找到前一頁的url
def getPreviousPageUrl(PageUrl):
    previous_page_request = request.Request(PageUrl, headers=headers);
    index = request.urlopen(previous_page_request)
    soup_index = BeautifulSoup(index.read().decode('utf-8'), "html.parser")
    paging_list = soup_index.select('.btn.wide')
    previous_page_url = "";
    for paging in paging_list:
        if paging.getText() == '‹ 上頁':
            previous_page_url = paging.get('href');

    return 'https://www.ptt.cc/' + previous_page_url;

# 將組好的資料，寫成txt檔
def generateCsv(data):
    with open('movie.txt', mode='w', encoding='utf-8') as file:
        for item in data:
            file.write(item['title']);
            file.write(',');
            file.write(str(item['goodOpinionCount']));
            file.write(',');
            file.write(item['time']);
            file.write('\n');


count = 3; # 總共解析三頁

while(count > 0):
    # 解析每一頁
    handleEveryPage(url);
    # 解析每一頁完找出前一頁的url
    url = getPreviousPageUrl(url);
    count -= 1;

print(result);

generateCsv(result);
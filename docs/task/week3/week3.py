import urllib.request as request
import json
# import re
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
with request.urlopen(url) as response:
    # 需要注意編碼
    data = json.load(response);

location_info = data['result']['results'];

# distict_zone_list = ['中正區', '萬華區', '中⼭區', '⼤同區', '⼤安區', '松⼭區', '信義區', '⼠林區', '文⼭區', '北投區', '內湖區', '南港區'];
print(len(location_info));
with open('attraction.csv', mode='w', encoding='utf-8') as file:
    for location in location_info:
        file.write(location['stitle']);
        file.write(',');
        distict = location['address'][5:8];
        file.write(distict);
        location['distict'] = distict;
        all_file = location['file'];
        position = all_file.index("https://www.travel.taipei/", 5);
        main_website = all_file[:position];
        location['main_website'] = main_website;
        file.write(',');
        file.write(main_website);
        file.write('\n');

location_by_distict = {}
# by 區域group 各景點: {區域: '', 景點:[]}
for location in location_info:
    distict = location['distict'];
    view_point = location['stitle'];
    if distict in location_by_distict.keys():
        location_by_distict[distict] += [view_point];
    else:
        location_by_distict[distict] = [view_point];

with open('mrt.csv', mode='w', encoding='utf-8') as file:
    for key, values in location_by_distict.items():
        file.write(key);
        file.write(',');
        file.write(','.join(values));
        file.write('\n');


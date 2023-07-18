import urllib.request as request
import json;
import re
url = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json';
with request.urlopen(url) as response:
    # 需要注意編碼
    data = json.load(response);

location_info = data['result']['results'];

distict_zone_list = ['中正區', '萬華區', '中⼭區', '⼤同區', '⼤安區', '松⼭區', '信義區', '⼠林區', '文⼭區', '北投區', '內湖區', '南港區'];
print(len(location_info));
with open('attraction.csv', mode='w', encoding='utf-8') as file:
    for location in location_info:
        file.write(location['stitle']);
        file.write(',');
        distict = location['address'][5:8];
        file.write(location['address'][5:8]);
        location['distict'] = distict;
        all_file = location['file'];
        position = all_file.index("https://www.travel.taipei/", 5);
        main_website = all_file[:position];
        location['main_website'] = main_website;
        file.write(',');
        file.write(main_website);
        # pattern = "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$";
        # all_file_list = re.findall(pattern, all_file, re.IGNORECASE);
        # if len(all_file_list) > 0:
        #     file.write(',');
        #     file.write(all_file_list[0]);
        #     location['main_website'] = all_file_list[0];
        file.write('\n');

location_by_distict = {}
for location in location_info:
    distict = location['distict'];
    view_point = location['stitle'];
    if distict in location_by_distict.keys():
        location_by_distict[distict] += [view_point];
    else:
        location_by_distict[distict] = [view_point];

print(location_by_distict);

with open('mrt.csv', mode='w', encoding='utf-8') as file:
    for key, values in location_by_distict.items():
        file.write(key);
        file.write(',');
        file.write(','.join(values));
        file.write('\n');


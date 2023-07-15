def find_and_print(messages):
    eighteen_age_list = ['vote', '18 years old', 'legal age in Taiwan'];
    result = [];
    for key, value in messages.items():
        for eighteen_age in eighteen_age_list:
            if eighteen_age in value:
                result.append(key);
    print('-----task1-----');
    print(result);
# write down your judgment rules in comments
# your code here, based on your own rules
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
})


def calculate_sum_of_bonus(data):
    total_salary = 0;
    standard_performance_rate ={"above_average": 5,"average": 3, "below_average": 2 }; # 定義各表現程度的加權比例
    standard_role_rate = {"Engineer": 3,"CEO": 5, "Sales": 2};
    for info in data['employees']:
        for key, value in info.items():
            
            if key == 'salary':
                salary = str(value).replace(",", "");
                if 'USD' in salary:
                    salary = salary.replace("USD", "")
                    salary = int(salary) * 30;
                else:
                    salary = int(salary);
                info['salary'] = salary;
                total_salary += salary;
     
    total_new_salary = 0;
    new_salary_list = []
    for info in data['employees']:
        salary = info['salary'];
        bonus_rate = salary/total_salary;
        performance = info['performance'].replace(" ", "_");
        performance_rate = standard_performance_rate[performance];
        role_rate = standard_role_rate[info['role']];
        new_salary = salary * (performance_rate + role_rate);
        info['new_salary'] = new_salary;
        new_salary_list.append(new_salary);
        total_new_salary += new_salary;
    
    salary_for_each_one = [round(i/total_new_salary * 10000) for i in new_salary_list]
    total_bonus = sum(salary_for_each_one);
    print('-----task2-----');
    print('total bouns:', total_bonus);


calculate_sum_of_bonus({
    "employees":[
        {
            "name":"John",
            "salary":"1000USD",
            "performance":"above average",
            "role":"Engineer"
        },
        {
            "name":"Bob",
            "salary":60000,
            "performance":"average",
            "role":"CEO"
        },
        {
            "name":"Jenny",
            "salary":"50,000",
            "performance":"below average",
            "role":"Sales"
        }
    ]
})

def func(*data):
    duplicate_list = [];
    for i in range(0, len(data)):
        for j in range(i+1, len(data)):
            i_name = data[i];
            j_name = data[j];
            if i_name[1:2] == j_name[1:2]:
                duplicate_list.append(i_name);
                duplicate_list.append(j_name);
                
    for name in data:
        if name not in duplicate_list:
            print(name);        
print('-----task3-----');       
func("彭大牆", "王明雅", "吳明") # print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花") # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花") # print 沒有


print('-----task4-----');  
def get_number(index):
    result = 0;
    if index % 2 == 0:
        #  偶數
        result += 0 + 3 * index /2;
    else:
        # 奇數
        result += 4 + (index -1) * 3/2;

    print('index:', index , ', result:' , int(result));
get_number(1) # print 4
get_number(5) # print 10
get_number(10) # print 15
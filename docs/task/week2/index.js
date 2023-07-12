
var find_and_print = function(messages) {
    let result = []; // 如果符合18歲年齡將名單放進這個array
    let eightean_age_list = ['18 years old', 'legal age in Taiwan'] //定義18歲年齡

    for (let data in messages) {
        for (let j=0;j < eightean_age_list.length;j++) {
            if (messages[data].indexOf(eightean_age_list[j]) > -1 ) {
                result.push(data);
            }
        }
    }         
    console.log('-----task1-----');
    console.log('result: ' + result);
};
find_and_print({
    "Bob":"My name is Bob. I'm 18 years old.",
    "Mary":"Hello, glad to meet you.",
    "Copper":"I'm a college student. Nice to meet you.",
    "Leslie":"I am of legal age in Taiwan.",
    "Vivian":"I will vote for Donald Trump next week",
    "Jenny":"Good morning."
});


let calculateSumOfBonus = function(data){
    let employeeInfo = data["employees"];
    let usd_rate = 30; // 定義匯率
    let standard_performance_rate ={"above_average": 5,"average": 3, "below_average": 2 }; // 定義各表現程度的加權比例
    let standard_role_rate = {"Engineer": 3,"CEO": 5, "Sales": 2}; // 定義各角色的加權比例
    let total_salary = 0;
    
    let bonus_rate = [];
    for (let i=0;i< employeeInfo.length;i++) {
        let salary = employeeInfo[i]['salary'].toString().replace(/,/g, ""); // 將逗號拿掉
        if (salary.indexOf('USD') > -1) {   // 如果是USD，先乘匯率
            salary = salary.replace('USD', '');
            salary = salary * usd_rate;
        }
        employeeInfo[i]['salary'] = parseInt(salary);
    }

    // 計算表現和角色的加權比例成薪水，組成加權薪水
    let total_new_salary = 0;
    for (let i=0;i < employeeInfo.length;i++) {
        let salary = employeeInfo[i]['salary'];
        let bonus_rate = salary/total_salary;
        let performance = employeeInfo[i]['performance'].toString().replace(/ /g, "_");
        let performance_rate = standard_performance_rate[performance];
        let role_rate = standard_role_rate[employeeInfo[i]['role']];
        let new_salary = salary * (performance_rate + role_rate); // 新的加權薪水，利用原薪水 * (表現加權 + 角色加權)
        employeeInfo[i]['new_salary'] = new_salary;
        total_new_salary += new_salary;
    }

    // 按照每個人的加權薪水比例去分配bonus 10000原
    for (let i=0;i < employeeInfo.length;i++) {
        let new_salary = employeeInfo[i]['new_salary'];
        employeeInfo[i]['bonus']  = Math.round(new_salary/total_new_salary*10000);
    }
    console.log(employeeInfo);

}

console.log("---task2------");
calculateSumOfBonus({
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
});


var func = function(/**/) { 

    let raw_data = Array.prototype.slice.call(arguments);
    let duplicate_date = [];
    // 先把重複的名字取出來，塞到duplicate_date
    for (let i=0; i < raw_data.length; i++) {
        for (let j=i+1; j < raw_data.length; j++) {
            let i_name = raw_data[i];
            let j_name = raw_data[j];
            if (i_name.substr(1, 1) === j_name.substr(1, 1)) {
                duplicate_date.push(i_name);
                duplicate_date.push(j_name);
            }
        }
    }

    let result = [];
    // 如果不在duplicate_date中的資料，表示是unique的名字
    for (let i=0; i < raw_data.length; i++) {
        if (duplicate_date.indexOf(raw_data[i]) < 0) {
            result.push(raw_data[i]);
        }
    }
    console.log('raw_data:' + raw_data);
    console.log('result:' + result);

};
console.log('-----task3-----');
func("彭大牆", "王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有

let getNumber = function(index) {
    let result = 0;
    if (index % 2 == 0) {
        // 偶數
        result += 0 + 3 * index /2;
    } else {
        // 奇數
        result += 4 + (index -1) * 3/2;
    }
    console.log('index:' + index + ', result:' + result);
}

console.log('-----task4-----');
getNumber(1); // print 4
getNumber(5); // print 10
getNumber(10); // print 15
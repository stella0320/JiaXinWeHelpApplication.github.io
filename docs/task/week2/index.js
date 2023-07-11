
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
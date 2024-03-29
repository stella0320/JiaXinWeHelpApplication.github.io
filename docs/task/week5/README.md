### 要求三：SQL CRUD

*  使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。

```mysql=
INSERT INTO website.member (name, username, password)
VALUES ('test', 'test', 'test');
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-1.png)

```mysql=
INSERT INTO website.member (name, username, password, follower_count)
VALUES ('test1', 'test1', 'test1', 10);


INSERT INTO website.member (name, username, password, follower_count)
VALUES ('test2', 'test2', 'test2', 15);


INSERT INTO website.member (name, username, password, follower_count)
VALUES ('test3', 'test3', 'test3', 20);


INSERT INTO website.member (name, username, password, follower_count)
VALUES ('test4', 'test4', 'test4', 25);
```

![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-1-1.png)



* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。

```mysql=
select * from website.member;
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-2.png)


* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。

```mysql=
select * from website.member order by time desc;
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-3.png)

* 使⽤ SELECT 指令取得 member 資料表中第 2 到第 4 筆共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )

```mysql=
select a.* from website.member a order by time desc
limit 1, 3;
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-4.jpg)


* 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。

```mysql=
select * from website.member 
where username = 'test';
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-5.png)

* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。

```mysql=
select * from website.member
where username='test' and password='test';
```

![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-6.png)


* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test5。

```mysql=
update website.member 
set username = 'test5'
where username = 'test'
```

![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image3-7.png)


### 要求四：SQL Aggregate Functions

利⽤要求⼆建立的資料庫和資料表，寫出能夠滿⾜以下要求的 SQL 指令：
* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
```mysql=
select count(*) from website.member;
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image4-1.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。
```mysql=
select sum(follower_count) from website.member;
```

![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image4-2.png)


* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。

```mysql=
select sum(follower_count)/ count(follower_count) from website.member;
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image4-3.png)


### 要求五：SQL JOIN


* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者的姓名。

```mysql=
select b.username , a.* FROM website.message a
LEFT join website.member b
on a.member_id = b.id;
```
![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image5-1.png)


* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test5 的所有留⾔，資料中須包含留⾔者的姓名。

```mysql=
select b.username , a.* FROM website.message a
LEFT join website.member b
on a.member_id = b.id
where username = 'test5';
```

![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image5-2.png)


* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。

```mysql=
SELECT sum(c.like_count)/count(*) avg_like_count from (select b.username , a.* FROM website.message a
LEFT join website.member b
on a.member_id = b.id
where username = 'test5') c;
```

![](https://github.com/stella0320/JiaXinWeHelpApplication.github.io/blob/main/docs/task/week5/image/image5-3.png)

OS: Windows/Mac, Python3
IDE Tools: PyCharm 2018 (Professional Edition)

Set-up Environment: 
1)	Install psycopg2
Enter below command in cmd (for Windows) or in terminal (for Mac)
 pip install psycopg2
 
2)	Open “Map-based Guide” project

i)	Extract file inside “Hotel4.zip” to a local disk;

ii)	Launch Pycharm software ;

iii)	Click open to open the extracted project at step i);

3)	Set-up database

i)	Create PostgreSQL database in PyCharm 

Expand “Database” tool window on right-side of PyCharm interface, click plus “+” button, then choose add Data Source to add new PostgreSQL database;

Click button  to launch setting window of Database. Set Database parameters as shown below.

ii)	Add database parameters in “HelloWorld/MainPage/settings.py” file

4)	Initialize data
Enter below command in cmd (for Windows) or in terminal (for Mac):
cd /“Change this part to the path where the PyCharm project files are extracted”/HelloWorld
python manage.py makemigrations 
python manage.py migrate
(Notes: known issues and solutions for this step is in Appendix B)

5)	Start Web service
Enter below command in cmd (for Windows) or in terminal (for Mac):
python manage.py runserver 127.0.0.1:8000

6)	Load data to database
Open Web Browser and enter below query to address bar then press “Enter”.
http://127.0.0.1:8000/testdb
http://127.0.0.1:8000/tourismdb

7)	Verify if the application is running
Open Web Browser and enter below url address:
http://127.0.0.1:8000/map?query=



Causes:
The table already exist inside database;
May due to multiple execution of Django migration.

Solution:
Follow below steps:
1)	Drop the tables

Right click “TestModel_test”, “TestModel_tourism” inside PyCharm database tool window;
Click drop database button;
Click “OK” to drop.

2)	Truncate table “django_migration”
Right click “django_migration” table inside PyCharm database tool window and follow the below steps to truncate table.

3)	Refresh the database
Click button  to refresh database.PyCharm Project Code


运行环境：
Windows/Mac
Python3
IDE工具：
PyCharm 专业版


环境配置：
1.	安装运行所需的python依赖库：
比如：psycopg2
可以在终端输入命令：pip install psycopg2

2.	安装数据库
安装postgresql 
设置过程中端口改成 15432
用户名设置为：postgres
密码设置为：123456
（此处的设置，需要与HelloWorld/MainPage/settings.py中的设置一致）

在PyCharm中新建数据库，点击右侧Database，然后点击+号，新建PostgreSQL数据库。（如果已有数据库，请先删除再新建）

新建成功后，设置数据库的用户名(User)、密码(Password)、以及端口(Port)


3.	初始化数据
打开控制台（windows）/终端（Mac）
输入以下命令
cd /Users/windy.macbookpro/Downloads/hotels4/HelloWorld
（红色部分请替换成projec所在路径，该命令的作用是进入hotels中HelloWorld所在位置）
python manage.py makemigrations 
python manage.py migrate
（migrate前，如果存在TestModel_test, TestModel_tourism,请先drop掉这两个表;并清空django_migration，右键)
( 运行时，如果显示django_content_type存在，请右键django_content_type，点击drop，此时系统会生成TestModel_test, TestModel_tourism)
  
此处的命令的作用，是根据TestModel中models.py文件里面定义的model创建,并在数据库中创建相应的table
谈谈机制: migrations机制有两个指令，第一个是makemigrations，第二个是migrate，生成migrations代码的makemigrations指令是用models里面的model和当前的migrations代码里面的model做对比，如果有新的修改，就生成新的migrations代码，migrate指令是用migrations目录中代码文件和django数据库djaong_migrations表中的代码文件做对比，如果表中没有，那就对这些没有的文件按顺序及依赖关系做migrate apply，然后再把代码文件名加进migrations表中。

4.	启动服务器
打开控制台（windows）/终端（Mac）
输入以下命令
python manage.py runserver 127.0.0.1:8000

5.	加载数据到数据库
http://127.0.0.1:8000/testdb

http://127.0.0.1:8000/tourismdb

6.	访问程序
打开任意浏览器，在地址栏输入地址
http://127.0.0.1:8000/map?query=


使用说明：
1.	点击地图上的不同坐标，可以查看不同坐标的信息

2.	点击左右list中的hotel或者tourism，地图上会单独显示酒店的位置

3.	点击左侧或右侧的搜索栏，可对想要查找的酒店或景点进行搜索


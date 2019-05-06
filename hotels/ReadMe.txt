执行安装：pip install psycopg2

1. 安装数据库
安装postgresql 建议装到C盘 ，设置过程中端口改成 15432
jdbc:postgresql://localhost:15432/postgres
postgres/123456

2. 初始化数据
	http://127.0.0.1:8000/testdb
	http://127.0.0.1:8000/tourismdb

3. 运行命令初始化数据
python manage.py makemigrations
python manage.py migrate

4. 启动
 cd /(your root)/hotels4/HelloWorld
 python manage.py runserver 127.0.0.1:8000

5.访问程序
     http://127.0.0.1:8000/map?query=
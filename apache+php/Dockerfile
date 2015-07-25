
#名称：apache+php
#用户：web前段服务
#创建时间： 2015-7-25


FROM centos
MAINTAINER zhangxin insanetomato@me.com

WORKDIR /root/

#忽略错误的写法，有点莫名其妙 暂时记下来看看
RUN yum -y install httpd php||true
RUN yum -y install mysql php-mysqlnd

#启动httpd报错 增加下配置
RUN sed -ri 's/#ServerName www.example.com:80/ServerName 127.0.0.1:80/g' /etc/httpd/conf/httpd.conf
#保存日志目录
RUN mkdir -p /var/log/httpd/
#保存apache数据文件
RUN mkdir -p /var/www/
#存放web页面
RUN mkdir -p /var/html/

#配置需要连接的mysql  
ENV MYSQL_ADDR 10.0.0.106:3306
ENV MYSQL_USER test
ENV MYSQL_PASS mypassword

ENV TERM linux
ENV LC_ALL en_US.UTF-8

ADD test.php /var/www/html/test.php
EXPOSE 80

ADD run.sh /root/run.sh
RUN chmod u+x run.sh
CMD /root/run.sh 


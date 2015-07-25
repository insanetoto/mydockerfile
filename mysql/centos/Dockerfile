#容器化的mysql
#用户： 后端数据持久化服务
#创建时间  2015-07-25

#维护者信息
FROM centos
MAINTAINER zhangxin insanetomato@me.com

#工作目录
WORKDIR /root/

#安装mysql
RUN yum -y install wget
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
RUN rpm -ivh /root/mysql-community-release-el7-5.noarch.rpm
RUM yum -y install mysql-server
RUN mysql_install_db --user=mysql

#设置用户，根据自己情况增加
ENV MYSQL_USER test
EVN MYSQL_PASS mypassword

ENV LC_ALL en_US.UTF-8

ADD build_table.sh /root/build_table.sh
RUN chmod u+x build_table.sh
RUN /root/build_table.sh

EXPOSE 3306


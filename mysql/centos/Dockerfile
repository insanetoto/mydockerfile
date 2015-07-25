#容器化的mysql
#用户： 后端数据持久化服务
#创建时间  2015-07-25

#维护者信息
FROM centos
MAINTAINER zhangxin insanetomato@me.com

#工作目录
WORKDIR /root/

#导入签名信息 安装mysql的时候用到，网速超慢，疯了
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7

#安装mysql
RUN yum -y install wget
RUN wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
RUN rpm -ivh /root/mysql-community-release-el7-5.noarch.rpm
RUN yum -y install mysql-server
RUN mysql_install_db --user=mysql

#设置用户，根据自己情况增加
ENV MYSQL_USER test
ENV MYSQL_PASS mypassword

#支持中文
ENV LC_ALL en_US.UTF-8

ADD build_table.sh /root/build_table.sh
RUN chmod u+x build_table.sh
RUN /root/build_table.sh

#暴漏端口
EXPOSE 3306

ADD run.sh /root/run.sh
RUN chmod u+x run.sh
RUN /root/run.sh



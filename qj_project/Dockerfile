#曲靖项目数据同步环境Docker化  纯练手性质
#搭建 Python2.7+cx_Oracle+Oracle11g环境
#提供ssh服务

#Dockerfile 信息
FROM ubuntu:14.04
MAINTAINER zhangxin <insanetomato@me.com>
ENV DEBIAN_FRONTEND noninteractive

#用国内源 国外实在太慢了
RUN cp /etc/apt/sources.list /etc/apt/sources.list_backup
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ utopic main restricted universe multiverse" >/etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ utopic-security main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ utopic-updates main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ utopic-proposed main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.aliyun.com/ubuntu/ utopic-backports main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ utopic main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ utopic-security main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ utopic-updates main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ utopic-proposed main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.aliyun.com/ubuntu/ utopic-backports main restricted universe multiverse" >>/etc/apt/sources.list
RUN apt-get update 
RUN apt-get upgrade -y

#安装ssh
RUN locale-gen --no-purge en_US.UTF-8
RUN apt-get install -y openssh-server

#安装ssh
RUN locale-gen --no-purge en_US.UTF-8
RUN apt-get install -y openssh-server

#设置root用户登陆
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh
RUN mkdir -p /var/run/sshd
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
#监听端口
EXPOSE 22
#设置root用户密码
RUN echo 'root:gogogo' | chpasswd

#设置环境变量
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8


#cx_Oracle环境
RUN apt-get install python -y
RUN apt-get install libaio1 -y

#配置oracle客户端环境变量
RUN mkdir -p /opt/oracle/lib
ENV LD_LIBRARY_PATH /opt/oracle/lib
# 将cx_Oracle放到python系统路径
ADD cx_Oracle.so /usr/lib/python2.7/dist-packages/cx_Oracle.so

#将oracle客户端文件放到lib中
ADD libclntsh.so.11.1 /opt/oracle/lib/libclntsh.so.11.1
ADD libnnz11.so /opt/oracle/lib/libnnz11.so
ADD libocci.so.11.1 /opt/oracle/lib/libocci.so.11.1
ADD libociei.so /opt/oracle/lib/libociei.so
ADD libocijdbc11.so /opt/oracle/lib/libocijdbc11.so

#容器启动
ENTRYPOINT /usr/sbin/sshd -D

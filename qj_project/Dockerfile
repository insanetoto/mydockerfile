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

RUN apt-get install python -y
RUN apt-get install libaio1 -y

#配置oracle客户端环境变量
RUN mkdir -p /opt/oracle/lib
ENV LD_LIBRARY_PATH /opt/oracle/lib

#将oracle客户端文件放到lib中
ADD libclntsh.so.11.1 /opt/oracle/lib/libclntsh.so.11.1
ADD libnnz11.so /opt/oracle/lib/libnnz11.so
ADD libocci.so.11.1 /opt/oracle/lib/libocci.so.11.1
ADD libociei.so /opt/oracle/lib/libociei.so
ADD libocijdbc11.so /opt/oracle/lib/libocijdbc11.so

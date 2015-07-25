FROM ubuntu:14.04
MAINTAINER zhangxin <insanetomato@me.com>
ENV DEBIAN_FRONTEND noninteractive
#用国内源 国外实在太慢了
RUN cp /etc/apt/sources.list /etc/apt/sources.list_backup
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse" >/etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse" >>/etc/apt/sources.list
RUN echo "deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse" >>/etc/apt/sources.list
RUN apt-get update 
RUN apt-get upgrade -y
#使用add-apt-repository 这个命令需要安装的包
RUN apt-get install -y  python-software-properties
RUN apt-get install -y  software-properties-common

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

#容器启动
ENTRYPOINT /usr/sbin/sshd -D

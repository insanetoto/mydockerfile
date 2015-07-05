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

#安装ssh
RUN locale-gen --no-purge en_US.UTF-8
RUN apt-get install -y openssh-server
#设置root用户登陆
RUN sed -ri 's/session    required     pam_loginuid.so/#session    required     pam_loginuid.so/g' /etc/pam.d/sshd
RUN mkdir -p /root/.ssh && chown root.root /root && chmod 700 /root/.ssh
RUN mkdir -p /var/run/sshd
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config
#设置root用户密码
RUN echo 'root:gogogo' | chpasswd
#设置环境变量
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

#安装 mysql
RUN apt-get install -y mysql-server && \
  rm -rf /var/lib/apt/lists/* && \
  sed -i 's/^\(bind-address\s.*\)/# \1/' /etc/mysql/my.cnf && \
  sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/my.cnf && \
  echo "mysqld_safe &" > /tmp/config && \
  echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" identified by \"gogogo\";'" >> /tmp/config && \
  echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"localhost\" identified by \"gogogo\";'" >> /tmp/config && \
  bash /tmp/config && \
  rm -f /tmp/config
#设置数据卷
VOLUME ["/etc/mysql", "/var/lib/mysql"]
#设置工作目录
WORKDIR /data
#容器启动
ENTRYPOINT mysqld_safe && /usr/sbin/sshd -D
#监听端口
EXPOSE 22
EXPOSE 3306

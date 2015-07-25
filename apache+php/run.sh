#!/bin/sh
#启动apache
httpd
#httpd命令会立即返回，用个命令防止脚本结束，避免容器直接退出
#防止脚本结束
while true;do sleep 1000;done

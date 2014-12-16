#/bin/sh

num=13310

while [ 0 ]; do
    num=$(curl http://fun.coolshell.cn/n/$num)
    echo $num
    read
done

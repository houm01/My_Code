#!/usr/bin/env bash

# sh_file=test.sh

# [ -x "$sh_file" ] && ./$sh_file || { echo "can't execute, exit...";exit 1; }
# test -x "$sh_file" && ./$sh_file || { echo "can't execute, exit...";exit 1; }

# cat /etc/passwd | while read line;do
# 	let num+=1
# 	echo $num: $line
# done

# while read line;do
# 	let num1+=1
# 	echo $num1: $line
# done < /etc/passwd
# echo $num1

# while read line;do
# 	let num2+=1
# 	echo $num2: $line
# done < <(grep 'UUID' /etc/passwd



select fname in cat dog sheep mouse;do
  echo your choice: \"$REPLY\) $fname\"
  break
done
1) cat
2) dog
3) sheep
4) mouse
#? 3                      # 在此选择序号3
your choice: "3) sheep"   # 将输出序号3对应的内容

#!/usr/bin/env bash

touch "P1. 01.了解jQuery(1).mp4"
touch "P2. 02.jQuery的基本使用(2).mp4"
touch "P3. 03.jQuery的2把利器(3).mp4"
touch "P4. 04.jQuery函数的使用(4).mp4"
touch "P5. 05.jQuery对象的使用(5).mp4"
touch "P6. 06.基本选择器(26).mp4" 
touch "P7. 07.层次选择器(7).mp4"   
touch "P8. 08.过滤选择器(128).mp4" 


for i in *.mp4 ;do
	mv "$i" "`echo $i | sed -r 's/.* ([0-9]{1,3}\..*)\([0-9]{1,3}\)\.mp4/\1.mp4/'`"
done

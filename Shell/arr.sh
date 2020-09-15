#!/usr/bin/env bash

declare -A aarr

for i in `cat a.txt`;do
    let ++aarr[$i]
done

for i in ${!aarr[@]};do
    echo -----
    echo data: $i
    echo count: ${aarr[$i]}
done



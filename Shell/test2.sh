#!/bin/bash

while [ ${#@} -gt 0 ];do
    case "$1" in
        -c|--count)
            count=$2
            shift 2
            ;;
        -t|--timeout)
            timeout=$2
            shift 2
            ;;
        -a|--ip)
            ip=$2
            shift 2
            ;;
        *)
            echo "wrong options or arguments"
            exit 1
    esac
done

ping -c $count -W $timeout $ip

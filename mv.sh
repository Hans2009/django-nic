#!/bin/bash


if [ $1 = "0" ]; then
    echo "Moving pkgs to: ~/pkgs"
    mv mysite/mysite/opa/pkgs/ ~/pkgs/
    pwd && ls -l ~/pkgs/
elif [ $1 = '1' ]; then
    echo "Moving back to dj"
    mv ~/pkgs/ mysite/mysite/opa/pkgs/
    pwd && ls -l mysite/mysite/opa/pkgs/
else 
    echo "--------Please input '0' or '1'-----------"
    echo "----0:moving off"
    echo "----1:moving back"
fi


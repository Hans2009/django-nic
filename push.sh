#!/bin/bash
./mv.sh 0
sudo git add ./
sudo git status
sudo git commit -m "update"
sudo git push origin master
./mv.sh 1

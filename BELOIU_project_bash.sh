#!/bin/bash

echo "It works" 

cd ~/Downloads

cp *.gz ~/
cp *.csv ~/ 

cd ~

gunzip *.gz 

mkdir RAW_DATA 

mv *.fna RAW_DATA 
mv *.csv RAW_DATA

mkdir P_DATA
mkdir RESULTS 

export PATH=$PATH:"~/RAW_DATA" 
export PATH=$PATH:"~/P_DATA"
export PATH=$PATH:"~/RESULTS" 

echo $PATH > readme.txt 
echo " " >> readme.txt
echo "RAW_DATA" >> readme.txt 
echo " " >> readme.txt   
ls RAW_DATA >> readme.txt

cat readme.txt

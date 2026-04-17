#!/bin/bash 

#make sure to run this in the RAW_DATA file or else it won't work 

read -p "Enter fasta filename: " fn 

if [[ ! -f ./$fn ]];
 then
   echo "The file does not exist. Exiting..."
   exit 1
fi

echo $fn

awk 'BEGIN {n_seq=0;} /^>/ {if(n_seq%50000==0){file=sprintf("myseq%d.fa",n_seq);} print >> file; n_seq++; next;} { print > file; }' < bigdata.fna  

grep -c ">" *.fa > log.txt  

cat log.txt 

for f in my*fa
do
    echo Processing $f
    awk 'BEGIN{RS=">"}{gsub("\n","",$0); print ">"$0}' $f > $f.txt 
done

for fn in my*fa.txt
do 
    echo -n "$fn:" >> log.txt
    grep -c 'CACCCTCTCAGGTCGGCTACGCATCGTCGCC' "$fn" >> log.txt 
done 

mv *.fa.txt ~/P_DATA  

cd ~ 

tar -cvf pdata.tar P_DATA
















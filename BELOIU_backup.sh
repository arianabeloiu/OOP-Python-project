#!/bin/bash 

cd ~ 

if [ -d "$HOME/BACKUP_FILES" ] 
then
    echo "Directory $HOME/BACKUP_FILES exists." 
else 
    mkdir -p $HOME/BACKUP_FILES 
    echo "Created BACKUP_FILES in $HOME directory" 
fi   

for ITEM in RAW_DATA/*
  do 
    cp $ITEM BACKUP_FILES 
done 

for ITEM in P_DATA/*
  do   
    cp $ITEM BACKUP_FILES
done   

echo "Files have been copied to backup" 

print_info () {
ls -al $HOME/BACKUP_FILES 
du -sh $HOME/BACKUP_FILES 
} 

print_info $HOME/BACKUP_FILES 

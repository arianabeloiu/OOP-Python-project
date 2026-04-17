
list.files('~') #list the files in ur home directory 

d1=read.table('RTestData.txt', header=TRUE) #read the table 
d1 

d1$fuso #prints out the fuso column 

attach(d1) #attach the d1 to R

fuso #print the fuso column 

strep <- d1$strep 
strep  

qqnorm(strep) 

log_strep <- log(strep) 
log_strep

qqnorm(log_strep) 

lstrep=log_strep
qqnorm(lstrep)
hist(lstrep)

t.test(d1$fuso,strep)
t.test(d1$fuso,lstrep) 

d2=read.csv('primer.csv') 
attach(d2)

newdata=d1[order(time),] 
newdata 

time1 = subset(d1, time=='1')
time1

write.csv(time1,"time1.csv")

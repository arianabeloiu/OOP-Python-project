
data("airquality")

head(airquality) 

qqnorm(airquality$Ozone)
qqnorm(airquality$Solar.R)
qqnorm(airquality$Wind)
qqnorm(airquality$Temp)

Ozone <- airquality$Ozone
Solar <- airquality$Solar.R
Wind <- airquality$Wind
Temp <- airquality$Temp

hist(Ozone)
hist(Solar)
hist(Wind)
hist(Temp)

var.test(Ozone,Solar)
var.test(Ozone,Temp)  

install.packages("bestNormalize") 
library(bestNormalize)

bestNormalize(Ozone)
asinh(Ozone)
qqnorm(asinh(Ozone))
hist(asinh(Ozone))
hist(logb_ozone)
 
bestNormalize(Solar)
bestNormalize(Wind)
bestNormalize(Temp)

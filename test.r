library(MASS)
library(ggplot2)
data(phones)
data(ToothGrowth)

ToothGrowth

phones

cor.test(ToothGrowth$len, ToothGrowth$dose)
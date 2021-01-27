install.packages('arules')
install.packages('arulesViz')
library(arules)
library(arulesViz)
library(data.table)

milk <- fread("milk.csv") #wide data format
milk
sapply(milk, class)

milk$ID = factor(milk$ID)
milk$milk = factor(milk$milk)
milk$bread = factor(milk$bread)
milk$butter = factor(milk$butter)
milk$beer = factor(milk$beer)
milk$diapers = factor(milk$diapers)

sapply(milk, class)



##library(tidyr)
milk_long <- gather(milk, key = item, ,milk:diapers, factor_key = TRUE)
milk_long <- milk_long[milk_long$value == 1,]
milk_long <- subset(milk_long, select = c(1,2))

milk_long



milk <- subset(milk, select = 2:6)
milk
milk_long <- subset(milk_long, select = 2)
milk_long

milk_rules <- apriori(milk[c(2,3,4,5),], parameter = list(support = 0.04, confidence = 0.3, minlen = 1))
milk_rules #278 rules

milk_rules_long <- apriori(milk_long, parameter = list(support = 0.04, confidence = 0.3, minlen = 1))
milk_rules_long #1 rules

inspect(head(sort(milk_rules, by = 'confidence'), 3)) #top 3 rules shown by confidence

inspect(head(sort(milk_rules_long, by = 'confidence'),3)) #top 3 rules shown by confidence

sapply(milk_long, class)

?apriori



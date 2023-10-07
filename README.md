# 2024-Predictions

This was my attempt only using past data to try an predict next seasons stats. It's definitely not the most sophisticated way to go about doing it.
In the future I would like to try using the more advanced/predictor stats like xERA, FIP, etc but with the data I had this was my best idea. 

Methodology: 
The idea was to use random forest regressor to look at their other stats and make a prediction based on those stats. However, the problem was that they didn't have any other stats for 2024 obviously. So what I did 
was I took the data from the last four full seasons (2019, 2021, 2022, 2023) and did a weighted average based on innings pitched. The reason for this was lets say for example through 180 innings last year the
pitcher had an ERA of 2.50. However, two years ago they only pitched 100 innings then the year of 180 would be weighed more heavily. I did this mainly to avoid really low inning seasons from screwing up the 
averages. Although I also put in a term that tried to avoid this by needing a minimum of 13 games to count toward the season. Obviously this effects starters more than reliver in terms of needing a minimum. 
However, reliever innings are usually lower anyway so a lower inning season shouldn't effect there averages as much. A 30 inning season is closer to what relievers throw as opposed to a 30 inning season for a 
starter. Then I would make the predictions by using the averaged data to make the prediction on the specific stat I wanted. The data was trained on the full 4 year data set. 

Right now it only predicts pitcher stats. 



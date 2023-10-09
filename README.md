# 2024-Predictions

This was my attempt using only past data to try and predict next seasons stats. It's definitely not the most sophisticated way to go about doing it.
In the future I would like to try using the more advanced/predictor stats like xERA, FIP, etc but with the data I had this was my best idea. 

Methodology: 
The idea was to use random forest regressor to look at the players other stats and make a prediction based on those stats. However, the problem was that they didn't have any other stats for 2024, obviously. So what
I did was I took the data from the last four full seasons (2019, 2021, 2022, 2023) and did a weighted average based on innings pitched. The reason for this was to make the data coming from seasons with a lot of 
innings pitched more valuable. For example, through 180 innings last year a random pitcher had an ERA of 2.50. However, two years ago through 100 innings that same pitcher had a 5.00 ERA. Then the 2.50 ERA would be 
weighed more heavily. I did this mainly to avoid really low inning seasons from screwing up the averages. Although I also put in a term that tried to avoid this by needing a minimum of 13 games to count toward the 
season. Obviously this effects starters more than relivers in terms of needing a minimum. However, reliever innings are usually lower anyway so a lower inning season shouldn't effect there averages as much. A 30 
inning season is closer to what relievers throw as opposed to a 30 inning season for a starter. Then I would make the predictions by using the averaged data to make the prediction on the specific stat I wanted. The 
data was trained on the full 4 year data set. 

Right now it only predicts pitcher stats. 

Clayton Kershaw 2024 predicted stats (easy to see in code part of the read me)

  G	    GS	    W	    L	    SV	 IP	   H	  R	    ER	BB	SO	 HR	 HBP	ERA	    AB	 2B	 3B	 GDP	Str	 StL	 StS	 GB/FB	LD	PU	  WHIP	  BAbip	 SO9	SO/W
  27	  24	    10	  5	    0	 140.0	117	 50	    46	30	151	 14	  6	  2.76	 529	 21	  2	 10	 0.67	 0.17	 0.13	 0.45  0.23	0.07	1.0118	0.278	 9.7	4.56


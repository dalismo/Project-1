![image](https://user-images.githubusercontent.com/78628287/119001839-576eb380-b95a-11eb-865f-a6ea019034af.png)
# Analysis of Pollutants in California 


Project 1 for Rutgers Data Science Bootcamp | Due: Sunday May 23, 2021
### [Link to Presentation](https://docs.google.com/presentation/d/1iASbDnn62o1SOcaoT7vGkzs5uftBpUboqCBNdySm6Ts/edit#slide=id.p)

**Group Penny Members**
* Alberto Gonzalez
* Mubashira Qari
* Abayomi Olujobi
* Elise Eng
* Bertrand Louis

# Data and Supplemental Sources

### [www.Kaggle.com](https://www.kaggle.com/sogun3/uspollution) 
US Pollution Information 2000-2016 download


### [wonder.cdc.gov](https://wonder.cdc.gov/controller/datarequest/D76) 
Underlying Cause of Death, 2000-2010 Request for California

### [web.archive.org](https://web.archive.org/web/20181119041829/http://www.fire.ca.gov/fire_protection/downloads/siege/2007/Overview_CompleteFinal.pdf)
California Fire Siege 2007 

### [leginfo.legislature.ca.gov](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=200520060SB1368)
Senate Bill No. 1368 Electricity: emissions of greenhouse gases.

# Questions & Approach 
***based on California's mortality and pollution data from 2006 to 2010...***

**1.** Are deaths caused by chronic lower respiratory diseases (CLRD) linked to changes in AQI and air pollutant levels? 

**2.** Which of these air pollutants (CO, O3, NO2, SO2) have a greater influence, if at all, on the mortality rate due to CLRD? 

**3.** If we find trends that deaths and pollution are correlated, can we further prove that there is a delayed effect from exposure to toxic air pollutants on the mortality rate caused by CLRD?

## Null and Alternative Hypothesis

**Null Hypothesis** - There is no relation between pollutants that cause chronic lower respiratory diseases which eventually lead to death.

**Alternative Hypothesis** - There is a relation between pollutants that cause chronic lower respiratory diseases which eventually lead to death.

## Our Motivation 

Our group took the US pollution data from 2000 to 2016 and was interested in analyzing the Air Quality Index (AQI) trends, specifically in the carbon monoxide (CO), ozone (O3), nitrogen dioxide (NO2) and sulfur dioxide (SO2) levels and how pollution may affect mortality in the US. Initially, we focused on the entirety of the country, but found the dataset to be too large. So then, we decided to focus on the pollution solely in California and saved it as California_Pollution.csv. We chose California because it’s the most densely populated state and also has the largest economy/GDP in the country. With its vast industry and activities from over 39 million people, Cali would hypothetically have hazardous climate change and poor air quality, ultimately jeopardizing the health and wellbeing of its residents. 

To observe the harmful effects of air pollutants in California, we downloaded the 2000 - 2010 California mortality information from the CDC website and concentrated on deaths caused only by chronic lower respiratory diseases (CLRD). As we prepared the data for analysis, we needed to choose data from a smaller range of years. Additionally, each dataset had a different amount of counties, so we also reduced the amount of counties we wanted to analyze. This would allow us to merge the data for further research. Once we were finally done cleaning the data, we merged the two that had data from specifically 16 California counties and within 2006 and 2011. 

In summary, our mission was to find if there is a correlation between the increased AQI (particularly in four air pollutants) and deaths caused by CLRD in the state of California between the years 2006 and 2011. A brief background, according to the CDC, chronic lower respiratory diseases are the fourth leading cause of death in the United States. A few examples of CLRD include asthma, chronic bronchitis, emphysema, pulmonary hypertension, and occupational lung diseases. Even though these types of respiratory diseases are normally found among smokers, we can safely assume that long term inhalation of toxic air pollutants could also play an important role in the development of chronic lower respiratory diseases in Americans. These are some alarming and very relevant issues we face around the world as climate change and natural disasters continue to endanger life on earth. These are a few reasons why we are interested in this topic for our project.
  
## Preparing the Data

### Cleaning Mortality Data
1. From wonder.cdc.gov, we made an API call request and saved it as *California_Mortality.csv*, which included deaths in California from 2006 to 2016 
    - mortality_2006_2010 = mortality_df[mortality_df["Year"] < 2011]
2. Filtered for mortality data from years less than 2011
3. Removed 'County, CA’ with blank using the str.replace() function 
4. Dropped the ‘Notes’ and ‘Year Code’ columns using the .drop()
5. Replaced .0 in the Year column with a blank using str.replace()
6. Find out how many counties are listed using .unique().tolist() → there is 54 total
7. Matched the number of mortality counties with that in the pollution data using .isin(x)
8. Saved finalized cleaned dataset as *mortality_data_clean_df*
### Cleaning Pollution Data
9. From kaggle.com, we downloaded the US Pollution Information (2000-2010) dataset
10. Filtered for pollution data for years greater than 2005 
    - pollution_2006_2010 = pollution_df[pollution_df["Year"] > 2005]
11. Removed '#' from 'ICD-10 113 Cause List' and replaced it with blank using str.replace()
12. Find out how many counties are listed using .unique().tolist() → there is 18 total
13. Saved final cleaned dataset as *pollution_data_df*
### Merging Datasets!!!
14. Combined our mortality_data_clean_df with pollution_data_df using .combine_first()
    - This function worked best b/c it allowed the union of two series even though they each have a lot of null values. This method prioritizes the first call series, in this case, the pollution data frame. So if there is null value, it will take the value at the same position and index from the second series, or our mortality data frame.
15. Replaced all 'NaNs' values with 0 using .fillna(0)


## Findings from our Data Visualizations

### Question 1
**Are deaths caused by chronic lower respiratory diseases (CLRD) linked to changes in AQI and air pollutant levels?** 

Between 2006 and 2010 and in all 18 California counties…
  * CO AQI vs. total mortality due to CLRD: The R-Value is 0.7543850834952978 
   - [x] This indicates a strong correlation between higher CO AQI and death from Chronic Lower Respiratory Disease.
  * NO2 AQI vs. total mortality due to CLRD: The R-Value is 0.8827775793559318 
   - [x] This indicates a very strong correlation between higher NO2 AQI and death from Chronic Respiratory Disease.
  * SO2 AQI vs. total mortality due to CLRD: The R-Value is 0.6170401313230505 
   - [x] This indicates a fairly strong correlation between higher SO2 AQI and death from Chronic Respiratory Disease.
  * O3 AQI vs. total mortality due to CLRD: The R-Value is 0.5435496110691815 
   - [x] This indicates a moderate correlation between higher O3 AQI and death from Chronic Respiratory Disease.

### QUESTION 2
Which of these air pollutants (CO, O3, NO2, SO2) have a greater influence, if at all, on the mortality rate due to CLRD? 

Analysis of Mean AQI levels in California counties
Average CO AQI (2006-2010) vs. Counties: we found that Imperial county has the highest levels of CO (16 ppm). 
We think it's possibly due to the wildfires that are a prominent challenge in SoCal, especially during the hot and dry season.
For reference, the U.S. National Ambient Air Quality Standards for CO for 8 hours is 9 ppm(parts per million).


Average NO2 AQI (2006-2010) vs. Counties: LA and San Bernardino have the highest levels of NO2, but they are still below the EPA standard. 
High levels of NO2 could be linked to the notorious LA traffic, numerous fossil fuel plants and industries, and consistent drought conditions. Additionally, geographically the LA county is a large basin with the Pacific Ocean and surrounded by several mountain ranges with 11,000-foot peaks in the east and south. The health problems that possibly follow could be asthma and respiratory infections.
EPA annual average NO2 standard is 53 ppb.


Average SO2 AQI (2006-2010) vs. Counties: San Diego and Contra Costa have the highest levels. 
One factor could be that SD is part of the San Diego Air Basin (SDAB), a subtropical climate zone characterized by hot/dry summers and mild/wet winters. Additionally, a combination of light winds, stagnant air, little precipitation, and 170+ days of over 70 degrees weather create the ideal conditions for pollution accumulation in the atmosphere. 
In 2010, the Primary National Ambient Air Quality Standard (NAAQS) for Sulfur Dioxide was implemented, establishing the standard to be 75 parts per billion.


Average O3 AQI (2006-2010) vs. Counties: Fresno, Riverside, and San Bernardino have the maximum levels respectively 
Ground-level ozone is created when sunlight strikes pollutants called nitrogen oxides found in the air.
Riverside and San Bernardino counties are located in SoCal where there is constant sunshine and heat is the norm, ozone levels tend to be more elevated. 



Observed Trend : There is an overall decline of  Average Pollutants’ AQI  Levels for California State from 2006 to 2010.

This observed downward trend could be attributed to the California Senate Bill No. 1368, which placed new emission standards for electrical utilities that contribute to combustion of greenhouse gases. EPA’s national and regional rules to reduce emissions of pollutants are strictly implemented.
https://en.wikipedia.org/wiki/Global_Warming_Solutions_Act_of_2006 

# Mortality in California from 2006-2010

Chronic lower respiratory diseases have the highest percentage rate at 31.11 %. This category includes 
But other chronic lower respiratory diseases aren't far behind, with 27.17% of the total. Other CLRD include 
Thus, about 58% of all of the respiratory diseases come from CLRD.
Asthma (0.52%), pneumonitis due to solid & liquid (1.36%), and emphysema (2.14%) are the lowest causes of deaths
Influenza & pneumonia (16.50%)


### Question 3
 If we find trends that deaths and pollution are correlated, can we further prove that there is a delayed effect from exposure to toxic air pollutants on the mortality rate caused by CLRD?

We examined 4 of the most populous counties in California (from 2006 to 2010) to see if the increase in the Air Quality Index (AQI) of these pollutants led to an increase in the total number of deaths from CLRD. 


## Conclusion
  
  Based on our analysis of the data we have proved the alternative hypothesis based on our data supporting that there is a relation between pollutants that cause chronic lower respiratory diseases which eventually lead to death.

## Limitations

Between the Pollution and Mortality files, the overlapping data spanned only from 2006 to 2010 (US Pollution Data was from 2000 - 2016 and the Mortality data for California was from 2006 - 2016)
We only used 16 out of 58 counties in California because the Pollution file had information for just 18 counties and most counties had missing information.
## Challenges
Used 2 datasets and had issues finding the relationship between mortality and pollution levels
We had frequent Github push and pull challenges since this was our first group project sharing a repository.
After our cleaning and visualizations, we had some difficulties putting the story together. Initially, we didn’t realize the number of counties and the years that both datasets shared data was a limitation. With a smaller dataset from the start, picturing a storyline was restricted as well. 

-------- 
  Based on our analysis of of the data we found no correlation between increased amounts of pollution that affect the AQI that leads to more deaths caused by chronic lower respiratory diseases. On the otherhand, there were decreases across all pollutants that could be attributed to the California Senate Bill No. 1368 signed in 2006 that instituted emissions standards that affect the output of greenhouse gases. The purpose of the bill was to lower the emmissions of these gases into the atmosphere and promote cleaner energy.  
  
  There are also anomalies in the data though that were interesting. As an example Imperial county in southern California which is susceptible to wildfires had increased levels of CO which can come from these occurences.

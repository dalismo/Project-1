   <img src="https://user-images.githubusercontent.com/78628287/119001839-576eb380-b95a-11eb-865f-a6ea019034af.png" width=80% height=80%>

# Analysis of Pollutants in California 


***Project 1 for Rutgers Data Science Bootcamp | Due: Sunday May 23, 2021***
### [Link to Presentation](https://docs.google.com/presentation/d/1iASbDnn62o1SOcaoT7vGkzs5uftBpUboqCBNdySm6Ts/edit#slide=id.p)

<details>
  <summary>Group Penny Members :moneybag:</summary>
    <p>:shipit: Alberto Gonzalez</p>
    <p>:octocat: Mubashira Qari</p>
    <p>:shipit: Abayomi Olujobi</p>
    <p>:octocat: Elise Eng</p>
    <p>:shipit: Bertrand Louis</p>
</details>

## Our Motivation 

Our group took the US pollution data from 2000 to 2016 and was interested in analyzing the Air Quality Index (AQI) trends, specifically in the carbon monoxide (CO), ozone (O<sub>3</sub>), nitrogen dioxide (NO<sub>2</sub>) and sulfur dioxide (SO<sub>2</sub>) levels and how pollution may affect mortality in the US. Initially, we focused on the entirety of the country, but found the dataset to be too large. So then, we decided to focus on the pollution solely in California and saved it as California_Pollution.csv. We chose California because it’s the most densely populated state and also has the largest economy/GDP in the country. With its vast industry and activities from over 39 million people, Cali would hypothetically have hazardous climate change and poor air quality, ultimately jeopardizing the health and wellbeing of its residents. 

To observe the harmful effects of air pollutants in California, we downloaded the 2000 - 2010 California mortality information from the CDC website and concentrated on deaths caused only by chronic lower respiratory diseases (CLRD). As we prepared the data for analysis, we needed to choose data from a smaller range of years. Additionally, each dataset had a different amount of counties, so we also reduced the amount of counties we wanted to analyze. This would allow us to merge the data for further research. Once we were finally done cleaning the data, we merged the two that had data from specifically 16 California counties and within 2006 and 2011. 

In summary, our mission, as data science and health enthusiasts, was to find if there is a correlation between the increased AQI (particularly in four air pollutants) and deaths caused by CLRD in the state of California between the years 2006 and 2011. A brief background, according to the CDC, chronic lower respiratory diseases are the fourth leading cause of death in the United States. A few examples of CLRD include asthma, chronic bronchitis, emphysema, pulmonary hypertension, and occupational lung diseases. Even though these types of respiratory diseases are normally found among smokers, we can safely assume that long term inhalation of toxic air pollutants could also play an important role in the development of chronic lower respiratory diseases in Americans. These are some alarming and very relevant issues we face around the world as climate change and natural disasters continue to endanger life on earth. These are a few reasons why we are interested in this topic for our project.
  
# Questions & Approach 
***based on California's mortality and pollution data from 2006 to 2010...***

**Q1.** Are deaths caused by chronic lower respiratory diseases (CLRD) linked to changes in AQI and air pollutant levels? 

**Q2.** Which of these air pollutants (CO, O<sub>3</sub>, NO<sub>2</sub>, SO<sub>2</sub>) have a greater influence, if at all, on the mortality rate due to CLRD? 

**Q3.** If we find trends that deaths and pollution are correlated, can we further prove that there is a delayed effect from exposure to toxic air pollutants on the mortality rate caused by CLRD?

## Our Hypotheses

   - [ ] **Null Hypothesis** - There is no relation between pollutants that cause chronic lower respiratory diseases which eventually lead to death.

   - [ ] **Alternative Hypothesis** - There is a relation between pollutants that cause chronic lower respiratory diseases which eventually lead to death.

## Data Exploration & Cleanup

<details>
  <summary>Dependencies and Setup</summary>
  <p> - import matplotlib.pyplot as plt</p>
  <p> - import pandas as pd</p>
  <p> - import numpy as np</p>
  <p> - import scipy.stats as st</p>
</details>

### Cleaning Mortality Data
1. From wonder.cdc.gov, we made an API call request and saved it as [*California_Mortality.csv*](http://localhost:8888/edit/Resources/California_Mortality.csv), which included deaths in California from 2006 to 2016 
2. Filtered for mortality data from years less than 2011    
   1. mortality_2006_2010 = mortality_df[mortality_df["Year"] < 2011]
   2. Saved as [*mortality_2006_2010_clean.csv*](http://localhost:8888/edit/Resources/mortality_2006_2010_clean.csv)
3. Removed 'County, CA’ with blank using the str.replace() function 
4. Dropped the ‘Notes’ and ‘Year Code’ columns using the .drop()
5. Replaced .0 in the Year column with a blank using str.replace()
6. Find out how many counties are listed using .unique().tolist() 
    1. there are 54 total
7. Matched the number of mortality counties with that in the pollution data using .isin(x)
8. Saved finalized cleaned dataset as *mortality_data_clean_df*
### Cleaning Pollution Data
9. From kaggle.com, we downloaded the US Pollution Information (2000-2010) dataset and saved it as [*California_Pollution.csv*](http://localhost:8888/edit/Resources/California_Pollution.csv)
10. Filtered for pollution data for years greater than 2005 
    1. pollution_2006_2010 = pollution_df[pollution_df["Year"] > 2005]
    2. Saved as [*pollution_2006_2010.csv*](http://localhost:8888/edit/Resources/pollution_2006_2010.csv)
11. Removed '#' from 'ICD-10 113 Cause List' and replaced it with blank using str.replace()
12. Find out how many counties are listed using .unique().tolist() 
    1. there are 18 total
13. Saved final cleaned dataset as *pollution_data_df*
### Merging Datasets!!!
14. Combined our mortality_data_clean_df with pollution_data_df using .combine_first()
    1. This function worked best b/c it allowed the union of two series even though they each have a lot of null values. This method prioritizes the first call series, in this case, the pollution data frame. So if there is null value, it will take the value at the same position and index from the second series, or our mortality data frame.
15. Replaced all 'NaNs' values with 0 using .fillna(0)

## Findings from our Data Visualizations

### Question 1
**Are deaths caused by chronic lower respiratory diseases (CLRD) linked to changes in AQI and air pollutant levels?** 

Between 2006 and 2010 and in all 18 California counties…
  * CO AQI vs. total mortality due to CLRD: The R-Value is 0.7543850834952978 
   - [x] This indicates a strong correlation between higher CO AQI and death from Chronic Lower Respiratory Disease.
  * NO<sub>2</sub> AQI vs. total mortality due to CLRD: The R-Value is 0.8827775793559318 
   - [x] This indicates a very strong correlation between higher NO<sub>2</sub> AQI and death from Chronic Respiratory Disease.
  * SO<sub>2</sub> AQI vs. total mortality due to CLRD: The R-Value is 0.6170401313230505 
   - [x] This indicates a fairly strong correlation between higher SO<sub>2</sub> AQI and death from Chronic Respiratory Disease.
  * O<sub>3</sub> AQI vs. total mortality due to CLRD: The R-Value is 0.5435496110691815 
   - [x] This indicates a moderate correlation between higher O<sub>3</sub> AQI and death from Chronic Respiratory Disease.

### QUESTION 2
**Which of these air pollutants (CO, O<sub>3</sub>, NO<sub>2</sub>, SO<sub>2</sub>) have a greater influence, if at all, on the mortality rate due to CLRD?** 

*Analysis of Mean of 4 different AQI levels in California counties*


    <img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/mq_charts/years_co.png">

 * Average CO AQI (2006-2010) vs. Counties: we found that Imperial county has the highest levels of CO (16 ppm). 
      * We think it's possibly due to the wildfires that are a prominent challenge in SoCal, especially during the hot and dry season.
      * For reference, the U.S. National Ambient Air Quality Standards for CO for 8 hours is 9 ppm(parts per million).

    <img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/mq_charts/years_no2.png">
          
 * Average NO<sub>2</sub> AQI (2006-2010) vs. Counties: LA and San Bernardino have the highest levels of NO<sub>2</sub>, but they are still below the EPA standard. 
    * High levels of NO<sub>2</sub> could be linked to the notorious LA traffic, numerous fossil fuel plants and industries, and consistent drought conditions. Additionally, geographically the LA county is a large basin with the Pacific Ocean and surrounded by several mountain ranges with 11,000-foot peaks in the east and south. The health problems that possibly follow could be asthma and respiratory infections.
    * For reference, the EPA annual average NO2 standard is 53 ppb.

    <img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/mq_charts/years_so2.png">
     
 * Average SO<sub>2</sub> AQI (2006-2010) vs. Counties: San Diego and Contra Costa have the highest levels. 
    * One factor could be that SD is part of the San Diego Air Basin (SDAB), a subtropical climate zone characterized by hot/dry summers and mild/wet winters. Additionally, a combination of light winds, stagnant air, little precipitation, and 170+ days of over 70 degrees weather create the ideal conditions for pollution accumulation in the atmosphere. 
    * For reference, in 2010, the Primary National Ambient Air Quality Standard (NAAQS) for Sulfur Dioxide was implemented, establishing the standard to be 75 parts per billion.

     <img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/mq_charts/years_o3.png">

  * Average O<sub>3</sub> AQI (2006-2010) vs. Counties: Fresno, Riverside, and San Bernardino have the maximum levels respectively 
    * Ground-level ozone is created when sunlight strikes pollutants called nitrogen oxides found in the air.
    * Riverside and San Bernardino counties are located in SoCal where there is constant sunshine and heat is the norm, ozone levels tend to be more elevated. 

**Average Air Pollutants Over Time**

    <img src="http://localhost:8888/view/mq_charts/years_avg_pollutants.png">

*Observed Trend : There is an overall decline of  Average Pollutants’ AQI  Levels for California State from 2006 to 2010.*

   * This observed downward trend could be attributed to the California Senate Bill No. 1368, which placed new emission standards for electrical utilities that contribute to combustion of greenhouse gases. EPA’s national and regional rules to reduce emissions of pollutants are strictly implemented.
      * [Reference](https://en.wikipedia.org/wiki/Global_Warming_Solutions_Act_of_2006) 

### Mortality in California from 2006-2010

  * Chronic lower respiratory diseases have the highest percentage rate at 31.11 %. This category includes...
    * J40  Bronchitis, not specified as acute or chronic
    * J41  Simple and mucopurulent chronic bronchitis
    * J42  Unspecified chronic bronchitis
    * J43  Emphysema
    * J44  Other chronic obstructive pulmonary disease
    * J45 & J46  Asthma
    * J47  Bronchiectasis
  * But other chronic lower respiratory diseases aren't far behind, with 27.17% of the total. These include just...
    * J44  Other chronic obstructive pulmonary disease
    * J47  Bronchiectasis
  * Thus, about 58% of all of the respiratory diseases come from CLRD.
  * Asthma (0.52%), pneumonitis due to solid & liquid (1.36%), and emphysema (2.14%) are the lowest causes of deaths
  * Influenza & pneumonia (16.50%) J09-J18 and just pneumonia (16.15%) J12-J18
<img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/piechart.png">

### Question 3
**If we find trends that deaths and pollution are correlated, can we further prove that there is a delayed effect from exposure to toxic air pollutants on the mortality rate caused by CLRD?**

We examined 4 of the most populous counties in California (from 2006 to 2010) to see if the increase in the Air Quality Index (AQI) of these pollutants led to an increase in the total number of deaths from CLRD. 

***LA County***
<img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/LA_Pollutants.png">
  * In LA county, Mortality from CLRD vs. Total AQI of 4 Pollutants: 
    * There's opposing trends seen when comparing all four air pollutants to mortality rate between 2006 and 2010. For instance, as CO AQI decreased, mortality rate increased. In 2009, mortality in LA reached its peak while all four pollutants dropped its lowest within that time frame. In conclusion, there is not enough evidence to prove that there is a delayed reaction between an overall decrease in toxic air pollutants and changes in mortality rate due to CLRD.

***Contra Costa County***
<img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/ContraCosta_Pollutants.png">
  * In Contra Costa county, Mortality from CLRD vs. Total AQI of 4 Pollutants:
    * Contrarily to LA county, Contra Costa county exhibits a better story. As all four air pollutants AQI levels dropped overall, mortality rate seemed to follow a similar trend from 2008. There seems to be a delayed reaction to the decrease in pollution and mortality rate in Contra Costa. 

***SD County***
<img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/SD_Pollutants.png">
  * In SD county, Mortality from CLRD vs. Total AQI of 4 Pollutants:
    * Similarly to LA county, SD county does not have a clear storyline. SD exhibits fluctuations in all four pollutant levels as it initially decreases in 2007, rises in 2008, drops again in 2009, and then reaches a new peak in 2010. There is a slight delay correlation between the rise and dip in pollution levels with mortality decreasing from 2008 to 2010. 

***San Bernardino County***
<img src="https://github.com/dalismo/Project-1/blob/d22c77172946baee473582b90a0eebebc0b1046f/SB_Pollutants.png">
  * In San Bernardino county, Mortality from CLRD vs. Total AQI of 4 Pollutants:
    * Each air pollutant in SD county dropped in 2007 and peaked to its highest in 2008, while mortality rate fell in 2007 and overall rose the next few years. From observation, there is not a delayed response between the fluctuations in pollution levels and mortality rate. 

## Conclusion
  
  We were able to see enough correlation in our analysis and visualizations to support our alternative hypothesis... that there is a slight correlation between high toxic air pollutants and death caused by chronic lower respiratory diseases in California residents in 2006-2010. Diving deeper in our data, we looked at four of the most populous counties in California and compared it to the mean AQI of all four pollutants. To our surprise, Contra Costa county (located in the northern portion of the East Bay area) exhibits the best story. As all four pollutants' AQI overall fell, mortality rate seemed to follow a similar delayed trend after 2008. The other three counties (LA, San Bernardino, and SD) had unclear story to depict any relationships.
  
  To find more tangible results, we calculate the correlation coefficient to see how strongly average AQI levels for each air pollutant is connected to death from CLRD in California. NO<sub>2</sub> had the highest R-value of 0.883, which indicates a pretty strong relationship between NO2 levels and its role in mortality rate. A bit of context, NO<sub>2</sub> is a reddish-brown gas with a pungent, acrid odour that can cause bronchoconstriction, inflammation, reduced immune response, and harmful effects on the heart. CO had the following highest R-value of 0.754.  
  
  On the otherhand, there is an overall decrease in average AQI levels for all four air pollutants. This could be attributed to the California Senate Bill No. 1368 signed in 2006, which instituted emissions standards that affect the output of greenhouse gases. The purpose of this bill was to lower the emmissions of these gases into the atmosphere and promote cleaner energy.  
  

## Limitations

  * Between the Pollution and Mortality files, the overlapping data spanned only from 2006 to 2010 (US Pollution Data was from 2000 - 2016 and the Mortality data for California was from 2006 - 2016)
  * We only used 16 out of 58 counties in California because the Pollution file had information for just 18 counties and most counties had missing information.
## Challenges
  * Used 2 datasets and had issues finding the relationship between mortality and pollution levels
  * We had frequent Github push and pull challenges since this was our first group project sharing a repository.
  * After our cleaning and visualizations, we had some difficulties putting the story together. Initially, we didn’t realize the number of counties and the years that both datasets shared data was a limitation. With a smaller dataset from the start, picturing a storyline was restricted as well. 

-------- 
# Data and Supplemental Sources

> [www.Kaggle.com](https://www.kaggle.com/sogun3/uspollution) 
>>
>> where we downloaded the U.S. Pollution Information (2000-2016)
>>
> [wonder.cdc.gov](https://wonder.cdc.gov/controller/datarequest/D76) 
>>
>> API request for Underlying Cause of Death, 2000-2010 for California
>>
> [web.archive.org](https://web.archive.org/web/20181119041829/http://www.fire.ca.gov/fire_protection/downloads/siege/2007/Overview_CompleteFinal.pdf)
>>
>> background information on the California Fire Siege 2007 
>>
> [leginfo.legislature.ca.gov](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=200520060SB1368)
>>
>> background information on the Senate Bill No. 1368 Electricity: Emissions of Greenhouse Gases

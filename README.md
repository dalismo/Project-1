# Analysis of Pollutants in California

Project 1 for Rutgers Data Science Bootcamp

### [Link to Presentation](https://docs.google.com/presentation/d/1iASbDnn62o1SOcaoT7vGkzs5uftBpUboqCBNdySm6Ts/edit#slide=id.p)

# Group Penny Members
* [Alberto Gonzalez]
* [Mubashira Qari]
* [Abayomi Olujobi]
* [Elise Eng]
* [Bertrand Louis]

# Data Sources and Supplemental Information

### [www.Kaggle.com](https://www.kaggle.com/sogun3/uspollution) 
US Pollution Information 2000-2016 download


### [wonder.cdc.gov](https://wonder.cdc.gov/controller/datarequest/D76) 
Underlying Cause of Death, 2000-2010 Request for California

### [web.archive.org](https://web.archive.org/web/20181119041829/http://www.fire.ca.gov/fire_protection/downloads/siege/2007/Overview_CompleteFinal.pdf)
California Fire Siege 2007 

### [leginfo.legislature.ca.gov](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=200520060SB1368)
Senate Bill No. 1368 Electricity: emissions of greenhouse gases.

#### Questions posed on data

**1.** Are deaths caused by chronic lower diseases (CLRD) directly linked to pollutants?

**2.** Are we able to explain the increase and decrease in the Air Quality Index (AQI) associated with carbon monoxide (CO), ozone (O3), nitrogen dioxide (NO2) and sulfur dioxide (SO2)?

**3.** Can we prove that there is a lag between the consumption of pollutants and mortality rate?

### Null and Alternative Hypothesis

**Null Hypothesis** - The fluctuations in the Air Quality Index (AQI) based on the pollutants CO, O3, NO2 and SO2 do not lead to deaths in California casued by chronic lower respiratory diseases.

**Alternative Hypothesis** - Yes, there is a direct correlation between increased level of pollutants affecting the AQI that do lead to more deaths caused by chronic lower respiratory diseases.

## Summary

  Our group used US pollution data from 2000 to 2016 to see how the Air Quality Index is adversely affected by carbon monoxide (CO), ozone (O3), nitrogen dioxide (NO2) and sulfur dioxide (SO2). Initially we focused on the entirety of the US but the data set was too large. Amongst ourselves we came to the conclusion to focus on California since the state is the most populated and also has the largest economy. Because of it's vast industry it would also have increased amounts of pollution affecting the air quality. As we analyzed and cleaned the data we then focused on a few counties for our review. With the pollution data for those counties we then downloaded mortality information from the CDC website for the state of California for the years 2000 - 2010 concentrating on deaths caused by chronic lower respiratory diseases. Luckliy that data was also by county. This would allow us to merge the data for further research. The thought process was to find a correlation between the inreased pollutants and deaths that are caused by chronic lower respiratory dieases (CLRD). CLRD is the fourth leading cause of death in the US. CLRD includes emphysema, chronic bronchitis, asthma, pulmonary hypertension, and occupational lung diseases. These types of diseases are normally found among smokers. However, constant exposure to air pollutantscan also play a role in the development of chronic lower respiratory disease, according to the Centers for Disease Control and Prevention (CDC).  
  
  ## Findings


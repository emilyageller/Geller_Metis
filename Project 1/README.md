# Geller_Metis
## EDA: New York City Subway Traffic and Demographic 

We hit the ground running in our first week at the Metis Data Science Bootcamp!

It was a shortened week, due to MLK day falling on Monday, so we had a pretty tight timeframe for our first project! It was assigned on Tuesday, with a due date of Friday.

We were given a scenario in which a ficticious company (WomenTechWomenYes - aka WTWY) had asked us to do some prelimanry EDA in order to gauge our potential for further collaboration. WTWY were, ostensibly, planning an annual Summer gala to increase brand awareness, donations and participation.  They want to send teams out to subway stations to promote the event, as well as to collect email addresses.  Those who register receive free tickets to the event.  The deliverable for this scenario was to provide recommendations on where to place street teams.

### Approach

Our strategy to provide valuable recommendations involved finding the top subway stations with respect to foot traffic, and then verifying that the population in the surrounding areas held demographics that could place them in WTWY's target audience. 

In order to do this, we used data from the NYC MTA to analyze foot traffic across the NYC subway system.  We also incorporated census data from the American Community Survey to analyze demographics, and Census location data to tie these two datasets together.

### Data

#### Turnstile Usage Data - 2016:

The dataset we used for station traffic involved records from the 2016 calendar year, and can be found [here](https://data.ny.gov/Transportation/Turnstile-Usage-Data-2016/ekwu-khcy). This source also provides a useful [overview of the data](https://data.ny.gov/api/views/ekwu-khcy/files/30554bf0-2ec6-4804-a91b-85185a96a877?download=true&filename=MTA_Turnstile_Data_Overview.pdf), as well as a [data dictionary](https://data.ny.gov/api/views/ekwu-khcy/files/e35d46bb-d988-44c5-a170-8736c1c773af?download=true&filename=MTA_Turnstile_Data_DataDictionary.pdf).

Included in this dataset was:  

* C/A, Unit and SCP: unique identifiers for turnstiles
* Station, Linename and Divison: information for each station
* Date, Time, Desc: temporal data and notes for each sample
* Entries and Exits: the volume of foot traffic in and out of the station for each sample

#### American Community Survey Data

Our demographic dataset came from the [American Community Survey](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml), though we used a [subset](https://www.kaggle.com/muonneutrino/new-york-city-census-data/downloads/nyc_census_tracts.csv) that had already been curated by [MuonNeutrino on Kaggle](https://www.kaggle.com/muonneutrino). 

This dataset included a lot of demographic information.  The specific features we looked for each area were:

* TotalPop, Men, Women: Sample populations
* Income: Median Household Income
* Transit: the percentage of the population commuting via public tranpsortaion
* CensusTract: id for each sample


We combined this with data from the [Census Block Conversions API](https://factfinder.census.gov/faces/nav/jsf/pages/index.xhtml) in order to look at the demographics geospatially.  This included:

* Latitude and Longitude
* BlockCode: id for each record

We combined these two census datasets on CensusTract and BlockCode. CensusTract is equivalent to the first 11 digits of BlockCode.


### Data Cleanup

Luckily, the Census datasets were already relatively clean.

The MTA data was a different story!

A few of the issues we had to address were:  

* the fact that samples were on an individual turnstile level, rather than per station
* samples were cumulative across time
* some turnstiles were defective, meaning they'd reset randomly, subtract values and sometimes send the same record twice

We dealt with this by:

* aggregating individual turnstile traffic for each station
* distributing traffic across time intervals per station
* filtering for outliers, discarding the 99% quantile


### Subway Traffic Findings

Once we had our data in a relatively clean state, we analyzed the top stations by traffic.  We measured traffic by adding the number of entrances and exits for each station together, to get an absolute total.

We found that the top stations were in central Midtown Manhattan, and were all major hubs.  The top 20 stations according to our analysis are shown below:

![Top 20 Stations, 2016](/images/top_20_stations.png "Top 20 Stations, 2016")

Once we had an idea of our top performers, we decided to zoom in and look at traffic at each of the top 4 stations.  They had very similar distributions:

![](../../emilyageller.github.io/images/station_traffic_penn_st.png)

![](../../emilyageller.github.io/images/station_traffic_23rd_st.png)

![](../../emilyageller.github.io/images/station_traffic_34_herald.png)

![](../../emilyageller.github.io/images/station_traffic_times_42.png)

Each of the top stations has a conspicuous spike in March and, upon further investigation, we saw that this was consistent across all of the stations in the subway system.  This either points to an actual spike in traffic, or (more likely) some further data cleaning that we should do.

Since we had a tight timeframe, we decided to use this as is. 

Some notable observations from these graphs are:  

* spikes occur on weekdays
* dips occur on weekends
* there is slightly more traffic in the spring and summer
* there is a gap in june, where our filtering probably identified outliers (this could be revisited to ensure we didn't filter out valid samples)

### Demographic Analysis

We built demographic heatmaps using the two census datasets (and matplotlib) to show our top performing stations and characteristics of their surrounding populations.

##### Median Household Income:
![](../../emilyageller.github.io/images/median_household_income.png)

On this map, we can see that 34 Penn St and 23 St stations (which happen to be our top 2 in terms of traffic), also have the highest median household income.  This is interesting, since we would like to send the street teams to areas with disposable income for increased chances of donations.

##### Female Population:
![](../../emilyageller.github.io/images/female_population.png)

Of the top ten stations, 23rd St and 34 Herald Sq are surrounded by the highest female percentage of population.  We're interested in female participation in the gala, so sending stream teams to areas with a high concentration of women could be a good strategy.

##### Percentage of Population Commuting via Public Transportation:
![](../../emilyageller.github.io/images/transit.png)

The top stations that also had the highest percentage of commutors on public transport were 23 St and Times Sq - 42nd St. 

##### Tech Hubs:
![](../../emilyageller.github.io/images/tech_hubs.png)

A few of the top stations were near tech hubs. Focusing on the top five, 34 Herald Sq and Grand Central-42 St really stand out.  These would be good stations to target, since they have high foot traffic that may be interested in tech.

### Combined Analysis and Recommendations
We combined both the station traffic analysis and the demographic analysis in order to make our recommendations in terms of stations that WTWY should target with street teams.

We compared demographics for each of the five subway stations with heaviest traffic.

High Traffic Stations 	 | Surrounding Demographic Highlights
------------- | -------------
34 Penn St Station  | High median household income ($159821)
23rd St Station | High female population (60.7%), income ($135750) and  transit percentage (48.4%)
34th Herald Sq | Near tech hubs
Times Sq 42nd St Station | High transit percentage (37.2%)
Grand Central 42nd St | Near tech hubs


All in all, we found favorable trends for WTWY in Manhattan in terms of stations to target with street teams.  A few of the major hubs also have demographics that place a high percentage of their surrounding population in WTWY's target audience.

Based on our findings so far, we would recommend focusing street teams at:  
1. 34 Penn St Station,  
2. 23rd St Station,  
3. 34th Herald Sq,  
4. Times Sq 42nd St Station, and   
5. Grand Central 42nd St.


### If we had more time...
As I said earlier, this project was done on a pretty tight timeframe, and there was a lot more that we could have done!

A few things that would be next steps in this analysis are:  

* dig a bit deeper in terms of outliers  
	* investigate the March spike,
	* look into the missing records in June,
	* try different filter values
* analyze traffic data for temporal trends
	* seasonal
	* weekday/weekend
	* time of day
* create a demographic 'scorecard' for each station, so that we can better prioritize our recommendations

--

Overall this was a great first project! We learned a lot, and were definitely thrown in the deep end.  Putting ourselves in this project oriented mindframe has set the tone for the rest of the course.  

We presented our findings at a mock client meeting with a deck that can be found [here](https://docs.google.com/presentation/d/1daA66nUAfeK-DIv_iJcl1n506gSXo9g3z4hOuhh6arc/edit#slide=id.p)

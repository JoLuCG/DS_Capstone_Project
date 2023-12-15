# BUILDING ENERGY CONSUMPTION PREDICTOR (BECP)
    ...less energy, more future!
Introduction
----------------------
How much energy will a building consume? This is the question that the Building Energy Consumption Predictor (BECP) model aims to answer. 

Buildings account for 30% of global energy consumption and 26% of global energy-related emissions(1). Fortunately, substantial investments are being made to enhance building efficiencies, aiming to reduce energy consumption and emissions. However, building owners often find themselves questioning whether these investments make business sense and if the improvements are performing as anticipated.

This is why an increasing number of building owners opt for retrofit companies that provide 'pay-for-performance financing.' In this program, owners make payments based on the difference between their actual energy consumption and what they would have consumed without any retrofits. Typically, the latter values are derived from a software energy model, but its estimations often lack cohesion and struggle to scale effectively. An alternative solution lies in the BECP model, capable of accurately predicting metered building energy usage across several areas: chilled water, electric, hot water, and steam meters. 

With better estimates of these energy-saving investments, not only building owners but also large scale investors and financial institutions will be more inclined to invest in this area to enable progress in building efficiencies.


(1) International Energy Agency website < https://www.iea.org/energy-system/buildings >


Overview
----------------------
The problem statement revolves around the inefficiency and uncertainty in evaluating the effectiveness of building retrofits and their impact on energy consumption.

The solution presented by the project involves implementing the Building Energy Consumption Predictor (BECP) model. This model aims to resolve the inefficiencies and uncertainties in evaluating the effectiveness of building retrofits by providing precise predictions of metered building energy usage across categories such as chilled water, electric, hot water, and steam meters. Additionally, it empowers building owners to confidently assess the efficacy of their retrofit investments, offering a clear understanding of whether the retrofits are financially sound and if the improvements align with anticipated energy and sustainability goals.

The key features of the Building Energy Consumption Predictor (BECP) model are:

-	BECP offers accurate predictions of energy usage across various metered categories within buildings, including chilled water, electric, hot water, and steam meters. This comprehensive approach ensures a holistic understanding of energy consumption patterns.
-	It aids in identifying whether improvements meet the anticipated energy-saving and sustainability benchmarks set for the building.
-	Serves as a decision support tool, assisting stakeholders in making informed decisions regarding retrofit initiatives. Its insights help prioritize investments that yield both financial and environmental benefits.
-	The model is designed to provide precise and scalable predictions what makes it suitable for diverse building types and sizes.

These features collectively position BECP as a comprehensive, accurate, and decision-enabling tool for evaluating and optimizing building energy consumption post-retrofit.

Dataset description
----------------------

The dataset comprises data collected from a comprehensive study conducted across more than 1,000 buildings over a span of three years.

The raw dataset can be found in ASHRAE Great Energy Predictor (AGreEP) III from [Kaggle](https://www.kaggle.com/competitions/ashrae-energy-prediction/data). It consists of three CSV files:
-	train.csv: Contains meter readings per meter type (electricity, chilledwater, steam, hotwater) for multiple buildings.
-	building_meta.csv: Provides key features for each building, including activity type, area, year built, and number of storeys.
-	weather.csv: Includes meteorological data corresponding to the time of meter readings.

The raw dataset originally comprises around 20 million rows. For ease of process, it has been filtered down to a subset of 397,992 rows and 17 columns. Most columns contain numeric data, with only three being categorical.

For License and Usage, the dataset can be used for educational purposes, academic research and education.

This dataset provides a valuable resource for analyzing energy consumption trends across diverse buildings and exploring the relationship between building attributes, meteorological conditions, and energy usage patterns.

Dictionary
----------------------
**Target / dependent variable**
- `meter_reading`, the target variable. Energy consumption in kWh.

**Predictor / independent variables**
- `building_id`, foreign key for the building metadata.
- `meter_type`, the  meter id code. Read as {0: electricity, 1: chilled water, 2: steam, 3: hot water}.  Not every building has all meter types.
- `meter_timestamp`, when the measurement was taken. Same as `weather_timestamp`.
- `site_id`, foreign key for the weather files.
- `primary_use`, indicator of the primary category of activities for the building.
- `square_feet`, gross floor area of the building in ft2.
- `year_built`, year building was opened.
- `floor_count`, number of floors of the building.
- `weather_timestamp`, when the measurement was taken. Same as `meter_timestamp`.
- `air_temperature`, degrees celsius.
- `cloud_coverage`, portion of the sky covered in clouds, in oktas.
- `dew_temperature`, degrees celsius.
- `precip_depth_1_hr`, millimeters.
- `sea_level_pressure`, millibar/hectopascals.
- `wind_direction`, compass direction (0-360).
- `wind_speed`, meters/second (m/s).

Data wrangling
----------------------
This section initiates the transformation and structuring of data from its raw form into a preferred format, aiming to enhance data quality and usability for analytics or machine learning purposes. It encompasses tasks such as data loading, dataset cleansing, reviewing null values to determine their removal or treatment, and identifying and managing duplicate rows.

Exploratory data analysis
----------------------
The exploration of datasets involved thorough analysis, incorporating data visualizations. These visuals play a crucial role by simplifying intricate information into an easily digestible format, facilitating quick identification of patterns, trends, and relationships within the data. Specifically focusing on numerical columns, with 'Reviewer_Score' as the primary point of interest, these visualizations aim to extract insights.

Statistics
----------------------
Statistical analysis will help reveal patterns, relationships, and trends crucial for understanding customer preferences and guiding decisions to enhance hotel service and satisfaction. Tasks like column correlation, heatmap visualization, and seeking correlation coefficients will be conducted for this purpose.

Modeling
----------------------
Modeling, including time series analysis, plays a critical role in uncovering patterns, predicting outcomes, and pinpointing crucial factors affecting the target variable, providing valuable insights for decision-making. In the context of this energy consumption prediction model for buildings, incorporating time series analysis optimizes efficiency and informs decisions for sustainable building management.

Time series analysis was selected due to the dataset's sequence of energy consumption observations indexed by hourly timestamps. Its objective is to forecast future energy consumption patterns by leveraging historical data.

Conclusions
----------------------
The Trend-Seasonal Decomposition analysis highlights distinct features: a slight upward trend evident before and after May, coupled with a plateau during this period. Daily variations remain consistent, as demonstrated in the seasonal plot. However, the residual component showcases irregular patterns with no clear trend and displays changing variance, indicating heteroscedasticity within the dataset.

Repository structure
----------------------
    ├── 01_notebooks                        <- Folder for Jupyter code notebooks
        ├── data                            <- Folder for data files 
            ├── .gitignore                  <- Files to ignore
            ├── 01_healthcare_train_df.csv  <- Export from Jupyter file, includes the 'Healthcare' category subset
        ├── .DS_Store                       <- ?
        ├── .gitignore                      <- Files to ignore
        ├── Sprint_1_Capstone_BECP.ipynb    <- Capstone Jupyter file, includes files merging, subset dataframe and EDA
        ├── Sprint_2_Capstone_BECP.ipynb    <- Capstone Jupyter file, includes more advanced preprocessing, EDA and baseline model creation.      
    ├── 02_presentations                    <- Folder for Capstone's presentations
        ├── .gitignore                      <- Files to ignore
        ├── Sprint_1_BECP.pdf               <- Presentation for Sprint 1
        ├── Sprint_2_BECP.pdf               <- Presentation for Sprint 2         
    ├── .DS_Store                           <- ?
    ├── .gitignore                          <- Files to ignore
    ├── README.md                           <- Explanation of how to navigate the code in the repository.
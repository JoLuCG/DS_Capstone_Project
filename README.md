# BUILDING ENERGY CONSUMPTION PREDICTOR (BECP)
    ...less energy, more future!
Introduction
----------------------

How much energy will a building consume? This is the question that the Building Energy Consumption Predictor (BECP) model aims to answer. This model predicts energy usage for Healthcare buildings, aiding owners in assessing retrofit effectiveness and sustainability goals.

Buildings account for 30% of global energy consumption and 26% of global energy-related emissions(1). Fortunately, substantial investments are being made to enhance building efficiencies, aiming to reduce energy consumption and emissions. However, building owners often find themselves questioning whether these investments make business sense and if the improvements are performing as anticipated.

This is why an increasing number of building owners opt for retrofit companies that provide 'pay-for-performance financing.' In this program, owners make payments based on the difference between their actual energy consumption and what they would have consumed without any retrofits. Typically, the latter values are derived from a software energy model, but its estimations often lack cohesion and struggle to scale effectively. An alternative solution lies in the BECP model, capable of accurately predicting electricity building energy usage.

With better estimates of these energy-saving investments, not only building owners but also large scale investors and financial institutions will be more inclined to invest in building retrofits.


(1) International Energy Agency website < https://www.iea.org/energy-system/buildings >


Overview
----------------------
The problem statement revolves around the inefficiency and uncertainty in evaluating the effectiveness of building retrofits and their impact on energy consumption.

The solution presented by the project involves implementing the Building Energy Consumption Predictor (BECP) model. This model aims to resolve the inefficiencies and uncertainties in evaluating the effectiveness of building retrofits by providing precise predictions of electricity usage in buildings. Additionally, it empowers building owners to confidently assess the efficacy of their retrofit investments, offering a clear understanding of whether the retrofits are financially sound and if the improvements align with anticipated energy and sustainability goals.

The key features of the Building Energy Consumption Predictor (BECP) model are:

-	BECP offers predictions of electricity usage. This comprehensive approach ensures a holistic understanding of energy consumption patterns.
-	It aids in identifying whether improvements meet the anticipated energy-saving and sustainability benchmarks set for the building.
-	Serves as a decision support tool, assisting stakeholders in making informed decisions regarding retrofit initiatives. Its insights help prioritize investments that yield both financial and environmental benefits.

These features collectively position BECP as a comprehensive, accurate, and decision-enabling tool for evaluating and optimizing building energy consumption post-retrofit.

Dataset description
----------------------

The dataset comprises data collected from a comprehensive study conducted across more than 1,000 buildings over a span of three years.

The raw dataset can be found in ASHRAE Great Energy Predictor (AGreEP) III from [Kaggle](https://www.kaggle.com/competitions/ashrae-energy-prediction/data). It consists of three CSV files:
-	train.csv: Contains meter readings per meter type (electricity, chilled water, steam, hot water) for multiple buildings.
-	building_meta.csv: Provides key features for each building, including activity type, area, year built, and number of storeys.
-	weather.csv: Includes meteorological data corresponding to the time of meter readings.

The raw dataset originally comprises around 20 million rows. For ease of process, it has been filtered down to a subset of 397,992 rows and 17 columns. Most columns contain numeric data, with only three being categorical.

For License and Usage, the dataset can be used for educational purposes, academic research and education.

This dataset provides a valuable resource for analyzing energy consumption trends across diverse buildings and exploring the relationship between building attributes, meteorological conditions, and energy usage patterns.

Assumptions
----------------------
- Patterns observed in historical data will generalize to future scenarios is fundamental. However, changes in building structure, technology, or user behavior might challenge this assumption.
- External factors such as policy changes, environmental shifts, or advancements in technology that might influence energy consumption patterns is important for a comprehensive model.

Limitations
----------------------
- The model's accuracy heavily relies on the quality and completeness of the data. Inaccurate, or incomplete data could lead to misleading predictions.
- Insufficient historical data might limit the model's ability to capture diverse scenarios and trends, especially if the retrofits or changes in building characteristics are recent.
- Assuming stationary might not hold in real-world scenarios where building usage, occupancy, or environmental conditions vary significantly over time.
- If significant changes occur in the building structure, retrofits, or technology during or after model development, the model might become less relevant or require recalibration.

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
This section initiates the transformation and structuring of data from its raw form into a preferred format, aiming to enhance data quality and usability for analytics or machine learning purposes. It encompasses tasks such as data loading for three CSV files, cleansing, merging into a one dataset and finally filtering such data set into a subset. This smaller subset exclusively contains data relevant to the healthcare primary use. Its reduced size aims to simplify data manipulation and expedite processing time on the PC.

Exploratory data analysis
----------------------
The exploration of datasets involved thorough analysis, incorporating data visualizations. These visuals play a crucial role by simplifying intricate information into an easily digestible format, facilitating quick identification of patterns, trends, and relationships within the data. Specifically focusing on numerical columns, with `meter_reading` as the primary point of interest, these visualizations aim to extract insights.

Statistics
----------------------
Statistical analysis will help reveal patterns, relationships, and trends crucial for understanding customer preferences and guiding decisions to enhance `meter_reading` accuracy. Tasks like column correlation, heatmap visualization, and seeking correlation coefficients will be conducted for this purpose.

Modeling
----------------------
Modeling plays a critical role in uncovering patterns, predicting outcomes, and pinpointing crucial factors affecting the target variable, providing valuable insights for decision-making. In the context of this energy consumption prediction model for buildings, incorporating time series analysis optimizes efficiency and informs decisions for sustainable building management. Additionally to the time series models, we also studied other regressor models such as XGBoost and Random Forest, and finalized the modelling with Multivariate time series analysis. 

Interpretability
----------------------
This subject provides insights into how the model arrives at its predictions, offering a deeper understanding of the relationships between input features and the predicted outcomes. In the context of health care buildings electricity consumption prediction, interpretability helps identify the most influential factors impacting electricity usage, aiding stakeholders in making informed decisions regarding energy-efficient practices or retrofit investments. 

Conclusions
----------------------
The project concludes with the determination that among the models analyzed, the Random Forest Regressor stands out with the lowest Mean Absolute Error (MAE). This finding signifies its efficacy as the most reliable model for predicting electricity consumption in healthcare buildings. Notably, through analysis, it becomes evident that features linked to thermal comfort, such as dew and air temperature, play a pivotal role in influencing energy consumption patterns within these structures. Understanding and prioritizing these comfort-related features are pivotal for accurate predictions and informed decisions towards enhancing energy efficiency in healthcare buildings.

Repository structure
---------------------
Keep in mind that the notebooks should be executed in ascending order by name, as each one generates CSV files utilized in the subsequent notebooks.


    ├── 01_notebooks                        <- Folder for Jupyter code notebooks
        ├── data                            <- Folder for data files 
            ├── .gitignore                  <- Files to ignore
            ├── 01_healthcare_train_df.csv  <- Export from Jupyter file, includes the 'Healthcare' category subset
        ├── .gitignore                      <- Files to ignore
        ├── 01_dataset_filtering.ipynb      <- Capstone Jupyter file, includes data wrangling, merging and filtering. 
        ├── 02_EDA_stats.ipynb              <- Capstone Jupyter file, includes data preprocessing, EDA and statistical analysis.
        ├── 03_modelling_timeseries.ipynb   <- Capstone Jupyter file, includes the baseline, AR and ARIMA models.
        ├── 04_modelling_regressors.ipynb   <- Capstone Jupyter file, includes XGBoost, Random Forest and Multivariate analysis.         
    ├── 02_presentations                    <- Folder for Capstone's presentations
        ├── .gitignore                      <- Files to ignore
        ├── Sprint_1_BECP.pdf               <- Presentation for Sprint 1
        ├── Sprint_2_BECP.pdf               <- Presentation for Sprint 2
        ├── Sprint_3_BECP.pdf               <- Presentation for Sprint 3      
    ├── .gitignore                          <- Files to ignore
    ├── README.md                           <- Explanation of how to navigate the code in the repository.
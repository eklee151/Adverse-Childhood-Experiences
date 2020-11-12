# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone: Adverse Childhood Experiences
## Eboni Lee, DSIR-824

# Executive Summary
Adverse Childhood Experiences (ACEs) are defined by the Children's Bureau as "traumatic events occurring before the age of 18". They can be categorized as abuse, household challenges and neglect.  

## Problem Statement
Can Adverse Childhood Experiences (ACEs) be used to predict future behavior and outcomes?
   - How well can it be used to predict whether someone's use of smokeless tobacco products?
   - How well can it be used to predict whether someone's activity limitation due to health problems?
   - How well can it be used to predict whether someone is in good or poor health?
   - How well can it be used to predict someone’s smoker status?
   - Can factors other than ACE influence the precision of the models?
   
## Packages
```imblearn```
```xgboost```

### Contents:
- 1_data_collection_inspection
- 2_data_cleaning
- 3_eda
- 4_sample_data_models
- 5_best_models
- 6_heroku_flask_app
- assets
- README.md

## Data 
- The data was collected from the CDC's Behavioral Risk Factor Surveillance System (BRFSS), where the ACE module was included, for the years between 2009 - 2012. 
    - It can be downloaded [here](https://www.cdc.gov/brfss/about/archived.htm)
- The amount of features within the datasets range from 359 - 454: 
    - After cleaning, analysis and modeling was only performed on the 31 features, including ACEs, below
    
### Data Dictionary
|Feature|Type|Description|
|---|---|---|
|_STATE|nominal| State FIPS Code|
|DISPCODE|nominal| Final Disposition|
|PHYSHLTH|numerical| Number of Days Physical Health Not Good|
|MENTHLTH|numerical|Number of Days Mental Health Not Good|
|USENOW3|nominal|Use of Smokeless Tobacco Products|
|HISPANC2|nominal|Hispanic/Latino|
|MARITAL|nominal|Marital Status|
|CHILDREN|numerical|Number of Children in Household|
|EMPLOY|nominal|Employment Status|
|RENTHOM1|nominal|Own or Rent Home|
|SEX|nominal|Respondents Sex|
|QLACTLM2|nominal|Activity Limitation Due to Health Problems|
|ACEDEPRS|nominal|Live With Anyone Depressed, Mentally Ill, Or Suicidal?|
|ACEDRINK|nominal|Live With a Problem Drinker/Alcoholic?|
|ACEDRUGS|nominal|Live With Anyone Who Used Illegal Drugs or Abused Prescriptions?|
|ACEPRISN|nominal|Live With Anyone Who Served TIme in Prison or Jail?|
|ACEDIVRC|nominal|Were Your Parents Divorced/Seperated?|
|ACEPUNCH|nominal|How Often Did Your Parents Beat Each Other Up?|
|ACEHURT|nominal|How Often Did A Parent Physically Hurt You In Any Way?|
|ACESWEAR|nominal|How Often Did A Parent Swear At You?|
|ACETOUCH|nominal|How Often Did Anyone Ever Touch You Sexually?|
|ACETTHEM|nominal|How Often Did Anyone Make You Touch Them Sexually?|
|ACEHVSEX|nominal|How Often Did Anyone Ever Force You to Have Sex?|
|MSCODE|nominal|Metropolitan Status Code|
|_IMPAGE|numeric|Age value used to determine age groups|
|_RFHLTH|nominal|Adults with good or better health|
|_SMOKER3|nominal|Computed Smoking Status
|_PRACE|nominal|Computed Preferred Race|
|_EDUCAG|nominal|Computed level of education completed categories|
|_INCOMG|nominal|Computed income categories|
|_TOTINDA|nominal|Leisure Time Physical Activity Calculated Variable|

## Conclusion/Recommendations

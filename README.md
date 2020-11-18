# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Capstone: Adverse Childhood Experiences
## Eboni Lee, DSIR-824

# Executive Summary
Adverse Childhood Experiences (ACEs) are defined by the Children's Bureau as "traumatic events occurring before the age of 18". They can be categorized into abuse, household challenges and neglect. Their importance lies in the fact that they have been linked to a decreased lifespan, mental illness, decreased opportunities, chronic diseases, etc. Essentially, they can affect every aspect of someone's adult life negatively. Despite having so many negative effects, it is preventable and the effects can be mitigated, when resources and information are distributed correctly. 

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
- [1_data_collection_inspection](https://github.com/eklee151/Adverse-Childhood-Experiences/blob/main/1_data_collection_inspection.ipynb)
- [2_data_cleaning](https://github.com/eklee151/Adverse-Childhood-Experiences/blob/main/2_data_cleaning.ipynb)
- [3_eda](https://github.com/eklee151/Adverse-Childhood-Experiences/blob/main/3_eda.ipynb)
- [4_sample_data_models](https://github.com/eklee151/Adverse-Childhood-Experiences/tree/main/4_sample_data_models)
- [5_best_models](https://github.com/eklee151/Adverse-Childhood-Experiences/tree/main/best_models)
- [6_heroku_flask_app](https://github.com/eklee151/Adverse-Childhood-Experiences/tree/main/6_heroku_flask_app)
- [ACEs website](https://adverse-childhood-experiences.herokuapp.com/)
- [presentation](https://github.com/eklee151/Adverse-Childhood-Experiences/blob/main/Capstone.pdf)
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
|**USENOW3**|**nominal**|**Use of Smokeless Tobacco Products**|
|HISPANC2|nominal|Hispanic/Latino|
|MARITAL|nominal|Marital Status|
|CHILDREN|numerical|Number of Children in Household|
|EMPLOY|nominal|Employment Status|
|RENTHOM1|nominal|Own or Rent Home|
|SEX|nominal|Respondents Sex|
|**QLACTLM2**|**nominal**|**Activity Limitation Due to Health Problems**|
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
|**_RFHLTH**|**nominal**|**Adults with good or better health**|
|**_SMOKER3**|**nominal**|**Computed Smoking Status**|
|_PRACE|nominal|Computed Preferred Race|
|_EDUCAG|nominal|Computed level of education completed categories|
|_INCOMG|nominal|Computed income categories|
|_TOTINDA|nominal|Leisure Time Physical Activity Calculated Variable|

### Questions and Answers that will be predicted
- USENOW3 (Smokeless Tobacco Usage): Do you currently use chewing tobacco, snuff, or snus every day, some days, or not at all?
   - 0 = Unknown
   - 1 = every day
   - 2 = some days
   - 3 = not at all
- QLACTLM2 (Activity Limitations due to health problems): Are you limited in any way in any activities because of physical, mental, or emotional problems?
   - 0 = Unknown
   - 1 = yes
   - 2 = no
- _RFHLTH (good or poor health): Adults with good or better health vs. fair or poor health (based off of GENHLTH)
   - 0 = Unknown
   - 1 = Good or Better Health
   - 2 = Fair or Poor Health
- _SMOKER3 (Four-level smoker status): Everyday smoker, Someday smoker, Former smoker, Non-smoker (based off of SMOKE100 & SMOKEDAY)
   - 0 = Unknown
   - 1 = Current smoker (now smokes every day)
   - 2 = Current smoker (now smokes some days)
   - 3 = Former smoker, 4 = Never smoked

## Conclusion/Recommendations
Women are one of the most vulnerable populations. During EDA and after building my models, identifying as a women was a very important feature for almost all of the models I ran. Because of this, I believe the conversation should really focus on how can we protect young women and girls from ACEs and figuring out a way to decrease the # of ACEs they may experience. Location also matters, a lot of the models showed that living in Tennessee plays a major role in predicting. Unfortunately, there was nothing in the data that indicated as to why Tennessee was so important, but it's definitely something that will have to be looked into further. Lastly, the number of ACEs does count and plays an important role in all models where it was present.

It is also noteworthy to say that even though they are preventable when resources are allocated appropriately, the rate of them may be increasing. A study done between 1995-97 by the CDC and Kaiser Permanente showed people experiencing at least 1 ACE at a little under two-thirds. They only had 17,000 participants. My data showed that more than two-thirds of almost 118,000 participants had experienced 1 or more ACEs.

Data is important and can provide important insights into such a disturbing problem, but it doesn't matter without taking everything within context. Each person surveyed has a story that is uniquely their's and also one that we may never know. Just because we don't know eveything about each person's story, should not be a reason for discouragement, but for motivation to learn more about the stories of those who have experienced ACEs. Becoming aware of them an important first step in figuring out how to help and maybe even change the world in the process. 

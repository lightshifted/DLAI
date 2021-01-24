# DL.AI Captston Project: A Weekly Guide
This documentation outlines suggested courses of action taken each week. It's main purpose is to ensure our team stays on track 
and work is completed in a timely fasion.

## Week 11: ML Project Deployment and AWS ##
### The deliverables for this week are: ###
1. Collect quantitative results to share regarding benchmarking. Start getting output performance metrics of sub-modules of our code base. 
2. Prioritize the scripting and running of modules and submodules, retraining models and identifying limiting conditions and planning how to overcome them. 
3. Have begun AWS-based data processing
4. Have developed ideas on how the final deployed version should look. This includes the description of frontend and backend considerations.

#### Week 11 Tasks: ####
* [data preprocessing] Given url sequence data, identify indices of rows containing "specialization", which signify users who've purchased DLAI courses
* [data preprocessing] Merge url sequence array with hubspot export array to centralize users' information into a hub df. 
* [model building] Complete buildout of classification model and begin training using hubspot export array.
* [model building] Complete buildout of LSTM model and begin training it on url sequence data. 
* [commmunication] Continue to maintain regular communication between team members

## Week 10: Setting Goals and Effective Communication ##
#### The deliverables for this week are as follows: ####
1. Create slide deck for presentation to domain expert. Slide deck is to have: 
- description of work completed thus far categorized by: Data, Process, Outcome
- key results/metrics including examples of "bad" and "good" use cases
- key bottlenecks/hurdles the team is facing
- description of deliverables for week 11
2. Prioritize effective communication
- Set individual goals for team members and checkin (short meetings or over slack) frequently for updates. (atleast 2 meetings per week, if not more).
- Ensure team members are pushing code to github regularly (atleast once each week)
- Maintain a document where all team members can add their bottlenecks and challenges that must then be collated prior to meeting with SME.

#### Week 10 Tasks: ####
* [data preprocessing] Finish preprocessing of data set for clustering algorithim
* [model building] Build LSTM for feature based classification using `hubspot_export.csv`
* Begin preparations for model deployment on AWS

## Week 9: Project Baselining and Code ##
#### The deliverables for this week are as follows: #### 
1. Find a base paper and code and start getting it to run for your local data set. In terms of product rollout timplan, the baseline work represents 
the version that is most adaptable, can be prepared with minimal time commitment and that requires minimal resources (bandwidth, fast turnaround, minimal GPU support etc.)
2. Complete data preprocessing steps for training of baseline classification model. 

#### Base papers: #### 
1. Su. Q, Chen L. *A method for discovering clusters of e-commerce interest patterns using click-stream data.*(2014)(https://www.sciencedirect.com/science/article/abs/pii/S1567422314000726?via%3Dihub)
2. Roychowdhury S., et. al. *Categorizing Online Shopping Behaviour from Cosmetics to Electronics: An Analytical Framework.*(2020)(https://arxiv.org/abs/2010.02503)
3. Gang Wang, Xinyi Zhang, Shiliang Tang, Haitao Zheng, Ben Y. Zhao. Unsupervised Clickstream Clustering for User Behavior Analysis. Proceedings of SIGCHI Conference on Human Factors in Computing Systems (CHI), San Jose, CA, May 2016.

#### Week 9 Tasks: ####
* [data collection] Identify 1 public data set to benchmark on
* [data preprocessing] Extract *click-stream* data from data set, where *click-stream* data refers to the sequence of pages visited and the number of times these pages were viewed.
* [data preprocessing] Structure website categories using parsed URL information from `email_field_hist.csv`.
* [data preprocessing] Establish definition of user's interest using website categories that the user has visited (ascertained from tree topology) 
* [documentation] Complete definition of terms document for paper 1.
* [documentation] Create slide deck outlining goals and completed tasks for week 9
* [documentation] Create GitHub repository for project 
* [data preprocessing] Feature selection on `hubspot_export.csv` for 2 pre-selected targets

## Week 8: Project proposal ##
#### The deliverables for this week are as follows: ####
1. Student Project Template
2. System Design and Ethics considerations
3. Project Proposal slides

# Market Segmentation
The technical report for this task can be found at <a href="https://observablehq.com/d/49e10841552c7a46">Obervable</a>

### Engineered Features
Next, we used domain knowledge of our data to design additional relevant features for better model performance. From these engineered features, we were able to extract new knowledge which could not be ascertained from the initial features alone.
1. ${tex.block`\text t_1 = D_{first|open} - D_{first|send} `}
By taking the difference between when a user opened and clicked the first marketing email sent by Deeplearning.ai, we obtain metric time by which users' interest in their first marketing email can be gauged. 
2. ${tex.block`\text t_2 = D_{first|click} - D_{first|open} `}
The difference between when a user clicked and opened the first marketing email sent by Deeplearning.ai gives us a metric time by which users' interest in the emails' call to action can be gauged.
3. ${tex.block`\text t_3 = D_{last|click} - D_{first|click} `}
The difference in time between when a user clicked the last marketing email and when they clicked the first marketing email gives us a metric time to use for the identification of hot prospects; whereby small values signal users with high tendency to view successive emails.
4. ${tex.block`\text t_4 = D_{last|click} - D_{last|open} `}
By taking the difference between when users clicked and opened the last marketing email sent by Deeplearning.ai, we obtain a metric time to guage users' interest in the last marketing email's call to action. 
5. ${tex.block`\text t_5 = D_{last|open} - D_{last|send} `}
The difference between when users opened the last marketing email and gives us a metric time by which users' interest in the last marketing email can be measured. 
6. ${tex.block`\text S_{engagement} = (M_{clicked} * M_{opened}) / (M_{delivered}) `}
We obtained engagement scores for users by taking the product of the number of marketing emails clicked and marketing emails opened, and dividing it by the number of marketing emails delivered. 
7. ${tex.block`\text M_{effort} = (M_{delivered} * M_{opened}) / (1+M_{clicked}) `}
Marketing effort was obtained for each user by taking the product of the number of marketing emails delivered and the number of marketing emails opened, and dividing it the number of marketing emails clicked plus one.
8. ${tex.block`\sum_{i=1} time = t_1 + t_2 + t_3 + t_4 + t_5`}
Lastly, we sum engineered features ${tex`t_1`} through ${tex`t_5`} to obtain a score which relates to users' interest in marketing emails. 
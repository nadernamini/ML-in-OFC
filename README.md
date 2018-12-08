# DL and ML in OFC

## What is the central question that you are asking and why is it important? (max: 2 sentences)

(Jupyter Notebook) Can we use a machine learning model
, i.e. deep learning, to predict decisions based on 
neural activity in the orbitofrontal cortex? The 
answer to this question would allow us, by looking 
at the learned model, to better understand how 
patterns of neural activity can lead to a decision.

## Jupyter Notebook: What data do you plan to use? 
(be specific)
I will be using the 
[ofc-3 dataset](http://crcns.org/data-sets/ofc/ofc-3/about-ofc-2)
 which contains electrocorticography (ECoG) recordings
  from the orbitofrontal cortex (OFC) of n=10 
  neurosurgical patients being operated on for the 
  treatment of epilepsy. During the ECoG recordings,
   patients played a simple decision-making task 
   (a gambling game) ? the behavior and timestamps 
   of the relevant events are also provided. 
   Recordings last ~15min on average, each including
    200 behavioral trials. I will, also, be using 
    [ofc-2 dataset](http://crcns.org/data-sets/ofc/ofc-2/about-ofc-2) 
    which contains the recordings from the orbitofrontal cortex of three rats during an odor classification task. I will use a similar [dataset ofc-1](http://crcns.org/data-sets/ofc/ofc-1/about-ofc-1) which contains the recordings from the orbitofrontal cortex of five rats during an odor discrimination task.

## What specific work are you going to do?
I will be using PCA and ICA to reduce the dimension of the data. I will research different machine learning models and frameworks, such as deep learning and different types of neural networks, including but not limited to convolutional and recurrent neural networks, in the context of this problem. Mainly, I will be implemented various configurations of these models to train on the given dataset and test their accuracy on a subset of this dataset.

## What do you expect to find and what will you do if you do not find the expected results? (max: 3 sentences)
I expect to find a deep learning model that is able to predict decisions in the majority of cases. This is because deep learning models have been proven to be able to extract patterns in the data that were not previously extractable using other models. If I do fail to find the expected results, I will report my findings and possible reasons for short-comings of the models and try to propose different experimental data or model that could possibly tackle this question.


## TODO
- [ ] find average filter for both convolutional layers for each decision for one subject (subject 3, preferably)
- [ ] find average decision rule for random forest for each decision for one subject (subject 3, preferably)

## Citations
- __OFC-3__<br>
Ignacio Saez, Jack Lin, Arjen Stolk, Edward Chang, Josef Parvizi, Gerwin Schalk, Robert T. Knight, and Ming Hsu (2018); High-frequency activity of human orbitofrontal sites during decision-making play. CRCNS.org<br>
http://dx.doi.org/10.6080/K0VM49GF

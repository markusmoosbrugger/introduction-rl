# Introduction to Reinforcement Learning

Repository for the practical part of Introduction to Reinforcement Learning in the UIBK Data Science Master's programme.

This practical part will cover the following contents:

* Setting up a `gym` environment
* Setting up a RL agent for interacting with the environment
* Learn to navigate within a grid using SARSA and Q-Learning 
* Test and measure the performance of a simple RL agent

## Preparation and Setup

In order to solve the tasks following setup is recommended:
- Python~=3.8
- gym~=0.18.0
- jupyter~=1.0.0
- pandas~=1.2.4
- matplotlib~=3.4.1

### Setting up the virtual environment

This is an optional step to separate your local Python environment from packages required for this lab.
If you don't like to separate your environment you can simply skip this step.

In order to install the `virtualenv` package execute following command:

```
pip install virtualenv
```

The virtual environment can then be created via (make sure that you installed `python3.8`:
```
virtualenv -p python3.8 venv-rl-introduction
```

Now the virtual environment can be activated by using following command:

Mac OS/Linux
```
source venv-rl-introduction/bin/activate
```

Windows
```
venv-rl-introduction\Scripts\activate
```

Your command line prompt should now start with `(venv-rl-introduction)`. 
Any Python commands you use will now work with your virtual environment.

In order to deactivate the virtual environment you can use the command:

```
deactivate
```

### Installing required packages

The required packages are listed in the `requirements.txt` file.
In order to install all packages simply execute (if you like to install it in the virtual environment you need to activate it previously):

```
pip install -r requirements.txt
```


### Run jupyter notebook

If you use the virtual environment approach you need to register the kernel in the jupyter notebook:

```
python -m ipykernel install --user --name=venv-rl-introduction
```

Now you should be able to run `jupyter notebook` via the following command:

```
jupyter notebook
```


This should open your default web browser and you will see the *Notebook Dashboard* which displays the content of your current directory.
Now you should be good to go :)

## Assignment, due June 28<sup>th</sup> 2021


### Exercise 1: Practical part (5 points)
In this exercise we will train a RL agent to navigate inside a grid. The goal is to implement 
two of the most used algorithms for temporal difference (TD) learning, namely SARSA and Q-learning. 
Afterwards, the two approaches are evaluated and compared in order to get an intuition about the 
difference between on-policy and off-policy learning. 
The theoretical part focuses on the comparison between on-policy and off-policy methods as well as on the influence
of the parameters &alpha; and &gamma;.

### Tasks 

1. Implement SARSA and evaluate the learned strategy. Did the agent learn an optimal strategy? (2 points)

2. Implement Q-Learning and evaluate the learned strategy. Did the agent learn an optimal strategy? (2 points)

3. Does the agent learn an optimal strategy if there are 10 or 20 bombs placed on the board
instead of 5? What may be the problems if there are too many bombs on the field? (1 point)

### Exercise 2: Theoretical part (5 points)

### Questions (1 point each)

1. How do the update rules differ between SARSA and Q-Learning? 

2. What is the major difference between on-policy and off-policy algorithms? Why is SARSA considered 
as on-policy and Q-Learning off-policy?

3. Do SARSA and Q-Learning always learn the same policies? Do both of them converge to the optimal policy?

4. How does the learning rate &alpha; and the discount factor &gamma; influence the learning process?

5. Suppose &gamma; = 0.7 and the following sequence of rewards is received: R<sub>1</sub>=-1, 
R<sub>2</sub>=3, R<sub>3</sub>=5 and R<sub>4</sub>=1, with T=4. What are G<sub>0</sub>, G<sub>1</sub>,
..., G<sub>4</sub>?


### Expected submission format

Please hand in a single zip file containing
* Exercise 1
    * Jupyter notebook file (file extension `.ipynb`) with implementation of SARSA, Q-Learning, evaluation and discussion
    * Optional: additional `.pdf` file if you prefer to discuss the results in a separate file
    * Optional: `gym` environment (file extension `.py`) if you have made some changes in the environment 
* Exercise 2
    * Report `.pdf` file containing the answers for the questions


## Feedback & Support
We hope you enjoyed the course and you were able to learn something useful while completing the seminar and the exercises. If you have feedback or encountered any issues,
feel free to contact us at any time. Also, if you have any difficulties in doing the exercises, we are here to help :)

As we would love to improve this course continuously, we would really appreciate if you could provide us some feedback under the following link:  


[Link to Google Form](https://forms.gle/YHJscmbwxTKxz2V1A)

Thanks!

**Contact:**

[Christoph Klösch](mailto:christoph.kloesch@student.uibk.ac.at)

[Markus Moosbrugger](mailto:markus.l.moosbrugger@student.uibk.ac.at)

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
python3.8 -m ipykernel install --user --name=venv-rl-introduction
```

Now you should be able to run `jupyter notebook` via the following command:

```
jupyter notebook
```


This should open your default web browser and you will see the *Notebook Dashboard* which displays the content of your current directory.
Now you should be good to go :)


## Feedback & Support
We hope you enjoyed the course and you were able to learn something useful while completing the seminar and the exercises. If you have feedback or encountered any issues,
feel free to contact us at any time. Also, if you have any difficulties in doing the exercises, we are here to help :)

As we would love to improve this course continuously, we would really appreciate if you could provide us some feedback under the following link:  

[Link to Google Form](https://forms.gle/YHJscmbwxTKxz2V1A)

Thanks!

**Contact:**

[Christoph Klösch](mailto:christoph.kloesch@student.uibk.ac.at)

[Markus Moosbrugger](mailto:markus.l.moosbrugger@student.uibk.ac.at)

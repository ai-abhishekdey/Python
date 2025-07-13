

## Creating virtual environment using anaconda in ubuntu

**Author: Abhishek Dey**

**Date: 13 July 2025

### Download 


* Download anaconda installation script from [here](https://www.anaconda.com/download/)

### Installation 

```

cd <download path>


chmod 777 Anaconda3-2025.06-0-Linux-x86_64.sh


./Anaconda3-2025.06-0-Linux-x86_64.sh 

```

### Follow the prompts

* Accept License

* Choose installation path

* * Type **yes** for below prompt

```
Do you wish to update your shell profile to automatically initialize conda?
This will activate conda on startup and change the command prompt when activated.
If you'd prefer that conda's base environment not be activated on startup,
   run the following command when conda is activated:

conda config --set auto_activate_base false

You can undo this by running `conda init --reverse $SHELL`? [yes|no]
[no] >>>

```
* Then restart your terminal or:

```
source ~/.bashrc

```

This will reload your shell configuration, and since you chose yes during install, it initializes conda and activates the base environment by default.

```
(base) yourname@yourmachine:~$

```

* To get out out of the base environment, type

```
conda deactivate

```


### Create new virtual environment using conda


* Let’s say you want a new environment called **myenv** with Python 3.13

```

conda create -n myenv python=3.10

```

### To activate this environment, use

```

conda activate myenv

```

### To check the packages installed in the virtual env by default

```
pip3 list

```

```
Package    Version
---------- -------
pip        25.1
setuptools 78.1.1
wheel      0.45.1

```

### Install required packages inside virtual environment

* create a **requirements.txt** file and add the python packages

```
numpy
pandas
scipy
scikit-learn
matplotlib
seaborn
streamlit
```

* run the below to install the required packages

```
pip install -r requirements.txt

```

### To Check the installed packages

```
pip3 list

```



### To deactivate an active environment, use

```

conda deactivate

```
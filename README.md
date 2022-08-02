# ML_Regression_restaurant_rating_prediction
The main goal of this project is to perform extensive Exploratory Data Analysis(EDA) on the Zomato Dataset and build an appropriate Machine Learning Model that will help various Zomato Restaurants to predict their respective Ratings based on certain features.

#### Info about software and account requirement for project, essential directory and files neccessary for project, important git and docker command and basic CI/CD pipeline .

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs)

## Environment setup

Check conda is working in terminal or not by typing:
```
conda --version
```
>Note: If conda not working you have to setup Environment Variable in your pc/laptop.
[How to setup Environment Variable](https://www.youtube.com/watch?v=3qOK8WCnT3g)

Create conda virtual environment:
```
conda create -p venv python==3.7 -y
```
To activate newly created virtual environment 
```
conda activate venv/
```
If shell is selected or any error related to init then:
```
conda init --h
```
```
conda init <SHELL_NAME>
```
>eg. conda init bash  OR conda init cmd.exe

## Git Commands(Frequently Used)

To look status of changes/commit/untracked in the file:
```
git status
```

To Add files to git
```
git add .
```
>Don't forget the dot(.) after add in git add
OR
```
git add <file_name1 file_name2 file_name3 ..... file_namen>
```
>Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url
```
git remote -v
```
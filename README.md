
# Year of Challenges 2017

Hello and welcome to the Year of Programming 2017's challenges repository! Here
we will be posting ~~daily~~ periodic challenges for the community to complete.

## Table of Contents
    
1. [The Administration Team](#the-administration-team)
2. [Challenges](#challenges)
3. [Solutions](#solutions)
4. [Submitting Your Work](#submitting-your-work)
5. [Getting Set Up](#getting-set-up)
    1. [Verify Git Installation](#1-verify-git-installation)
    2. [Fork the 2017Challenges Repository](#2-fork-the-2017challenges-repository)
    3. [Clone Your Fork](#3-clone-your-fork)
    4. [Git Configuration](#4-git-configuration)
    5. [Proceeding With A Challenge](#5-proceeding-with-a-chaellenge)
    6. [Submitting Your Code](#6-submitting-your-code)
    7. [Acquiring New Challenges](#7-acquiring-new-challenges)

## The Administration Team
- [myrrlyn](https://github.com/myrrlyn "myrrlyn")
- [jremillard](https://github.com/jarydremillard "jaryd remillard")
- [sten](https://github.com/dashsten "dashten")
- [manuel](https://github.com/ManuelMeraz "ManuelMeraz")
- [marcus](https://github.com/MJUIUC "MJUIUC")
- [ae1vtas](https://github.com/aev1tas "aev1tas")
- [aakash](https://github.com/asethi77 "asethi77")

## Challenges

Each challenge will be posted in its own folder, in numbered order. Each
challenge folder will have a Challenge.md file describing the challenge, and may
have some example code or data provided.

## Solutions

To participate, simply [fork](https://help.github.com/articles/fork-a-repo/) the repository and then make a folder for your
solution, inside the challenge you are solving.

If I am solving the zeroth challenge in Rust, I would work in the folder
`challenge_0/rust/myrrlyn`, to organize solutions by their language and
then their author. This allows us to easily browse solutions by language, and
compare work!

## Submitting Your Work

To submit, open a [pull request](https://help.github.com/articles/about-pull-requests/) on the main repository. We'll make sure that merging won't cause any problems, and go from there.

Note: Your solution will not be instantly accepted onto repository. We will be reviewing your code, file formatting and directory structure of your code. If you satisfy the requirements, then we will accept and merge. 

## Getting Set Up

If you do not have git [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), please do that first.

Note: If you have never used the command line a `$` before some text denotes a command and a line following that without the `$` denotes the output of that command.

#### 1. Verify Git Installation

To confirm that you have git installed type in:
```
$ git --version
git version 1.9.1
```
It should respond by showing you the version of git you have installed.


#### 2. [Fork](https://help.github.com/articles/fork-a-repo/) The 2017Challenges Repository


Click on the button on the top that says fork.

**Image 1 here**

You will now have a copy of the 2017Challenges repository in your profile.


#### 3. [Clone](https://help.github.com/articles/cloning-a-repository/) Your Fork


Click on the green dropdown button titled "Clone or download" and copy the URL there.

Note: I recommend cloning as [SSH](https://help.github.com/articles/generating-an-ssh-key/) as it will allow you to use git without constant user authentication. If you are not comfortable with this yet, proceed with HTTPS.

**Image 2 here**

Open up your command line tool and enter:

Note: Enter the following without the following without the angled brackets (i.e. `git clone git@github.com:ManuelMeraz/2017Challenges.git`)

```
$ cd ~
$ git clone <URL that you copied here>
Cloning into '2017Challenges'...
remote: Counting objects: 874, done.
remote: Compressing objects: 100% (13/13), done.
remote: Total 874 (delta 4), reused 0 (delta 0), pack-reused 860
Receiving objects: 100% (874/874), 95.41 KiB | 0 bytes/s, done.
Resolving deltas: 100% (324/324), done.
Checking connectivity... done.
```


#### 4. Git Configuration


Next we will be [configuring](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) your git setup. 


Note: Simply replace the text inside the quotation marks with your name and email.

```
$ cd ~/2017Challenges/
$ git config --global push.default simple
$ git config --global user.name "John Doe"
$ git config --global user.email "your_email@example.com"
$ git remote add challenges https://github.com/YearOfProgramming/2017Challenges.git
```


#### 5. Proceeding With A Challenge


The challenges will be structured in the following format
```
/                                     -> root directory

README.md                             -> Contains the information in this help page
challenge_0/                          -> challenge_<number>

            README.md                 -> File containing challenge prompt
            r/                        -> lowercase directory with your preferred language. 
            php/                      -> If it does not exist, then create one. 
            python/
            cpp/
            csharp/
            .../
                    /john             -> your username in slack
                    /nick
                    /nancy
                    .../
                    
                           README.md  -> Documentation for your program. Be creative!
                           src/       -> contains your source code
```
  
Assuming that you are in the root of the directory you will look for the challenge you want to complete.

`/challenge_#/`

Move into the directory for the challenge you want to complete and see if a directory already exists for your preferred programming language.

If it exists, move into that directory. Otherwise, make a new directory for your language.

Note: The format for directory naming for programming languages is all lowercase plain text with no special characters(i.e. csharp).

`/challenge_#/language/`

Once inside your preferred programming language directory you will create a directory with your slackusername or name you want to be identified by for your work.

`/challenge_#/language/name/`

###### Documentation For Your Program and Source Code

Inside this directory you will have 2 items:
* A file named 'README.md' and inside you will document how your program works.
* Your source code, preferably in a directory titled 'src'

Note: When you are documenting your program, pretend you are someone who has never seen that programming language and instruct them on the steps to run your program and how to use it

Your set up should be as follows so far:
```
/challenge_#/language/name/README.md
/challenge_#/language/name/src/file_1
/challenge_#/language/name/src/file_2
/challenge_#/language/name/src/...
```

#### 6. Submitting Your Code

Assuming you are in the directory under your name you will enter the following
```
$ git add ./*
$ git commit -m "challenge_# in language"
$ git pull challenges master
$ git push origin master
```

Note: Replace the text inside the quotations with the relevant information.

If you go to the page where your forked repository is contained your updated code should be there. 

Click on the "New pull request" button button to submit your work for review.

**Image 3 here**


#### 7. Acquiring New Challenges

To get a new challenge that has just been posted you open your command line and enter
```
$ git pull challenges master
```

This will download the newest solutions and challenges to your computer



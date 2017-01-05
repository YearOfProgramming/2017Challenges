
# Year of Challenges 2017

Hello and welcome to the Year of Programming 2017's challenges repository! Here
we will be posting ~~daily~~ periodic challenges for the community to complete.

## Table of Contents
    
1. [The administration team](#the-administration-team)
2. [About Year of Programming](#about-year-of-programming)
3. [Challenges](#challenges)
4. [Solutions](#solutions)
5. [Submitting your work](#submitting-your-work)
6. [Getting set up](#getting-set-up)
    1. [Verify git installation](#1-verify-your-git-installation)
    2. [Fork the 2017Challenges repository](#2-fork-the-2017challenges-repository)
    3. [Clone your fork](#3-clone-your-fork)
    4. [Git configuration](#4-git-configuration)
    5. [Proceeding with a challenge](#5-proceeding-with-a-challenge)
    6. [Submitting your code](#6-submitting-your-code)
    7. [Acquiring new challenges](#7-acquiring-new-challenges)
7. [Workflow](#workflow) 

## The Administration Team
- [myrrlyn](https://github.com/myrrlyn "myrrlyn")
- [jremillard](https://github.com/jarydremillard "jaryd remillard")
- [sten](https://github.com/dashsten "dashten")
- [manuel](https://github.com/ManuelMeraz "ManuelMeraz")
- [marcus](https://github.com/MJUIUC "MJUIUC")
- [ae1vtas](https://github.com/aev1tas "aev1tas")
- [aakash](https://github.com/asethi77 "asethi77")

## About Year of Programming

A common source of frustration among budding developers is acquiring the experience necessary to move past the early stages of programming and computer science. _Year of Programming_ is an active community of dedicated participants that encourage each other to acquire daily experience in problem solving, programming and computer science through collaboration. 

## How does this work?

Periodically we will be releasing a new programming challenge by pushing it to our Github repository targeted at a wide audience. 

As a participant, you will solve this challenge with the programming language of your choice and document the thought process behind solving this problem, explain how to compile your code and how to use your program. 

You will then submit your code for review and your peers will review your code and give you feedback. Once enough people have reviewed and approved of your solution, we will merge your code onto the repository and the solution will be stored there for that challenge. 

Most of our communication is done through our [slack](https://yearofprogramming.signup.team/) chat room. Through this chat room you can collaborate with others to help solve these challenges or anything you feel like discussing. 

This will develop key skills required for problem solving and development for new developers such as:
* Solving problems through programming
* Technical writing
* Clean and readable code 
* Code reviewing and giving feedback
* Version control using Git
* Communication skills through collaboration

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

## Submitting your work

To submit, open a [pull request](https://help.github.com/articles/about-pull-requests/) on the main repository. We'll make sure that merging won't cause any problems, and go from there.

When submitting a pull request please use the following format for your title:
```
[Language] Challenge #
```

*Note: Your solution will not be instantly accepted onto repository. We will be reviewing your code, file formatting and directory structure of your code. If you satisfy the requirements, then we will accept and merge.*

## Getting set up

If you do not have git [installed](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git), please do that first.

*Note: If you have never used the command line a `$` before some text denotes a command and a line following that without the `$` denotes the output of that command.*

#### 1. Verify your Git installation

To confirm that you have git installed type in:
```
$ git --version
git version 1.9.1
```
It should respond by showing you the version of git you have installed.


#### 2. [Fork](https://help.github.com/articles/fork-a-repo/) The 2017Challenges Repository


Click on the button on the top that says fork.

![1](https://github.com/YearOfProgramming/storage/blob/master/images/1.png?raw=true)

You will now have a copy of the 2017Challenges repository in your profile.


#### 3. [Clone](https://help.github.com/articles/cloning-a-repository/) your fork


Click on the green dropdown button titled "Clone or download" and copy the URL there.

*Note: I recommend cloning as [SSH](https://help.github.com/articles/generating-an-ssh-key/) as it will allow you to use git without constant user authentication. If you are not comfortable with this yet, proceed with HTTPS.*

![2](https://github.com/YearOfProgramming/storage/blob/master/images/2.png?raw=true)

Open up your command line tool and enter:

*Note: Enter the following without the following without the angled brackets (i.e. `git clone git@github.com:ManuelMeraz/2017Challenges.git`)*

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


#### 4. Git configuration


Next we will be [configuring](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) your git setup. 


*Note: Simply replace the text inside the quotation marks with your name and email.*

```
$ cd ~/2017Challenges/
$ git config --global push.default simple
$ git config --global user.name "John Doe"
$ git config --global user.email "your_email@example.com"
$ git remote add challenges https://github.com/YearOfProgramming/2017Challenges.git
```


#### 5. Proceeding with a challenge


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

`/challenge_#/language/`

*Note: The format for directory naming for programming languages is all lowercase plain text with no special characters(i.e. csharp).*

Once inside your preferred programming language directory you will create a directory with your slackusername or name you want to be identified by for your work.

`/challenge_#/language/name/`

###### Documentation for your program and source Code

Inside this directory you will have 2 items:
* A file named 'README.md' and inside you will document how your program works.
* Your source code, preferably in a directory titled 'src'

*Note: When you are documenting your program, pretend you are someone who has never seen that programming language and instruct them on the steps to run your program and how to use it. [Here](https://gist.github.com/anonymous/52b08845673ef9c86c12e94d95f412b5) is a working template and [here](https://gist.github.com/anonymous/d89ec2a00976b2d42f90990ee3796972) is an example.*

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
$ git commit -m "[Language] Challenge #"
$ git pull challenges master
$ git push origin master
```

*Note: Replace the text inside the quotations with the relevant information.*

If you go to the page where your forked repository is contained your updated code should be there. 

Click on the "New pull request" button to submit your work for review. Be sure to include the challenge number and language of your solution!

![3](https://raw.githubusercontent.com/YearOfProgramming/storage/master/images/3.png)


#### 7. Acquiring New Challenges

To get a new challenge that has just been posted you open your command line and enter
```
$ git pull challenges master
```

This will download the newest solutions and challenges to your computer

## Workflow

When a challenge is released we will notify everyone in the Slack chatroom. If you have the app installed on your phone, you will receive a notification. 

To acquire the new challenge open up your command line tool move to the 2017Challenges directory and enter the following command

```
$ cd ~/2017Challenges/
$ git pull challenges master
```
*Note: Your text editor might open up to commit a merge. You can simply close it and continue.*

If you type in the command
```
$ ls
challenge_0  challenge_1  challenge_2  challenge_3  challenge_4  challenge_5  LICENSE.txt  README.md  Unittesting.md
```
You should have something like the output here.

Move into the chalenge directory you want to complete and follow the same process as before for completing a challenge. Make sure to follow the [documentation](#documentation-for-your-program-and-source-code) guidelines and [formatting](#5-proceeding-with-a-challenge) guidelines. 

After you have pushed your code to your forked repository as follows
```
$ git push origin master
```

Then you can submit a pull request. 

![workflow](https://raw.githubusercontent.com/YearOfProgramming/storage/master/images/github_flow.png)

**All credit goes to [@selectivealso](https://github.com/SelectiveAlso) from our slack chat for this awesome image!**

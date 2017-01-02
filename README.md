# Year of Challenges 2017

Hello and welcome to the Year of Programming 2017's challenges repository! Here
we will be posting ~~daily~~ periodic challenges for the community to complete.

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


### 1. Now that you have git installed please open up the command line tool for you operating system.


To confirm that you have git installed type in:
```
$ git --version
git version 1.9.1
```
It should respond by showing you the version of git you have installed.


### 2. [Fork](https://help.github.com/articles/fork-a-repo/) the 2017Challenges repository.


Click on the button on the top that says fork.

**Image 1 here**

You will now have a copy of the 2017Challenges repository in your profile.


### 3. [Clone](https://help.github.com/articles/cloning-a-repository/) your fork of the 2017Challenges repository onto your computer.


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


### 4. Git Configuration


Next we will be [configuring](https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup) your git setup. 


Note: Simply replace the text inside the quotation marks with your name and email.

```
$ cd ~/2017Challenges/
$ git config --global push.default simple
$ git config --global user.name "John Doe"
$ git config --global user.email "your_email@example.com"
$ git remote add challenges https://github.com/YearOfProgramming/2017Challenges.git
```


### 5. Proceeding with a challenge


The challenges will be structured in the following format
```
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
  
To be continued...

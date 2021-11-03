# This is a Tutorial made by Haolai Che on 11/02/2021
# This is about What is git Pull and How to use Git pull

# 1. What is git pull?
    Gitpull is used to fetch and merge changes from remote repo to local repo
    Gitpull is combined with two commands: Git fetch followed by Git merge

# 2.How to use gitpull, make changes and push it back
    pwd # Know where I am 
    mkdir abc # making a directory
    cd abc 
    mkdir changes
    cd changes
    # Now we are in this local directory and we want to make "changes" our local repo
    
    git init
    
    <img width="560" alt="截屏2021-11-02 21 56 27" src="https://user-images.githubusercontent.com/22487666/140000211-d8d5e78f-fae5-4b0f-a8f4-b57f4fcb4683.png">
    
    git pull git@github.com:CCM81/csds_438_project.git #This is just an example , in reality you can use any ssh-keys
    
# 3.Now we have pulled the project from remote repo to Local repo, we can make some changes and push it back
    #First we make some changes
    
    git status
    
    git add . 
    
    git commit -m "changes made"    # I think -m is for message
    
    git remote add origin git@github.com:CCM81/csds_438_project.git
    
    git remote -v
    
    git push -u origin master
    # master is the branch, the default is main
    
# Now The push is done, we have pulled, and committed changes, and then pushed it back. Hooray !! 😄 
    




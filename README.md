## Common git Commands

### To view the current status of your branch
git status

### To see any discrepancies between your local branch the remote
git fetch

### Once fetched, you can merge these changes into your local branch
git merge

### To both fetch and merge in one go, use 
#### Mr. T's preference
git pull

### To create a new branch, based off of another one
git checkout -b {new branch name} {branch to base off of}

### To add any changes made
#### the -A will stage all, or your can specify one file name at a time
git add -A

### To remove a staged file:
git restore --staged {file}

### To commit changes
#### saving to local git repo
git commit -m "Your commit message goes here"

### To save changes to remote repo
#### origin
git push origin {branch name}

### To view a log of all commits on a branch
git log --graph --pretty=one-line --abbrev-commit

### To roll back to a previous local commit
#### where N = 1 is the previous commit, N = 2 is the commit before that, and so on...
git reset --soft HEAD~N

### To overwrite your local branch with the remote version of it
git reset --hard origin/{branch name}

### To sqaure commits into one or more
#### for previous N commits
git rebase --interactive HEAD~N

then use pick and squash in the terminal editor to specify which commits to keep and which to squash
then update your commit message

### To rebase off of another branch
#### useful when trying to merge into master
#### first rebase your branch off of master, then submit your PR
git pull --rebase origin {remote branch name}

### To delete a local branch
#### capital D may be required
git branch -d {local branch name}

### To delete a remote branch
git push origin --delete {remote branch name}

### Force push
#### will be required if you squashed after pushing
git push origin {branch name} --force
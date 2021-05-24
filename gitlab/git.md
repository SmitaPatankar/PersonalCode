#### Tools
- linux putty
- windows command prompt 
- windows gitbash

#### SSH Auth Setup  
```
ssh-keygen    
enter -> enter -> enter    
~/.ssh$ cat id_rsa.pub -> store it on gitlab UI  
git config --global user.name "username"    
git config --global user.email "email address"    
```

#### Clone repository
```
git clone (urlofrepofromweb)
```

#### Checkout a branch
```
git checkout (branchnamefrorepofrommweb)
```
Make some changes.

#### List changes
```
git status
```

#### See changes in detail
```
git diff
```

#### Stage changes
```
git add (filename or . for all)
```

#### See staged changes in detail
```
git diff --staged
```

#### Commit changes
```
git commit -m "message"
```

#### Push changes
```
git push -u origin
```

#### Revert unstaged changes
```
git checkout -- (filename)
```

#### When your branch gets behind master branch  
```
git checkout master  
git pull origin master  
git checkout (yourbranch)   
git merge master  
git push origin (yourbranch)  
```
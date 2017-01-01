#Jumble words solver using Python and webapp2
![Anargam](/img.png "Screenshot") 

###[Live Demo](https://anargampy.appspot.com)
###[Doc](http://indrajith.me/jumble_words_solver_in_python/)

###is_anargam:
```python
def is_anargam(word1, word2):
    """Returns True if anargam is found. Else return False."""
    count = 0
    word1, word2 = list(word1), list(word2)  #get a list of charectors in the words
    if len(word1) == len(word2):             #match the dictionary word only if same length
          for i in word1:                    #removes a letter from the word and increase count
                   if i in word2:
                    word2.remove(i)
                    count += 1
          if count == len(word1):           #if count == lenght then its a match
               return True
    return False

```
###anargam_find:
```python
def anargamFind(wd_in):
    file = open('words.txt')              #open dictionary 
    wd_in=wd_in.lower();                  #make input string to lower case
    tmpString = ""                        #string of matched words
    found = 0
    for line in file:                     #loop through the dictionay
     if is_anargam(wd_in,line.strip()):
        found += 1
        tmpString += line.strip() + ", " 
    return tmpString, found

```
###run locally
Requrements: Python 2.7.10, google-cloud-sdk 
`git clone https://github.com/indrajithi/Jumble-words-Solver-using-webapp2`
`cd Jumble-words-Solver-using-webapp2/`
`dev_appserver .`
If everything goes smooth the server will be up and running at `http://localhost:8080/`
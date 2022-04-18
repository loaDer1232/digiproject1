# digiproject1
eotc database
Hi  
this project is desigend to allow teacher to keep track of students on a eotc camp.  
# bugs
one of the majoir bugs that the program currently has is when a user shurches by day the program returns several copies of each window 
![imag](readmedata/suerachbydaybug.PNG)
this is because of the the code surches though the data it does this by itarating tough the values of the array for each key so it returns mulatple times   
         ```Check = sherchbox.get()  
              for i in data:  
                 for e in i.values():  
                     if Check in e:  
                         info = i  
                         sherchoutput(info)```  
as you can see in the code sample above this wont be to hard to fix   

# imporvments
there are sevral improvemts i am going to make to this program 
1. fix the dropdown menu in sherach 
![img](readmedata/dropdownprob.PNG) 
2. let users shearch by more values
3. fix the code i was perviosly using to make a bad version of a database (was removed due to causeing the program to crash unexpectly)

# testing
to be done

# planing 
here is some proof of planing
![flow](readmedata/flow.png)


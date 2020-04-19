# 419C-Final-Project

% 419Cproject.py 
    
    Main of the code, In here you can customize youre queries, number of users and jobs to query
    and location of the data files

% finaccountURLS.py

    Searches google with the query and scrapes the URLS.
    
% findjobs.py

    Searches LinkedIn for jobs based on a query and location.
    
% scrapeuserskills.py
    
    opens each URL in the selected URL json file and scrapes the user skills from each profile.
     
% Allthejob.py

    helper used to congregate multiple jsons of jobs into a single file.

% compare.py

    Compares users to each job individually and prints the 3 most similar jobs for that user.

% compilejobs.py

      takes the raw job descriptions and process's it removing stopwords and porterstemming.
      
% compileusers.py

    proccess's the users skills, finding the most popular.  It also creates a master list of all 
    porterstemmed and stopword removed skills.
    
% parsjobskills

    creates a dictionary that holds the job name as a key to a list of its skills

% findaccountUrlsV2  
    
    Attempt at using github to search for people.  This didnt work as you can see people directly
    on github unless you are conntected.  UNUSED
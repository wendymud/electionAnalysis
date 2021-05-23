# Election Analysis Project Overview:
A Colorado Board of Elections employee requested an election audit to obtain data taken from the entire voting pool in a recent congressional election.  With the task at hand, the plan was to conduction calculations to determine the names of the candidates in the election, the percentage of votes each candidate obtained, the percentages of votes and of course the winner of the election, as well as determine the largest county turnout.  Here is the request of data to be extracted:

1 Calculate the total number of votes cast
2 List the counties that voted in this election
3 Calculate the percentages of votes per county and votes cast per county
4 List the largest county turnout
5 List the names of all candidates
6 Calculate the total number of votes for each candidate
7 Calculate the percentage of total votes for each candidate
8 List the winner of the election

## Resources 
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.562

## Election Audit Results
The extraction of the election data has provided results to depict a total of 369,711 votes cast during this election with the largest voter turnout from Denver county at 82.8% or 306,055 votes.  In addition Jefferson county was second with 10.5% voter turnout at 38,855 voters and third was Arapahoe county at 6.7% and 24,801 voters.
In terms of the vote selection from those counties, the overwhelming winner of the election is Diana DeGette at 73.8% or 272,892 of the winning votes.  Next was Charles Casper Stockham at 23% or 85,213 votes.  The third candidate, Ramon Anthony Doane at 3.1% or 11,606 of the votes.


![ElectionAnalysisTerminalOutput](https://user-images.githubusercontent.com/82694423/119248147-15a16100-bb44-11eb-96f2-c5500b60895f.PNG)



## Election-Audit Summary
The Python code that was created specifically for this project may be utilized in further elections to depict the same information or repurposed and customized to add additional analysis.  This was a relatively small pool of votes a bit under 400k, so the results could be provided in less that one minute.  If the data pool is substantially larger, in the millions, for example, then the time to obtain the answer will take a bit more time.  However, this program could easily be utilized as is, or modified to obtain results from any election.  Also, if there were additional candidates, the program in this code contains the appropriate variables to ensure all candidate names are displayed appropriately with their total vote counts and percentages.

Similarly, click here to view the textfile output of the election audit: [election_analysis.txt](https://github.com/wendymud/electionAnalysis/files/6527526/election_analysis.txt)


## Challenge Overview
Compared to Visual Basic for Applications (VBA), Python seems to be a bit easier and a lot less clunky to utilize.  Python seems more streamlined and user friendly to put together.  Saying that, it was nice that VBA was much more forgiving in that the capital letters and indenting didn't matter.  With Python, it really matters on how far indented the code is placed within the program.  I learned that the hard way as I encountered an error and took a bit of time trying to figure out why my code was typed out exactly as suggested in the module, however it wasn't working.  I came to find out that the indent wasn't following the right loop!  I took out a tabbed indent and voila!  I love that I'm starting to get a better sense of how I may provide code through different interpreters, utilizing different sytles, and thinking through challenging problems.  As I've stated to my tutor, the more I do this the better I become.  Through this course I'm discovering that I may be a closet software engineer, as I'm really starting to enjoy this coding bit.

## Challenge Summary
This week's challenge summary was practical and not too difficult to understand.  I enjoyed pulling the nuggets out of the supplied dataset and creating the data to provide the analysis.  I believe this exercise is a very meaningful and useful way of obtaining a comprehensive data summary for any election as well as any company.  I appreciated the real-life scenarios that the module depicted.  It's quite helpful to assign these types of real-life tasks as I try to understand, churn and, in turn, display valuable information to meet the demands of the week.


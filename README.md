# Election_Analysis

## Project Overview
In this election audit analysis, Colorado Board of Elections employee Tom and his manager Seth were looking for a few things; they wanted to automate the collection of data on not only the candidates and the winner amongst them, but also the counties that voted for them. Tom and I wrote a Python script gathering data from mail-in ballots, punch cards, and direct recording electronic counting. Their end goal was for us to collect enough data to determine the overall candidate winner as well as the county with the largest voter turnout. They also wanted us to report the individual data for each candidate and county:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who recieved votes.
3. Calculate the total number of votes each candidate recieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: [election_results.csv](https://github.com/TMWRose/Election_Analysis/files/8447743/election_results.csv)
- Software: Python 3.10, Visual Studio Code, 1.38.1

## Results
![txt file scrren shot](https://user-images.githubusercontent.com/100237685/163077188-47b7dfa5-1904-46ff-8c57-3fc426cd1bb6.png)

The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham recieved 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette recieved 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane recieved 3.1% of the vote and 11,606 votes.
- The winner of the election was:
    -Diana DeGette, who recieved 73.8% of the vote with 272,892 number of votes.
- The county vote break down:
    - Jefferson County votes comprised 10.5% of total election votes, or 38,855 voters.
    - Denver County votes comprised 82.8% of total election votes, or 306,055 voters.
    - Arapahoe County votes comprised 6.7% of total election votes, or 24,801 voters.
- Denver County had the largest number of votes

## Challenge Summary
I reccomend that the Election Commission utilizes the Python script that Tom and I wrote to automate the vote count given the following modifications are added: 

1. A section of code is added to track the demographics of the voters, such as: gender identity, race, age, and party affilition. This would help candidates gain a better understanding of the demographics they appeal to best.
2. The vote count results within the code should be converted to touples (once the votes are counted) to prevent any election fraud should either party attempt to hack and modify the code.
3. A section of code should be added to scan voter id's to ensure there are not multiple votes from an individual voter.  
4. A few sections of code should be added to send the voting results (once verified) to the candidates, relevant news outlets, and any government websites where the voting results would normally be published. 

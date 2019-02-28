# Writeup 3 - Operational Security and Social Engineering

Name: Rami Halboni
Section: 101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Rami Halboni

## Assignment Writeup

### Part 1 (40 pts)

The easiest way to get all the information prompted for using social engineering is to use a phishing scam where you email Elizabeth saying her ATM PIN numbmer has been compromised, and she needs to change it by clicking on this link. once she goes to the link, you can easily run a quick script to see what browser she is using, and people normally dont use more than one browser so the browser she is using is most likely the one she primarily uses. to make it believable it has to look just like her bank website so you make sure you copied the site. then you ask her to login. Then you prompt her with security 3 security questions, What's her mother's maiden name?, What city was she born in?, What was the name of her first pet?. once she answers the question the final step is to get her pin, to do this you prompt to enter her old pin, and then her new pin, along with a confirmation. Another form is to email Elizabeth asking her to call a number, where she calls you, and you go through the same process, just over the phone. The only hard part would be to figure out what internet browser she primarily uses since that is normally not a security question you normally use. 

### Part 2 (60 pts)

Hello Elizabet thank you for reaching out, I will be more than happy to help out. the three main issues I found is:

1. Your password is not secure at all, I did a dictionary attack on your server and easily found out linkinpark was your password, When I tested linkinpark to see how good of a password it was, it was not secure at all. An easy fix to this is to use websites that can rate how secure your password is, and keep making up passwords until one is secure. another way is to use a secure password generator. It may not be ideal since it will be hard to remember, but it will keep you safe from getting hacked.

2. You have a port that has been left open, which is how I hacked into your server. You should never leave pors open for no reason, to check if you have any extra ports open use a nmap scan to see what ports are open on your sever.

3. Dont use the same username for every account you have. I guessed that v0idcache was your username to the server because it was your twitter handle, and alias in pastebin. this made my dictionary attack a lot quicker/easier. because i was only testing for one thing.

OSINT (Open Source Intelligence)
======

## Assignment details

This assignment has two parts. It is due by Friday, February 22 at 11:59 PM.

To submit your homework, please follow the guidelines posted under the grading section of the syllabus.

**There will be a late penalty of 5% off per day late! Submissions received more than 3 days late will receive a 0!**

### Part 1

In class you were given an online usertag: `v0idcache`

NOTE: "briefly describe" = 2-3 sentences (and/or include screenshot(s))

Use OSINT techniques to learn as much as you can about `v0idcache` and answer the following questions:

1. What is `v0idcache`'s real name?
Elizabeth Moffet is the real name of v0idcache, she has a twitter account under that alias.

2. Where does `v0idcache` work? What is the URL to their website?
Elizabeth works at Elite Banking, and the website is 1337bank.money

3. List all personal information (including social media accounts, contacts, etc) you can find about `v0idcache`. For each, briefly detail how you discovered them.
-she is located in the Netherlands, twitter geotag
-she is interested in digital financing, google translated one of her tweets
- seems to enjoy Chop Suey, read another tweet
- she follows the UMD cybersecurity club
- she is a CEO, shown in bio
- user @CacheDev0id likes Elizabeth, he replied to one of her tweets asking her if she wants a relationship on 

4. List any ( >= 1 ) IP addresses associated with the website. For each, detail the location of the server, any history in DNS, and how you discovered this information.
- 142.93.136.81,Canada, Host Server, found using Domain Dumpster
- 216.87.155.33, US, DNS Server, found using Domain Dumpster

5. List any hidden files or directories you found on this website. For full credit, list *two* distinct flags.
- v=spfi include:spf.efwd.registrar-servers.com ~all found with domain dumpster
-
- /secret_directory, found by robots.txt
- User-agent: *, found by robots.txt
6. What ports are open on the website? What services are running behind these ports? How did you discover this?
FTP(21), SMTP(25), HTTP(80), POP3(110), IMAP(143), HTTPS(443), 1337(waste) I used Domain Dossier and ran a service scan.

<<<<<<< HEAD
7. Which operating system is running on the website? How did you discover this?
using shodan i enterered ub tge Host IP address and found that the OS running the site is Ubuntu
=======
7. Which operating system is running on the server that is hosting the website? How did you discover this?
>>>>>>> upstream/master

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}, A4300.txt, pastebin
CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5), found with domain dumpster
CMSC389R-{h1ding_fil3s_in_r0bots_L0L}, secret_directory using robots.txt
CMSC389R-{h1dd3n_1n_plain_5ight}, inspected html
CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}, reddit
### Part 2
when I found flag.txt, I ran cat flag.txt and got:
	Good work! Here's a flag: CMSC389R-{brut3_f0rce_m4ster}
### Format
In the "week/2/writeup" directory of our repository there is a README.md file for you to edit and submit your homework in. Use this as a template and directly edit it with your answers. Complete your bruteforce program in this directory as well. When you've finished the assignment, push it up to your personal GitHub for us to grade.

Your responses to every prompt in this assignment should include answers to any specific questions along with a brief explanation of your thought process and how you obtained the answer.

### Scoring

Part 1 is worth 45 points, and part 2 is worth 55 points.

### Tips

Reference the slides from lecture 2 to help you effectively utilize available OSINT techniques.

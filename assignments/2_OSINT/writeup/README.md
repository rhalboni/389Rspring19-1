# Writeup 2 - OSINT

Name: Rami Halboni
Section: 101

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examniation.

Digital acknowledgement: Rami Halboni

### Part 1
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
After running nmap I found these open ports:
SSH(22), HTTP(80),1337(waste) 

7. Which operating system is running on the website? How did you discover this?
using shodan i enterered ub tge Host IP address and found that the OS running the site is Ubuntu

8. **BONUS:** Did you find any other flags on your OSINT mission? (Up to 9 pts!)
CMSC389R-{YWX4H3d3Bz6dx9lG32Odv0JZh}, A4300.txt, pastebin
CMSC389R-{h0w_2_iNt0_DNS_r3c0Rd5), found with domain dumpster
CMSC389R-{h1ding_fil3s_in_r0bots_L0L}, secret_directory using robots.txt
CMSC389R-{h1dd3n_1n_plain_5ight}, inspected html
CMSC389R-{0M3G4LUL_G3T_pWN3d_N00b}, reddit
### Part 2
when I found flag.txt, I ran cat flag.txt and got:
	Good work! Here's a flag: CMSC389R-{brut3_f0rce_m4ster}

*After connecting to the host server I noticed that for any incorrect combination of username and password it would automatically disconnect. And I know v0idcache is very likely to be the username to the server. With this information I looped through all the possible passwords in rockyou.txt hoping that one would be the correct password. What I would do in every iteration is login, enter the username, and enter the password, at the line im reading, if it is incorrect I would read the next line, and retry over and over again. Once the username and password are correct I get access to server, and now I have full control of the server through the python code *

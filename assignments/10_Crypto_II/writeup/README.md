# Crypto II Writeup

Name: Rami Halboni
Section: 

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Rami Halboni

## Assignment Writeup

### Part 1 (70 Pts)
CMSC389R-{m3ss@g3_!n_A_b0ttl3}
### Part 2 gp(30 Pts)
1. I noticed that the ecb encryption still kind of shows the original picture, where thre cbc encryption covers the whole picture, and you cant tell what it is.
2. ECB encryption is definitely less secure, and it is because it encrypts identical plain text boxes to the same thing. CBC does not have the same problem since it takes in the previous encyrped block to and XORs it with the current plaintext box before it encypts it.

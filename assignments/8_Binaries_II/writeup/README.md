# Extra Credit Writeup - Binaries II

Name: Rami Halboni
Section: *PUT YOUR SECTION NUMBER HERE*

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Rami Halboni

## Assignment Writeup

### Part 1 (100 Pts)
Flag: CMSC389R-{0n3_st0p_l0cK_sh0P}

To find the flag in this code in the executable, I started off using IDA pro, however when I got down to a certain part I was not totally able to understand the assembly code, so I used ghdira, which helped by basically converting the whole assemly function to C code. Once it was in C code it was fairly easy to understand what the Flag was, because it was comparing char by char. using a hex to ascii, and a hex calculator I was able to do all the math and conversions that were needed since the whole code was not written comparing to a specific char, sometimes it was offset from the one before and so on.

file:///root/389Rspring19-1/assignments/8_Binaries_II/writeup/cs_hw.PNG


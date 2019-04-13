#include <stdlib.h>
#include <stdio.h>

int main()
{
	unsigned int a = 0x1ceb00da;
	unsigned int b = 0xfeedface;
	printf("a= %d\n", a);
	printf("b= %d\n", b);
	a = a ^ b;
	b = b ^ a; 
	a = a ^ b;
	printf("a= %d\n", a);
	printf("b= %d\n", b);
	return 0;
}

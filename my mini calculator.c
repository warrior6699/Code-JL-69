#include <stdio.h>
int main()
{

int a,b,c,d,x,y,operator;

printf("hello there!\t i'm a mini calculator designed to perform all your calculations for you\n what operation do you want to carry out ??\n");

printf("(availabe choices:\n1.addition\n2.multiplication\n3.division\n4.substraction\n5.square of a number)\n6.root of a number\n");

scanf("%d%%d%d%d",&operator);

printf("enter values for calculation\n");
scanf("%d%d",&x,&y);

if (operator<2)
printf("answer for %d+%d=%d",x,y,x+y);

else if (operator<3)
printf("answer for %dx%d=%d",x,y,x*y);

else if (operator<4)
printf("answer for %d/%d=%d",x,y,x/y);

else if (operator<5)
printf("answer for %d-%d=%d",x,y,x-y);

else if (operator<6)
printf("square of %d is %d",x,x*x);

else if (operator<7)
printf("operation coming soon");

// a mini calculator powered by AT7 THE WARRIOR VX
return 0;

}
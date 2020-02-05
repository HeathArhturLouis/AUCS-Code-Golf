with open('f.c','w') as f:
 d=[{">":"++p","<":"--p","+":"++*p","-":"--*p",".":"putchar(*p)",",":"*p=getchar()","[":"while(*p){","]":"}"}[c] for c in N]
 f.write('int a[9<<20]={0};char*p=a+(9<<19);main(){'+";".join(d)+';}')
import os
s = os.system
s('cc f.c')
s('./a.out')
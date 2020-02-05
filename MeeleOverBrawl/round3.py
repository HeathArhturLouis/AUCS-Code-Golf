N='+[-[<<[+[--->]-[<<<]]]>>>-]>-.---.>..>.<<<<-.<+.>>>>>.>.<<.<-.'
import os
#os.system('rm ./a.out')
with open('f.cpp','w') as f:
    m = {
        ">":"++i;a.push_back(0)",
        "<":"a.push_front(0)",
        "+":"++a[i]",
        "-":"--a[i]",
        ".":"putchar(a[i])",
        ",":"a[i]=getchar()",
        "[":"while(a[i]){",
        "]":"}"
    }
    ccomm = [m[c] for c in N]
    f.write('#include <deque>\n#include <cstdio>\nint main(){std::deque<int> a;size_t i = 0;' + ";".join(ccomm) + ';}')


os.system('g++ f.cpp')
os.system('./a.out')

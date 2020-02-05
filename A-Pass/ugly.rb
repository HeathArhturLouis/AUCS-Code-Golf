u=[d=e=f=(a=b=c=0)+1];(1..1e4).zip{|i|p u[i]=[d,e,f].min;u[i]==d&&(a+=1)&&d=u[a]*2;u[i]==e&&(b+=1)&&e=u[b]*3;u[i]==f&&(c+=1)&&f=u[c]*5}

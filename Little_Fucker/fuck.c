int i, j;
main(){int n=strlen(a);while(i<=n){if(a[i]==">") i++;if(a[i]=="<") i--;if(a[i]=="+") w[i]++;if(a[i]=="-")w[i]--;if(a[i]==".")putchr(w[i]);if(a[i]==",") {scanf("%c",&w[i]);}if(a[i]=="[") {if(w[i]==0){ for(int j=i;j<=n;j++) if(a[j]=="[") {i=j; j=n+1;}}}if(a[i]=="]"){ if(w[i]!=0) for(int j=i;j>=0;j--) if(a[j]=="[") {i=j;j=-1;}}i++;}}

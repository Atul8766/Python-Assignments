let n=1;
let esum=0;
let osum=0;
let sum = [];
while(n<=100)
{
    if(n%2==0)
    {
        esum = esum+n;
    }
    else
    {
        osum = osum+n;
    }
    n = n+1;
}

sum.push(esum);
sum.push(osum);

console.log(sum);
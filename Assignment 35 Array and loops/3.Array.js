const ages = [19,22,19,24,20,25,26,24,25,24];
let max = ages[0];
// Logic for finding maximum element in array 
for(let i=0; i<ages.length; i++)
{
    if(ages[i]>max)
    {
        max = ages[i];
    }
}
console.log(max);

// Logic for finding minimum element in array 
let min = ages[0];
for(let i=0; i<ages.length; i++)
{
    if(ages[i]<min)
    {
        min = ages[i];
    }
}
console.log(min);

//sorting array and then find max and min

ages.sort();
console.log(ages[ages.length-1]);
console.log(ages[0]);

//Find the median age(one middle item or two middle items divided by two)
console.log(ages);
len = ages.length;
console.log(ages[len/2]);

//Find the average age(all items divided by number of items)
//first we try by our logic;
let sum = 0;
for(let i=0; i<ages.length; i++)
{
    sum = sum+ages[i];
}
let avg = sum/ages.length;

//Find the range of the ages(max minus min)

//Compare the value of (min - average) and (max - average), use abs()
//method

let minimum = min-avg;
console.log(Math.abs(minimum));

let maximum = max-avg;
Math.abs(maximum);
console.log(maximum);


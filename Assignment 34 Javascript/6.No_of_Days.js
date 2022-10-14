let month = 13;

if(month>12)
{
    console.log("Invalid Input");
}
else if(month==4 || month == 6 || month == 9 || month ==11)
{
    console.log("31 Days");
}
else if(month == 2)
{
    console.log("28 or 29 Days");
}
else
{
    console.log("30 Days");
}
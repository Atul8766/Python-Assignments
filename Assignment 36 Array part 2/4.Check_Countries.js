const count = [
      "India",
      "Japan",
      "Germany",
      "Finland",
      "Kenya",
      "Nepal",
      "Ireland",
      "Egypt",
    ];

let arg1 = count.filter((arg)=>arg.includes("and"));
if(arg1.length)
{
    console.log(arg1);
}
else
{
    console.log(count);
}
function check_type(arr) {
    for(let i=0; i<arr.length; i++)
    {
        if(typeof arr[i]!="number")
        {
            return 1;
        }
    }
    return 0;
}

let arr = [1,2,3,4,5,6,9,"hello"];
if(check_type(arr))
{
    console.log("All items are not same");
}
else
{
    console.log("All Items are same");
}
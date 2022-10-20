function sumofArrayitems(arr)
{
    let sum=0;
    for(let i=0; i<arr.length; i++)
    {
        if(typeof arr[i]=="number")
        {
            sum = sum+arr[i];
        }
        else 
        {
            return"Array have some different types that so it is not possible to sum";
        }
    }
    return sum;
}

let arr = [1,2,3,4,5,6,7,8,9,10];
// if(typeof arr[0] === "number")
// {
//     console.log("object");
// }
console.log(sumofArrayitems(arr));

function modifyArray(arr)
{
    if(arr.length<5)
    {
        return"item not found";
    }
    else
    {
        arr[5] = "hello";
    }
    return arr;
}

let arr = [1,2,6,5,6,8];
console.log(modifyArray(arr));
let arr= ['banana', 'orange', 'mango', 'lemon'];

function captalize_array(arr)
{   let arr1=[];
    
    for(let i=0; i<arr.length; i++){
        arr1.push(arr[i].toUpperCase());
    }
    return arr1;
   
}

let arr1 = captalize_array(arr);
console.log(arr1);
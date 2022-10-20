const randomid = ()=>
{
    let n = (Math.random()*12345789110).toString(16);
    return "#"+n.slice(0,50);
};

console.log(randomid());
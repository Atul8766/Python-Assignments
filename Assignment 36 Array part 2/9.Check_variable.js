function check_var(vari)
{
    for(let i=0; i<vari.length; i++)
    {
        if(vari.charAt(i)=='$' || vari.charAt(i)=='_' || vari.charAt(i)=='.')
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}

let varname = ".name";

if(check_var(varname))
{
    console.log("Variable name is not valid");
}
else
{
    console.log("Variable name is valid");
}
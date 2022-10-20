const shoppingCart = ['Milk',
'Coffee', 'Tea', 'Honey']

console.log(shoppingCart.unshift("Meat"));
console.log(shoppingCart);
console.log(shoppingCart.push("Sugar"));
console.log(shoppingCart);
console.log(shoppingCart.splice(4,1));
console.log(shoppingCart);
shoppingCart[3] = "Green Tea";
console.log(shoppingCart);
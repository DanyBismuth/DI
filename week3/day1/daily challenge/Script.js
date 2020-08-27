var array = ["Banana", "Apples", "Oranges", "Blueberries"];
array.shift();
array.push("kiwi");
array.shift();
array.reverse();
console.log(array);

var array2 = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
array2[1][1][0]
console.log(array2[1][1][0])
const arr = [5,0,9,1,7,4,2,6,3,8];
//The output should be: [9,8,7,6,5,4,3,2,1,0]

function bubble_Sort(a)
{
    var swapp;
    var n = a.length-1;
    var x=a;
    do {
        swapp = false;
        for (var i=0; i < n; i++)
        {
            if (x[i] < x[i+1])
            {
               var temp = x[i];
               x[i] = x[i+1];
               x[i+1] = temp;
               swapp = true;
            }
        }
        n--;
    } while (swapp);
 return x; 
}

console.log(bubble_Sort(arr))	

console.log(arr.toString())
console.log(arr.join('+'))
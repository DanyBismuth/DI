//exercise 1

	// function checkDriverAge() {
	// let age = prompt("What is your age?");

	// if (Number(age) < 18) {
	//     alert("Sorry, you are too yound to drive this car. Powering off");
	// } else if (Number(age) > 18) {
	//     alert("Powering On. Enjoy the ride!");
	// } else if (Number(age) === 18) {
	//     alert("Congratulations on your first year of driving. Enjoy the ride!");
	// }}

	// function checkDriverAge(age) {

	// if (Number(age) < 18) {
	//     alert("Sorry, you are too yound to drive this car. Powering off");
	// } else if (Number(age) > 18) {
	//     alert("Powering On. Enjoy the ride!");
	// } else if (Number(age) === 18) {
	//     alert("Congratulations on your first year of driving. Enjoy the ride!");
	// }}

	// checkDriverAge(92);

// Exercise 2

	// amazonBasket = {
	//     glasses: 1,
	//     books: 2,
	//     floss: 100
	// }

	// function checkBasket() {
	// 	var item = prompt("What item do you want ?")

	// if (item in amazonBasket) {
	// 	alert("your item is in the basket")
	// }else {
	// 	alert("your item is not in the basket")
	// }
	// }

	// checkBasket();

//Exercise 3

	// function EnoughChange(pocketChange, price){
	// 	var sum = 0
	// 	sum = sum+pocketChange[0]*0.25
	// 	sum = sum+pocketChange[1]*0.10
	// 	sum = sum+pocketChange[2]*0.05
	// 	sum = sum+pocketChange[3]*0.01
		
	// 	if (sum>=price) {
	// 		console.log("you have enough money")
	// 	}else {
	// 		console.log("you are short on money")
	// 	}
	// }

	// EnoughChange([2, 100, 0, 0], 14.11);
	// EnoughChange([0, 0, 20, 5], 0.75);

//Exercise 4

	// var ShoppingList = ["banana","orange","apple"];

	// let stock = { 
	//     "banana": 6, 
	//     "apple": 0,
	//     "pear": 12,
	//     "orange": 32,
	//     "blueberry":1
	// }  

	// let prices = {    
	//     "banana": 4, 
	//     "apple": 2, 
	//     "pear": 1,
	//     "orange": 1.5,
	//     "blueberry":10
	// } 

	// let sumoftheprices = 0

	// function myBill(){
	// 	for (item of ShoppingList){
	// 		if (stock[item] > 0) {
	// 			sumoftheprices = sumoftheprices + prices[item]
	// 		}
	// 	}
	// 	}
	// 	return sumoftheprices;
		
	// }

	// console.log(myBill())

// Exercise 5

	// console.log(Math.floor(Math.random() * 100));

	// function random(begin, end){
	// 	if (begin%2 === 1) {
	// 		begin++
	// 	}
	// 	for (i = begin; i <= end; i+=2){
	// 		console.log(i)
	// 	}
	// }

	// random(0, 100);

// Exercise 6

	// var sum = 0 ;
	// function multiplyof23(number){
	// 	for(var i=1; i < number; i++){
	// 		if(i % 23 == 0){
	// 			sum = sum + i;
	// 		}
	// 	}
	// 	return sum;
	// }

	// console.log(multiplyof23(500));

// Exercise 7

	// function hotelCost(){
	// 	var night = prompt("how many night would you like to stay ?")
	// 	var cost = Number(night)*140
	// 	return cost;
	// };

	// var place = {
	// 		"London" : 183,
	// 		"Paris" : 220,
	// 		"Other" : 300,
	// 	}

	// function plane_ride_cost(){
	// 	var destination = prompt("where do you want to go?")
	// 	if(place[destination]){
	// 		return place[destination]
	// 	}else {
	// 		return place["Other"]
	// 	}
	// }

	// function rental_car_cost(){
	// 	var days = prompt("How many days would you like to rent a car ?")
	// 	var cost = Number(days)*40;
	// 	if(days>10){
	// 		cost= cost*0.95
	// 	}
	// return cost
	// }

	// function total_vacation_cost(){
	// 	var total = hotelCost() + plane_ride_cost() + rental_car_cost() 

	// 	console.log(total)
	// }
	// total_vacation_cost();
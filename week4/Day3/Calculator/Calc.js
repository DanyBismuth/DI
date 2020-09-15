let calcstrg="";
let calcdisplay = document.getElementByID('display');
function my_f(btn) {
	calcstrg = calcstrg + btn;
	display.innerHTML = calcstrg;
}

function result(){
	let calcrsult = eval(calcstrg);
	display.innerHTML = calcrsult;
	calcstrg= calcrsult;
}

function calclear(){
	calcstrg = "";
	display.innerHTML = 0;
}
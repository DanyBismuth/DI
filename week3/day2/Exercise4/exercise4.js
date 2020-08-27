let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
let nbonline = parseIn(prompt('enter number of people online'));

if (nbonline = 0) {
	console.log('no one online')

}else if (nbonline === 1) {
	console.log(users[0] + "online")
} else if (nbonline === 2) {
	console.log('${users[0]} ${users[1]} are online')
}else if (nbonline >2) {
	console.log('${users[0]} ${users[1]} ${user[2]} are online')
}

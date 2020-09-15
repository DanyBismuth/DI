const buttonElement = document.getElementById('btn');

buttonElement.addEventListener('click', function (event) {
  alert("UUUUPS");
  })

buttonElement.addEventListener('click', {
  handleEvent: function (event) {
    alert("Sorry I didn't had time to link my resume yet");
}})



const form = document.getElementById('contact');

form.addEventListener('focus', (event) => {
  event.target.style.background = 'grey';    
}, true);

form.addEventListener('blur', (event) => {
  event.target.style.background = '';    
}, true);



// document.addEventListener('keydown', logKey);

// function logKey(e) {
//   moi.textContent += "let's talk about me";
// }


const log = document.getElementById('comment');

document.addEventListener('keypress', logKey);

function logKey(e) {
  log.textContent += "if you are interested let me a comment at the bottom";
}
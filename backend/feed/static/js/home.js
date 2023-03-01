
var coll = document.getElementsByClassName("header-collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {

    var content = this.nextElementSibling;
    if (content.style.display === "block") {
      content.style.display = "none";
    } else {
      content.style.display = "block";
    }
  });
}



// Get the modal
var loginModal = document.getElementById("loginModal");
var signupModal = document.getElementById("signUpModal");


// Get the button that opens the modal
var loginBtn = document.getElementById("loginBtn");
var signUpBtn = document.getElementById("signUpBtn");



// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];
var spanLogin = document.getElementsByClassName("closeLogin")[0];




// When the user clicks the button, open the modal 
loginBtn.onclick = function() {
  loginModal.style.display = "block";
}
signUpBtn.onclick = function() {
  signupModal.style.display = "block";
}




// When the user clicks on <span> (x), close the modal
spanLogin.onclick = function() {
  loginModal.style.display = "none";
}
span.onclick = function() {
  signupModal.style.display = "none";
}




// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    loginModal.style.display = "none";
  }
}
window.onclick = function(event) {
  if (event.target == modal) {
    signupModal.style.display = "none";
  }
}
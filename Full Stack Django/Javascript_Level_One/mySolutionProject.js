var firstName = prompt("What is your First Name? ");
var lastName = prompt("What is your Last Name? ");
var age = prompt("What is your Age? ");
var height = prompt("What is your height? ");
var color = prompt("What is the Color of Moon? ");
alert("Thanku For Filling The Form.")




if (firstName[0]!=lastName[0]){
   console.log("Sorry! your'e not the appropiate person.");
}
else if (age < 20 && age > 30) {
   console.log("Sorry! your'e not the appropiate person.");
}
else if (height < 170) {
   console.log("Sorry! your'e not the appropiate person.");
}
else if (color != "red") {
   console.log("Sorry! your'e not the appropiate person.");
}
else {
  console.log("Welcome! "+firstName + " " + lastName + "\n Your next task will be given to you soon.");
}

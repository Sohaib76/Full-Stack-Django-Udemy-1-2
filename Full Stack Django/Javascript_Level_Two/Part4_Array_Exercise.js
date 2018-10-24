// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []

// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addNew(name) {
  roster.push(name);
}

// REMOVE STUDENT

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster
function remove(name){
  var i = roster.indexOf(name);
  roster.splice(i,1);
}
// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the roster to the console.
function display() {
  console.log(roster);
  // for (letter of roster){
  //     console.log(letter);
  //   }
}

// Start by asking if they want to use the web app
var start = prompt("Do you want to continue to the web App? Y/n")
  if (start == "n") {
    alert("Refresh the page to restart! ")
  }
// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
while (start == "Y") {
  var ask = prompt("What do you want to do with the Student Name?   (add,remove,display or quit)")


  if(ask == "add"){
    var add = prompt("Enter the Student Name: ");
    addNew(add);
  }


  else if (ask == "remove") {
    var remov = prompt("Enter the Student Name to Remove: ");
    remove(remov)
  }

  else if (ask == "display") {
    display();
  }

  else if (ask == "quit") {
    alert("Thanks For using! Refresh the page to restart..")
    break;

  }
  else {
    alert("Invalid Input");
  }


}

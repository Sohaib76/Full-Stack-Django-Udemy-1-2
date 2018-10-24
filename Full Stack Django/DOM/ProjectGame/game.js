

//restartBtn
var restart = document.querySelector('#restartBtn');

//Grab All Squares
var squares = document.querySelectorAll('td');





//function of clearBoxes
function clearBoxes() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}

//restart event
restart.addEventListener("click",clearBoxes);




//ticTac function
function ticTac() {
  if(this.textContent == ''){
    this.textContent = 'X';
  }
  else if (this.textContent == 'X') {
    this.textContent = 'O';
  }
  else {
    this.textContent = '';
  }
}

//tic Tac
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click",ticTac);
}






// document.getElementById("myH2").style.color = "#ff0000";



// var a =1 ;
//
//
// function dosomething(){
// if(a=1){
//    document.getElementById('#tt').innerHTML='x';
//    console.log("AD");
// }else{
//    document.getElementById('#tt').innerHTML='O';
// }
// a=0;
//
// }



// table.addEventListener("click",dosomething);


//console.log("GOO");

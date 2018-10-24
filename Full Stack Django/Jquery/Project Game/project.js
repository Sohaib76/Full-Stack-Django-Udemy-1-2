

var player1 = prompt("Player One, Enter your name. You will be Blue.");
var player2 = prompt("Player Two, Enter your name. You will be Red.");

//Grab h3
var head3 = $('h3');



//Sir
var player1Color = 'rgb(86, 151, 255)';
var player2Color = 'rgb(237, 45, 73)';           //use rgb in jQuery



var game_on = true;
var table = $('table tr');





//just for debugging
function reportWin(rowNum,colNum) {
  console.log("You won starting at this row and column");
  console.log(rowNum);
  console.log(colNum);
}




//
function changeColor(rowIndex,colIndex,color) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color',color);
}

//
function returnColor(rowIndex,colIndex) {
  return table.eq(rowIndex).find('td').eq(colIndex).find('button').css('background-color');
}
//
function checkBottom(colIndex) {
  var colorReport = returnColor(5,colIndex);
  for (var row = 5; row > -1; row--) {
    colorReport = returnColor(row,colIndex);
    if (colorReport === 'rgb(128, 128, 128)') {
      return row;
    }
  }
}

//
function colorMatchCheck(one,two,three,four) {
  return (one===two && one===three && one===four && one !== 'rgb(128, 128, 128)' && one !== undefined);
}


//Win check Big codes

//horizontalWinCheck
function horizontalWinCheck() {
  for (var row = 0; row < 6; row++) {
    for (var col = 0; col < 4; col++) {   //Had made a mistake
      if (colorMatchCheck(returnColor(row,col), returnColor(row,col+1), returnColor(row,col+2), returnColor(row,col+3) )) {
        console.log("horizontal");
        reportWin(row,col);
        return true;
      }
      else {
        continue;
      }
    }
  }
}


//vericalWinCheck
function verticalWinCheck() {
  for (var col = 0; col < 7; col++) {
    for (var row = 0; row < 3; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col), returnColor(row+2,col), returnColor(row+3,col) )) {
        console.log("vertical");
        reportWin(row,col);
        return true;
      }
      else {
        continue;
      }
    }
  }
}

//Diagonal Win check
function diagonalWinCheck(){
  for (var col = 0; col < 5; col++) {
    for (var row = 0; row < 7; row++) {
      if (colorMatchCheck(returnColor(row,col), returnColor(row+1,col+1), returnColor(row+2,col+2), returnColor(row+3,col+3) )) {
        console.log("negative slope");
        reportWin(row,col);
        return true;
      }
      else if (colorMatchCheck(returnColor(row,col), returnColor(row-1,col+1), returnColor(row-2,col+2), returnColor(row-3,col+3) )) {  //Had made a mistake
        console.log("possitive slope");
        reportWin(row,col);
        return true;
      }
      else {
        continue;
      }
    }
  }
}












//Game Logic

// Start with Player One
var currentPlayer = 1;
var currentName = player1;
var currentColor = player1Color;




//Start with one
head3.text("Player One: " + player1+ " this is your turn. Please select a column to drop your blue chip.");
$('.board button').on('click',function() {
  // Recognize what column was chosen
  var col = $(this).closest('td').index();

// Get back bottom available row to change
  var bottomAvail = checkBottom(col);
  // Drop the chip in that column at the bottomAvail Row
  changeColor(bottomAvail,col,currentColor);

  if (horizontalWinCheck() || verticalWinCheck() || diagonalWinCheck()) {
    $('h1').text(currentName+" You Have Won!");
    $('h2').fadeOut('fast');
    $('h3').fadeOut('fast');
    $("button").off("click");
  }

  //changing players
  currentPlayer = currentPlayer * -1;             //loop

  if(currentPlayer===1){
    currentName = player1;
    currentColor = player1Color;
    head3.text("Player One:" + currentName+" this is your turn. Please select a column to drop your blue chip.");
  }else {
    currentName = player2;
    currentColor = player2Color;
    head3.text("Player Two:" + currentName+" this is your turn. Please select a column to drop your red chip.");
  }

})
























// $('td').eq(0).click(function() {
//   $('td').eq(28).css("background-color",'blue');
// })
//
//
// $('td').eq(1).click(function() {
//   $('td').eq(29).css("background-color",'red');
// })
//x.css("color",'red');

// for (var i = 0; i < td.length; i++) {
//   $(td[i]).css("background-color",'blue');
// }]



// $('td').eq(x).click(function() {
//   $('td').eq(34-(6-x)).css("background-color",'red');
// })

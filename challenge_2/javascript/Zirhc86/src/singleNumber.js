var array = [2, 3, 4, 2, 3, 5, 4, 6, 4, 6, 9, 10, 9, 8, 7, 8, 10, 7];
var mixedArray = 
    [2,'a','l',3,'l',4,'k',2,3,4,5,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7];

// Passes array values as keys into 'acc' object and increments by 1 each time
// a value is encountered
function getTally(arr){
  return arr.reduce(function(acc, curr){
    acc[curr] ? acc[curr]++ : acc[curr] = 1;
    return acc;
  }, {});
}

// Filter out any keys in object that has a value of 1, and add to a string,
// separating chars with ', ' for each new addition
function logSingles(obj){
  var singles = '';
  for (var key in obj){
    if(obj[key] === 1){
      singles.length >=1 ? singles += ', ' + key : singles = key;
    }
  }
  return singles;
}

function test(arr){
  console.log(logSingles(getTally(arr)));
}

test(array);
test(mixedArray);

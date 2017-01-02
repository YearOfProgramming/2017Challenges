const arr1 = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7];
const arr2 = [2,'a','l',3,'l',4,'k',2,3,5,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7];

const count = (arr) => {
  if (arr.constructor !== Array) {
    return;
  }

  const hash = {};
  arr.forEach(char => {
    hash[char] = hash[char] ? hash[char] + 1 : 1;
  });

  return hash;
}

const unique = (arr) => {
  const hash = count(arr);
  if (!hash) {
    return "Not an array";
  }

  const singles = [];
  for (const i in hash) {
    if (hash.hasOwnProperty(i) && hash[i] === 1) {
      singles.push(i);
    }
  }
  return singles;
}

console.log(unique("arr1"));
console.log(unique(arr1));
console.log(unique(arr2));
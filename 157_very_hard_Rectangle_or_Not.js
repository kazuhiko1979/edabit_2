function isRectangle(coordinates) {
  function parsePoint(point) {
      point = point.replace(/[()]/g, ''); // Remove parentheses
      let [x, y] = point.split(',').map(Number); // Split by comma and convert to numbers
      return [x, y];
  }

  let points = coordinates.map(parsePoint);
  
  if (points.length !== 4) {
      return false;
  }

  function isParallelSides(p1, p2, p3, p4) {
      return (p2[0] - p1[0]) * (p4[1] - p3[1]) === (p2[1] - p1[1]) * (p4[0] - p3[0]);
  }

  function distance(p1, p2) {
      return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2;
  }

  function* permutations(array) {
      if (array.length <= 1) yield array;
      else {
          let [first, ...rest] = array;
          for (let perm of permutations(rest)) {
              for (let i = 0; i <= perm.length; i++) {
                  let start = perm.slice(0, i);
                  let rest = perm.slice(i);
                  yield [...start, first, ...rest];
              }
          }
      }
  }

  for (let perm of permutations(points)) {
      let [A, B, C, D] = perm;
      if (isParallelSides(A, B, C, D) && isParallelSides(A, D, B, C) &&
          distance(A, B) === distance(C, D) && distance(A, D) === distance(B, C)) {
          return true;
      }
  }
  return false;
}

console.log(isRectangle(["(-4, 3)", "(4, 3)", "(4, -3)", "(-4, -3)"])); // true
console.log(isRectangle(["(0, 0)", "(0, 1)"])); // false
console.log(isRectangle(["(0, 0)", "(0, 1)", "(1,0)"])); // false
console.log(isRectangle(["(0, 0)", "(9, 0)", "(7,5)", "(16, 5)"])); // true
console.log(isRectangle(["(0, 0)", "(1, 0)", "(0, 1)", "(0, 0)"])); // false
console.log(isRectangle(["(1, 0)", "(1, 2)", "(2, 1)", "(2, 3)", "(3, 3)"])); // false
console.log(isRectangle(["(-2, 2)", "(-2, -1)", "(5, -1)", "(5, 2)"])); // true

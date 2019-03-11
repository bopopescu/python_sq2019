function sumTest (...theArgs) {
  return theArgs.reduce((previous, current) => {
    return previous + current
  })
}
console.log(sumTest(1, 2, 3))
// expected output: 6

console.log(sumTest(1, 2, 3, 4, 10))
// expected output: 10

function square (arr) {
  return arr.map(function (item) {
    return item * item
  })
}

var arr = [1, 2, 3, 4]
console.log(square(arr))

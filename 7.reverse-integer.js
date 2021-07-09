var reverse = function(x) {
  let ans = Math.sign(x) * +[...`${Math.abs(x)}`].reverse().join('')
  return (ans < -(2**31) || ans > (2**31)) ? 0 : ans
};
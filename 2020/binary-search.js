function binarySearch(arr, v){
  let startIdx = 0
  let endIdx = arr.length - 1
  let midIdx = ~~((endIdx + startIdx)/2)

  while (arr[midIdx] !== v && startIdx < endIdx) {
    if      (v < arr[midIdx]) endIdx = midIdx - 1;
    else if (v > arr[midIdx]) startIdx = midIdx + 1;
    midIdx = ~~((endIdx + startIdx)/2)
  }

  return (arr[midIdx] !== v) ? -1 : midIdx;
}
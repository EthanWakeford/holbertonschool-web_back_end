/* eslint-disable no-param-reassign */
export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  for (const val of array) {
    array[idx] = appendString + val;
    idx += 1;
  }

  return array;
}

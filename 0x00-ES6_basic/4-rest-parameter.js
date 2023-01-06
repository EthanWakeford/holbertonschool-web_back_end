/* eslint-disable no-unused-vars */
export default function returnHowManyArguments(...args) {
  let count = 0;
  for (const i of args) {
    count = count + 1;
  }
  return count;
}

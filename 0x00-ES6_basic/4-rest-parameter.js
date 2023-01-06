export default function returnHowManyArguments(...args) {
  let count = 0;
  for (const i of args) {
  count++;
  };
  return count;
}

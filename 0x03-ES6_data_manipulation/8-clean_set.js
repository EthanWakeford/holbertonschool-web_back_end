export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  let s = '';
  for (const i of set) {
    if (i.startsWith(startString)) {
      if (s !== '') {
        s += '-';
      }
      s += i.slice(startString.length);
    }
  }
  return s;
}

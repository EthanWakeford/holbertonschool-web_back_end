export default function cleanSet(set, startString) {
  if (startString === '' || typeof startString !== 'string') {
    return '';
  }
  let s = '';
  for (const i of set) {
    if (typeof i !== 'string') {
      continue;
    }
    if (i.startsWith(startString)) {
      if (s !== '') {
        s += '-';
      }
      s += i.slice(startString.length);
    }
  }
  return s;
}

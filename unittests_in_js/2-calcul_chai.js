function calculateNumber(type, a, b) {
  roundedA = Math.round(a);
  roundedB = Math.round(b);

  if (type === 'SUM') {
    return roundedA + roundedB;
  } else if (type === 'SUBTRACT') {
    return roundedA - roundedB;
  } else {
    if (roundedB === 0) {
      return 'Error';
    }
    return roundedA / roundedB;
  }
}

module.exports = calculateNumber;

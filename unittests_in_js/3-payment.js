const calculateNumber = require("./utils.js").calculateNumber;

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const result = calculateNumber("SUM", totalAmount, totalShipping);
  console.log(`The total is: ${result}`);
  return result;
}

module.exports = sendPaymentRequestToApi;

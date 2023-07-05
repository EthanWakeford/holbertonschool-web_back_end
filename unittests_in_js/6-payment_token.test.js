const expect = require("chai").expect;
const getPaymentTokenFromAPI = require("./6-payment_token");

describe("getPaymentTokenFromAPI", () => {
  it("testing getPayment", (done) => {
    getPaymentTokenFromAPI(true)
      .then((response) => {
        expect(response).to.eql({ data: "Successful response from the API" });
        done();
      })
      .catch((error) => {
        done(error);
      });
  });
});

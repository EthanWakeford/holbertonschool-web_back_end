const { expect } = require("chai");
const { response } = require("express");
const request = require("request");

describe("testing get request", () => {
  it("returns correct string and 200 status", (done) => {
    request("http://localhost:7865/", (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Welcome to the payment system");
      done();
    });
  });
  it("works with int as id", (done) => {
    request("http://localhost:7865/cart/2", (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal("Payment methods for cart 2");
      done();
    });
  });
  it("does not work with not int as id", (done) => {
    request("http://localhost:7865/cart/notanumber", (err, res, body) => {
      expect(res.statusCode).to.equal(404);
      done();
    });
  });
  it("returns proper json object", (done) => {
    request("http://localhost:7865/available_payments", (err, res, body) => {
      expect(res.statusCode).to.equal(200);
      expect(body).to.equal(
        '{"payment_methods":{"credit_cards":true,"paypal":false}}'
      );
      done();
    });
  });
  // it("does psoting", (done) => {
  //   request(
  //     {
  //       method: "POST",
  //       url: "http://localhost:7865/login",
  //       body: {
  //         userName: "asdfd",
  //       },
  //     },
  //     (error, response, body) => {
  //       expect(response.statusCode).to.equal(200);
  //       expect(body).to.equal("Welcome asdfd");
  //       done();
  //     }
  //   );
  // });
});

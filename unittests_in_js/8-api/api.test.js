const { expect } = require("chai");
const { response } = require("express");
const request = require("request");

describe("testing get request", () => {
  it("returns correct string and 200 status", () => {
    request("http://localhost:7865/", (err, res, body) => {
      expect(res.statusCode).to.equal(200)
      expect(body).to.equal('Welcome to the payment system')
    })
  });
});

const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./3-payment.js");

describe("sendPaymentRequestToApi", () => {
  it("should use the calculateNumber function properly", () => {
    const stub = sinon.stub(Utils, "calculateNumber").returns(10);
    const consoleSpy = sinon.spy(console, 'log');

    const res = sendPaymentRequestToApi(100, 20);

    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(consoleSpy.calledWithExactly('The total is: 10')).to.be.true;
    expect(Utils.calculateNumber("SUM", 100, 20)).to.equal(10);
    expect(res).to.equal(10);

    stub.restore();
    consoleSpy.restore();
  });
});

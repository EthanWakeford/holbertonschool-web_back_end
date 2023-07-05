const sinon = require("sinon");
const { expect } = require("chai");
const Utils = require("./utils.js");
const sendPaymentRequestToApi = require("./3-payment.js");

describe("sendPaymentRequestToApi", () => {
  it("should use the calculateNumber function properly", () => {
    const spyUtils = sinon.spy(Utils, "calculateNumber");

    const res = sendPaymentRequestToApi(100, 20);

    expect(spyUtils.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    expect(Utils.calculateNumber("SUM", 100, 20)).to.equal(res);

    spyUtils.restore();
  });
});

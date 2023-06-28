const assert = require('assert');
const { describe } = require('node:test');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', () => {
  it('should equal 4', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it('should equal 5 with float', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('should equal 5 with floats', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('should equal 6 with floats', () => {
    assert.equal(calculateNumber(1.5, 3.7), 6);
  });
});

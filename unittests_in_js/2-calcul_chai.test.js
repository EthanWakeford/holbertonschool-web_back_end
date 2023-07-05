// test for 2-calcul_chai.js
const assert = require('assert');
const calculateNumber = require('./2-calcul_chai.js');
const { expect } = require('chai');

describe('calculateNumber', function () {
    it('should return the sum of rounded numbers', function () {
        // Test case 1
        const result1 = calculateNumber('SUM', 1.4, 4.5);
        expect(result1).to.equal(6)

        // Test case 2
        const result2 = calculateNumber('SUBTRACT', 1.4, 4.5);
        expect(result2).to.equal(-4);

        // Test case 3
        const result3 = calculateNumber('DIVIDE', 1.4, 4.5);
        expect(result3).to.equal(0.2);

        // Test case 4
        const result4 = calculateNumber('DIVIDE', 1.4, 0);
        expect(result4).to.equal('Error');
    });
});

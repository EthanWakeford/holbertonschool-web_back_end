// test for 0-calcul.js
const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
    it('should return the sum of rounded numbers', function () {
        // Test case 1
        const result1 = calculateNumber(3.7, 2.1);
        assert.strictEqual(result1, 6);

        // Test case 2
        const result2 = calculateNumber(1.4, 7.9);
        assert.strictEqual(result2, 9);

        // Test case 3
        const result3 = calculateNumber(0, 5.6);
        assert.strictEqual(result3, 6);

        // Test case 4
        const result4 = calculateNumber(-2.3, 4.8);
        assert.strictEqual(result4, 3);
    });
});

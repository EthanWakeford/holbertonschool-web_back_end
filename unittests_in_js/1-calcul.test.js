// test for 1-calcul.js
const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', function () {
    it('should return the sum of rounded numbers', function () {
        // Test case 1
        const result1 = calculateNumber('SUM', 1.4, 4.5);
        assert.strictEqual(result1, 6);

        // Test case 2
        const result2 = calculateNumber('SUBTRACT', 1.4, 4.5);
        assert.strictEqual(result2, -4);

        // Test case 3
        const result3 = calculateNumber('DIVIDE', 1.4, 4.5);
        assert.strictEqual(result3, 0.2);

        // Test case 4
        const result4 = calculateNumber('DIVIDE', 1.4, 0);
        assert.strictEqual(result4, 'Error');
    });
});

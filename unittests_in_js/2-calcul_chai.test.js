// 1-calcul.test.js
const assert = require('chai');  // Importando el modulo assert
const expect = chai.expect;
const calculateNumber = required( "./2-calcul_chai.js");


describe('calculateNumber type == SUM', () => {
  it('checks the output', () => {
    expect(calculateNumber('SUM', 1, 3), 4);
    expect(calculateNumber('SUM', 1, 3.7), 5);
    expect(calculateNumber('SUM', 3.7, 1), 5);
    expect(calculateNumber('SUM', 1.4, 4.5), 6);
    expect(calculateNumber('SUM', 4.5, 1.4), 6);
    expect(calculateNumber('SUM', 0.0, 0), 0);
    expect(calculateNumber('SUM', -1, 1), 0);
    expect(calculateNumber('SUM', 1, -1), 0);
    expect(calculateNumber('SUM', -1, -1), -2);
  });
});

describe('calculateNumber type == SUBTRACT', () => {
  it('checks the output', () => {
    expect(calculateNumber('SUBTRACT', 5, 3), 2);
    expect(calculateNumber('SUBTRACT', 3.1, 2.5), 0);
    expect(calculateNumber('SUBTRACT', 4.5, 2), 3);
    expect(calculateNumber('SUBTRACT', 0.0, 5), -5);
    expect(calculateNumber('SUBTRACT', 2, 4.5), -3);
    expect(calculateNumber('SUBTRACT', -1, 1), -2);
    expect(calculateNumber('SUBTRACT', -1.5, 0), -1);
  });
});

describe('calculateNumber type == DIVIDE', () => {
  it('check the output', () => {
    expect(calculateNumber('DIVIDE', 2, 2.5), 0.6666666666666666);
    expect(calculateNumber('DIVIDE', 0.0, 2), 0);
    expect(calculateNumber('DIVIDE', -1, 1), -1);
    expect(calculateNumber('DIVIDE', 1, 0), 'Error');
  });
});

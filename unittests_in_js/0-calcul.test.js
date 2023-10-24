const assert = require("assert"); // Importando el modulo assert
const calculateNumber = require("./0-calcul.js"); // Importando nuestra funcion

describe("calculateNumber", () => {
  it('should round two numbers and return their sum', () => {
  //Prueba 1
    assert.strictEqual(calculateNumber(1.5, 2.3), 4);

    //Prueba 2
    assert.strictEqual(calculateNumber(3.7, 5.1), 9);

    //Prueba 3
    assert.strictEqual(calculateNumber(1.1, 0.3), 1);
  });
});


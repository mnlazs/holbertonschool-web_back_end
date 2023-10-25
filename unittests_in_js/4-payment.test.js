'use strict';
const chai = require('chai');
const sinon = require('sinon');
const Utils = require('./utils.js');

// Importar la función que quieres probar desde el archivo 3-payment.js
const sendPaymentRequestToApi = require('./3-payment.js');

describe('sendPaymentRequestToApi function', () => {
  // Configurar un stub para Utils.calculateNumber
  const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
  
  // Configurar un espía para console.log
  let consoleLogSpy;

  before(() => {
    consoleLogSpy = sinon.spy(console, 'log');
  });

  after(() => {
    consoleLogSpy.restore();
  });

  it('validate the usage of the Utils function', () => {
    // Llama a la función que quieres probar
    sendPaymentRequestToApi(100, 20);

    // Verifica que el stub se llama correctamente
    sinon.assert.calledWith(calculateNumberStub, 'SUM', 100, 20);

    // Verifica que el espía de console.log registra el mensaje correcto
    chai.expect(consoleLogSpy.calledWith('The total is: 10')).to.be.true;
  });

  // Restaurar el stub después de las pruebas
  after(() => {
    calculateNumberStub.restore();
  });
});

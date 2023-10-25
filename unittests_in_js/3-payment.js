const Utils = require("./utils.js")

function sendPaymentRequestToApi(totalAmount, totalShipping) {
    var resultado = Utils.calculateNumber("SUM", totalAmount, totalShipping);
    console.log("The total is:" + resultado);
}
module.exports = sendPaymentRequestToApi;

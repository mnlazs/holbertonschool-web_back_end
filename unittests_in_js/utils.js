'use strict';
const Utils = {
    calculateNumber(type, a, b) {
      if (type === 'SUM') return Math.round(a) + Math.round(b);
      if (type === 'SUBTRACT') return Math.round(a) - Math.round(b);
      if (type === 'DIVIDE') return Math.round(b) === 0 ? 'Error' : Math.round(a) / Math.round(b);
    }
  }
  // Exportar la función calculateNumber para que esté disponible fuera del módulo
  module.exports = Utils;

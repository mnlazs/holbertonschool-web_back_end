// 2-read_file.js 
const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const students = lines.map((line) => {
      const [name, field] = line.split(',');
      return { name, field };
    });

    const fieldCounts = {};
    const allStudents = [];

    for (const student of students) {
      if (fieldCounts[student.field]) {
        fieldCounts[student.field]++;
      } else {
        fieldCounts[student.field] = 1;
      }
      allStudents.push(student.name);
    }

    const totalStudents = students.length;

    console.log(`Number of students: ${totalStudents}`);
    for (const field in fieldCounts) {
      console.log(`Number of students in ${field}: ${fieldCounts[field]}. List: ${allStudents.join(', ')}`);
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;

const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf8');
    let count = 0;
    const fields = {
      CS: {
        studentCount: 0,
        students: [],
      },
      SWE: {
        studentCount: 0,
        students: [],
      },
    };

    for (const row of data.split('\n').slice(1, -1)) {
      const student = row.split(',');
      fields[student[3]].studentCount += 1;
      fields[student[3]].students.push(student[0]);
      count += 1;
    }

    console.log(`Number of students: ${count}`);
    console.log(`Number of students in CS: ${fields.CS.studentCount}.List: ${fields.CS.students.join(', ')}`);
    console.log(`Number of students in SWE: ${fields.SWE.studentCount}.List: ${fields.SWE.students.join(', ')}`);
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;

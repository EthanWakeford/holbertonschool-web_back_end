const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
      fs.readFile(path, 'utf8', (err, data) => {
        if (err) {
          throw new Error('Cannot load the database')
          // console.log('error')
          // reject('Cannot load the database')
        }
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
        console.log(`Number of students in CS: ${fields.CS.studentCount}. List: ${fields.CS.students.join(', ')}`);
        console.log(`Number of students in SWE: ${fields.SWE.studentCount}. List: ${fields.SWE.students.join(', ')}`);
        resolve();
      });
  });
}

module.exports = countStudents;

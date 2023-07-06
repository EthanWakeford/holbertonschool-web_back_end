const fs = require('fs').promises;

function readDatabase(path) {
  return fs
    .readFile(path, 'utf8')
    .then((data) => {
      const fields = {
        CS: {
          students: [],
        },
        SWE: {
          students: [],
        },
      };

      for (const row of data.split('\n').slice(1, -1)) {
        const student = row.split(',');
        fields[student[3]].students.push(student[0]);
      }

      return fields;
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

module.exports = readDatabase;

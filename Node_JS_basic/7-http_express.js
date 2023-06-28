const express = require('express');
const fs = require('fs');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  let response = 'This is the list of our students\n';
  try {
    const data = fs.readFileSync(process.argv[2], 'utf8');
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
    response += `Number of students: ${count}\n`;
    response += `Number of students in CS: ${
      fields.CS.studentCount
    }. List: ${fields.CS.students.join(', ')}\n`;
    response += `Number of students in SWE: ${
      fields.SWE.studentCount
    }. List: ${fields.SWE.students.join(', ')}\n`;
    res.send(response);
  } catch (err) {
    response += 'Cannot load the database';
    res.send(response);
  }
});

app.listen(port, () => {});

module.exports = app;

const http = require('http');
const url = require('url');
const fs = require('fs');

const app = http.createServer((req, res) => {
  const reqUrl = url.parse(req.url).pathname;

  if (reqUrl === '/') {
    res.write('Hello Holberton School!');
    res.end();
  }
  if (reqUrl === '/students') {
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

    res.write('This is the list of our students\n');
    res.write(`Number of students: ${count}\n`);
    res.write(`Number of students in CS: ${fields.CS.studentCount}. List: ${fields.CS.students.join(', ')}\n`);
    res.write(`Number of students in SWE: ${fields.SWE.studentCount}. List: ${fields.SWE.students.join(', ')}\n`);
    res.end();
  }
}).listen(1245);

module.exports = app;

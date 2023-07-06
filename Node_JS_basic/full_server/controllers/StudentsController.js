const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase('../database.csv').then((students) => {
      let returnString = 'This is the list of our students\n';

      students.CS.students.sort();
      students.SWE.students.sort();

      returnString += `Number of students in CS: ${
        students.CS.students.length
      }. List: ${students.CS.students.join(', ')}\n`;
      returnString += `Number of students in SWE: ${
        students.SWE.students.length
      }. List: ${students.SWE.students.join(', ')}`;
      console.log(returnString);
      res.send(returnString);
    });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).write('Major parameter must be CS or SWE');
    }

    readDatabase('../database.csv').then((students) => {
      res.send(`List: ${students[major].students.join(', ')}`);
    });
  }
}

module.exports = StudentsController;

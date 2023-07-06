const readDatabase = require('../utils');

class StudentsController {
  static getAllStudents(req, res) {
    const students = readDatabase('../../database.csv');
    const returnString = 'This is the list of our students\n';

    students.CS.students.sort();
    students.SWE.students.sort();

    returnString.concat(`Number of students in CS: ${students.CS.students.length}. List: ${students.CS.students.join(', ')}\n`);
    returnString.concat(`Number of students in SWE: ${students.SWE.students.length}. List: ${students.SWE.students.join(', ')}`);

    res.send(returnString);
  }
}

module.exports = StudentsController;

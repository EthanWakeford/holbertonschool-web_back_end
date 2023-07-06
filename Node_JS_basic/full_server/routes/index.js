const app = require('../server');
const AppController = require('../controllers/AppController');
const StudentsController = require('../controllers/StudentsController');

app
  .get('/', AppController.getHomepage)
  .get('/students', StudentsController.getAllStudents)
  .get('/students/:major', StudentsController.getAllStudentsByMajor);

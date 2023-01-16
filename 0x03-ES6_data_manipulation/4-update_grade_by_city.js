/* eslint-disable no-param-reassign */
export default function updateStudentGradeByCity(studentArray, city, newGrades) {
  return studentArray.filter((x) => x.location === city)
    .map((x) => {
      x.grade = 'N/A';
      return x;
    })
    .map((x) => {
      for (const i of newGrades) {
        if (x.id === i.studentId) {
          x.grade = i.grade;
        }
      }
      return x;
    });
}

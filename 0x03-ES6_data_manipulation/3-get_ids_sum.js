export default function getStudentIdsSum(studentArray) {
  return studentArray.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
}

export default function createReportObject(employeesList) {
  return {
  allEmployees: {
    ...employeesList,
  },
  getNumberOfDepartments() {
    let departmentCount = 0;
    for (const i in employeesList) {
      departmentCount += 1;
    }
    return departmentCount;
  },
  }
}

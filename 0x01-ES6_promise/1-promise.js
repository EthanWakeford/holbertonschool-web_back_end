export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, rejects) => {
    if (success === true) {
      resolve({
        status: 200,
        body: 'Success',
      });
    } else {
      rejects(Error('The fake API is not working currently'));
    }
  });
}

export default function uploadPhoto(filename) {
  return new Promise((rejects) => {
    rejects(Error(`${filename} cannot be processed`));
  });
}

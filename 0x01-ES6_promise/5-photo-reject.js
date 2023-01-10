export default function uploadPhoto(filename) {
  return new Promise((resolve, rejects) => {
    rejects(Error(`${filename} cannot be processed`));
  });
}

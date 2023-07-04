const kue = require("kue");
const queue = kue.createQueue();

const job = queue
  .create("push_notification_code", {
    phoneNumber: '1234',
    message: 'hello',
  })
  .save();

job
  .on("enqueue", () => {
    console.log(`Notification job created: ${job.id}`);
  })
  .on("complete", () => {
    console.log("Notification job completed");
  })
  .on("failed", () => {
    console.log("Notification job failed");
  });

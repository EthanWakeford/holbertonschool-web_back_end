import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
  console.log("Redis client not connected to the server:", err)
);

console.log("Redis client connected to the server");

function setSchools(key, value) {
  client.hset("HolbertonSchools", key, value, print);
}

function getSchools() {
  client.hgetall("HolbertonSchools", (err, obj) => {
    if (err) {
      console.log(err);
    } else {
      console.log(obj);
    }
  });
}

setSchools("Portland", "50");
setSchools("Seattle", "80");
setSchools("New York", "20");
setSchools("Bogota", "20");
setSchools("Cali", "40");
setSchools("Paris", "2");

getSchools();

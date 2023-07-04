import { createClient, print } from "redis";
import { promisify } from "util";

const client = createClient();

client.on("error", (err) =>
  console.log("Redis client not connected to the server:", err)
);

console.log("Redis client connected to the server");

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, print);
}

// const displaySchoolValue = promisify(client.get(schoolName, print)).bind(schoolName);

const displaySchoolValue = async (schoolName) => {
  const display = promisify(client.get).bind(client);
  const result = await display(schoolName);
  console.log(result);
};

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

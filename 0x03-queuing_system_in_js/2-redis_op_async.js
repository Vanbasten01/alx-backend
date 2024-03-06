import { createClient } from "redis";
import { promisify } from "util";
import { util } from "chai";
const redis = require("redis");

const client = createClient().on("error", (err) =>
  console.log("Redis client not connected to the server:", err.message)
);
console.log("Redis client connected to the server");

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
}

const getAsync = promisify(client.get).bind(client)

const displaySchoolValue = (schoolName) => {
    getAsync(schoolName).then((res) => {
    console.log(res);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

client.quit()
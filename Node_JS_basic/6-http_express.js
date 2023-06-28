const express = require('express');

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/info', (req, res) => {
  res.json({ data: 'hello' });
});

app.listen(port, () => {
});

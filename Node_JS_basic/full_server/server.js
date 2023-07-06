const express = require('express');

const app = express();

const PORT = 1245;

app.listen(PORT, () => {
  console.log('express running on port', PORT);
});

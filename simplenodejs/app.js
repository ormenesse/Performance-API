
const express = require('express')
const app = express()
const port = 8000

app.get('/', async (req, res) => {
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms))
  await sleep(10000);
  res.send('Hello World!')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})
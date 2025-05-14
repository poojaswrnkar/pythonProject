const http = require('http');
const crypto = require('crypto');
const url = require('url');

const SECRET_KEY = "my-hardcoded-secret--------------for-test"; // Hardcoded secret

const server = http.createServer((req, res) => {
  const query = url.parse(req.url, true).query;
  
  // XSS vulnerability
  if (query.name) {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(`<h1>Hello, ${query.name}</h1>`);  // Unsanitized user input
  }

  // Insecure hashing algorithm
  const password = "user-password";
  const hash = crypto.createHash('md5').update(password).digest('hex');
  console.log("Password hash:", hash);

  // Dangerous use of eval
  if (query.code) {
    eval(query.code); // Code injection vulnerability
  }
});

server.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});

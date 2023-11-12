const http = require('http');

const host = 'localhost';
const port = 80;


const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    const ret_str = "Your IP address is " + res.socket.remoteAddress + " and your source port is " + res.socket.remotePort + ".";
    res.end(ret_str)
  });

server.listen(port, listen_callback);

function listen_callback(){
    console.log(`Server is running on http://localhost:${port}`)
}
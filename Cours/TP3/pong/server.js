const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const { Server } = require('socket.io');
const io = new Server(server);
const PORT = process.env.PORT || 5000

var gameOn = false;
var intervalId;

var player1 = { id: "",
		ready: false,
		y: 30,
		points: 0,
	      };
var player2 = { id: "",
		ready: false,
		y: 30,
		points: 0,
	      };

var leftThresh = 0;
var rightThresh = 0;
var leftPaddleThresh = 0;
var rightPaddleThresh = 0;
var upThresh = 0;
var downThresh = 0;

var width;
var height;
var ball = { deltaX : 5,
	     deltaY : 5,
	     pos : { x : 0, y : 0 },
	     dirX : 1,
	     dirY : 1,
	   };

function initBall () {
    ball.pos.x = width / 2;
    ball.pos.y = 10;
    ball.dirX = Math.random() * 2 - 1;
    // ball.dirX = -1;
    ball.dirY = 1;
}

function touchPaddle (player) {
    return ball.pos.y >= player.y-20 && ball.pos.y <= player.y + 20;
}

function moveBall () {
    ball.pos.x = ball.pos.x + ball.deltaX * ball.dirX;
    ball.pos.y = ball.pos.y + ball.deltaY * ball.dirY;

    if (ball.pos.y <= upThresh || ball.pos.y >= downThresh)
	ball.dirY = -ball.dirY;

    if (ball.pos.x <= leftPaddleThresh && touchPaddle(player1)
	|| ball.pos.x >= rightPaddleThresh && touchPaddle(player2))
	ball.dirX = -ball.dirX;

    else if (ball.pos.x <= leftThresh) {
	console.log("point for player 2");
	player2.points += 1;
	jsonMsg = { player : player2.id, score : player2.points };
	io.emit('score update', JSON.stringify(jsonMsg));
	initBall();
    }
    else if (ball.pos.x >= rightThresh) {
	console.log("point for player 1");
	player1.points += 1;
	jsonMsg = { player : player1.id, score : player1.points };
	io.emit('score update', JSON.stringify(jsonMsg));
	initBall();
    }

    io.emit('move ball', JSON.stringify(ball.pos));
}

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});
app.get('/style.css', (req, res) => {
    res.sendFile(__dirname + '/style.css');
});

// app.get("/view.js", (req, res) => {
//     res.sendFile(__dirname + '/view.js');
// });

io.on('connection', (socket) => {
    var msg;
    if (player1.id == "") {
	player1.id = socket.id;
	console.log("player 1 connected: "+socket.id);
	jsonMsg = { id: socket.id, status: "player1", j1: player1.id, j2: player2.id };
	msg = JSON.stringify(jsonMsg);
    } else if (player2.id == "") {
    	player2.id = socket.id;
    	console.log("player 2 connected: "+socket.id);
	jsonMsg = { id: socket.id, status: "player2", j1: player1.id, j2: player2.id };
	msg = JSON.stringify(jsonMsg);
    } else {
    	console.log("viewer connected");
	jsonMsg = { id: socket.id, status: "viewer", j1: player1.id, j2: player2.id };
	msg = JSON.stringify(jsonMsg);
    }
    io.emit('status', msg);

    socket.conn.on("close", (_) => {
	var is1 = socket.id == player1.id;
	var is2 = socket.id == player2.id;
	if (is1 || is2) {
	    console.log("stopping the game");
	    gameOn = false;
	    clearInterval(intervalId);
	    player1.points = 0;
	    player2.points = 0;
	    if (is1) {
		console.log("player 1 disconnected");
		player1.id = "";
		player1.ready = false;
	    }
	    else {
		console.log("player 2 disconnected");
		player2.id = "";
		player2.ready = false;
	    }
	    jsonMsg = { id: socket.id, status: "plop", j1: player1.id, j2: player2.id };
	    io.emit('status', JSON.stringify(jsonMsg));
	}
    });

    socket.on('dimensions', (jsonMsg) => {
	msg = JSON.parse(jsonMsg);
	width = msg.width;
	height = msg.height;
	console.log("canvas: "+width+"x"+height);
	leftThresh = 5;
	rightThresh = width - 5;
	leftPaddleThresh = 10;
	rightPaddleThresh = width - 10;
	upThresh = 5;
	downThresh = height - 5;
    });

    socket.on('ready', (_) => {
	if (socket.id == player1.id) {
	    player1.ready = true;
	    console.log("player 1 is ready");
	}
	else if (socket.id == player2.id) {
	    player2.ready = true;
	    console.log("player 2 is ready");
	}
	if (player1.ready && player2.ready) {
	    console.log("let's start!");
	    gameOn = true;
	    if (width == 0 || height == 0) {
		console.log("problem");
	    }
	    initBall();
	    io.emit('move ball', JSON.stringify(ball.pos));
	    intervalId = setInterval(moveBall, 50);
	}
    });

    socket.on('moved paddle', (y) => {
	if (gameOn) {
	    if (socket.id == player1.id)
		player1.y = y;
	    else if (socket.id == player2.id)
		player2.y = y;
	    jsonMsg = JSON.stringify({ id: socket.id, pos: y });
	    io.emit('move paddle', jsonMsg);
	}
    });
});


server.listen(PORT, () => {
  console.log(`listening on *: ${ PORT }`);
});

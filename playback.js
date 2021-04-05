var playCounter = 0;
var clipArray = [];

var $video1 = $("#video1");
var $video2 = $("#video2");
var $video3 = $("#video3");

$video1.attr("src", "/Videos/vid1-homepage.mp4");
// $video2.attr("src", "https://www.youtube.com/watch?v=pFnI8q7q_5E");
// $video3.attr("src", "https://www.youtube.com/watch?v=pFnI8q7q_5E");

// $("#video1").html('<source src="/Video/vid1-homepage.mp4" type="video/mp4"></source>' );
$("#video1").attr('src', "vid1.mp4");

var timerID;

var $canvas = $("#myCanvas");
var ctx = $canvas[0].getContext("2d");

function stopTimer() {
  window.clearInterval(timerID);
}

$('#startPlayback').click(function() {
  stopTimer();
  playCounter = $('#playbackNum').val();
  clipArray = [];

  // addd element to the end of the array
  clipArray.push(1);
  for (var i = 0; i < playCounter; i++) {
    clipArray.push(2);
  }
  clipArray.push(3);

  $video2[0].load();
  $video3[0].load();

  $video1[0].play();
});

function drawImage(video) {
  //last 2 params are video width and height
  ctx.drawImage(video, 0, 0, 640, 360);
}

// copy the 1st video frame to canvas as soon as it is loaded
$video1.one("loadeddata", function() {
  drawImage($video1[0]);
});

// copy video frame to canvas every 30 milliseconds
$video1.on("play", function() {
  timerID = window.setInterval(function() {
    drawImage($video1[0]);
  }, 30);
});
$video2.on("play", function() {
  timerID = window.setInterval(function() {
    drawImage($video2[0]);
  }, 30);
});
$video3.on("play", function() {
  timerID = window.setInterval(function() {
    drawImage($video3[0]);
  }, 30);
});

function onVideoEnd() {
  //stop copying frames to canvas for the current video element
  stopTimer();

  // remove 1st element of the array
  clipArray.shift();

  //IE fix
  if (!this.paused) this.pause();

  if (clipArray.length > 0) {
    if (clipArray[0] === 1) {
      $video1[0].play();
    }
    if (clipArray[0] === 2) {
      $video2[0].play();
    }
    if (clipArray[0] === 3) {
      $video3[0].play();
    }
  } else {
    // in case of last video, make sure to load 1st video so that it would start from the 1st frame 
    $video1[0].load();
  }
}

$video1.on("ended", onVideoEnd);
$video2.on("ended", onVideoEnd);
$video3.on("ended", onVideoEnd);
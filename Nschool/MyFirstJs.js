
// var myBirthTime = new Date(1995, 12, 29, 12, 30);
// function updateParagraph() {
//   var now = new Date();
//   var seconds = (now.getTime() - myBirthTime.getTime()) / 1000;
// //   getidしたHTMLのid要素をもつ箇所にこの文字列を設定するための記述
//   document.getElementById('birth-time').innerText =
//     '生まれてから' + seconds + '秒経過。';
// }
// setInterval(updateParagraph, 50);
// // setInterval → 指定された関数を指定されたミリ秒ごとに繰り返し実行するもの

var game = {
    startTime : null,
    displayArea: document.getElementById('display-area')
}

function start() {
  game.startTime = Date.now();
  document.body.onkeydown = stop;
}

function stop() {
  var currentTime = Date.now();
  var seconds = (currentTime - game.startTime) / 1000;
  if (9.5 <= seconds && seconds <= 10.5) {
    game.displayArea.innerText = seconds + '秒でした。すごい。';
  } else {
    game.displayArea.innerText = seconds + '秒でした。残念。';
  }
}
if (confirm('OKを押して10秒だと思ったら何かキーを押して下さい')) {
  start();
}

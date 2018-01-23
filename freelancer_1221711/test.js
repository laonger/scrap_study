
var url = 'https://www.portalinmobiliario.com/venta/departamento/santiago-metropolitana/6289-edificio-2-santo-domingo-1450-nva?tp=2&op=1&iug=434&ca=3&pd=2500&ts=1&sd=60&sh=100&dd=2&dh=4&bd=1&bh=3&mn=2&or=&sf=1&sp=1&at=0&i=6';

var page = require('webpage').create();

page.open(url, function(status) {
    page.render('test.png');
    phantom.exit();
});

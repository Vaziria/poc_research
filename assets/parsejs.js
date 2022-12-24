function parse_2(arg) { // o0qO00
    var hasil = [];
    
    hasil['push'](arg >> 24 & 255, arg >> 16 & 255, arg >> 8 & 255, 255 & arg);

    return hasil;
}


function parse_1(arg) { // o0qqQQ
    var hasil = [];
    
    hasil['push'](arg >> 8 & 255, 255 & arg)

    return hasil;
}

function encode_1(arg1, arg2) {
    var hasil;
    switch (arg1) {
    case 88:
        hasil = function(arg3) {
            var hasil = [];
            return hasil['push'](255 & arg3),
            hasil;
        }(arg2);

        break;
    case 105:
        hasil = parse_1(arg2);
        break;
    case 7:
        hasil = parse_2(arg2);
        break;
    case 77:
        hasil = function(arg3) {
            var hasil = 4294967296
              , cc = arg3 / hasil | 0
              , counter = arg3 - cc * hasil;
            return parse_2(cc).concat(parse_2(counter));
        }(arg2);
    }
    return hasil;
}


function encode_2(arg) { // o0qO0o
    
    for (var hasil = [], counter = 0; counter < arg['length']; )
        hasil['push'](255 & arg['charCodeAt'](counter)),
        counter++;
    return hasil;

}

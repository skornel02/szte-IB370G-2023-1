var f = r => { a = r.ertek; for(var n of r.gyerekek) { a += f(n)}; return a; }
var faOsszeg = f;
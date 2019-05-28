var v000 = 0;
var v001 = 0;
var v010 = 0;
var v011 = 0;
var v100 = 0;
var v101 = 0;
var v110 = 0;
var v111 = 0;
for (i = 0; i < 1024; i++){
    num = Math.floor(Math.random() * 8)
    if (num == 0){
        v000++;
    }
    if (num == 1){
        v001++
    }
    if (num == 2){
        v010++
    }
    if (num == 3){
        v011++
    }
    if (num == 4){
        v100++
    }
    if (num == 5){
        v101++
    }
    if (num == 6){
        v110++
    }
    if (num == 7){
        v111++
    }
}
var v000perc = (v000*100)/1024;
var v001perc = (v001*100)/1024;
var v010perc = (v010*100)/1024;
var v011perc = (v011*100)/1024;
var v100perc = (v100*100)/1024;
var v101perc = (v101*100)/1024;
var v110perc = (v110*100)/1024;
var v111perc = (v111*100)/1024;

console.log("000: " + v000perc + "%");
console.log("001: " + v001perc + "%");
console.log("010: " + v010perc + "%");
console.log("011: " + v011perc + "%");
console.log("100: " + v100perc + "%");
console.log("101: " + v101perc + "%");
console.log("110: " + v110perc + "%");
console.log("111: " + v111perc + "%");
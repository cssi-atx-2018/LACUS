let region = document.getElementById('reg');
let state = document.getElementById('st');
let mintemp = document.getElementById('min');
let maxtemp = document.getElementById('max');
let region_submit = document.getElementById('regsub');

let useravg = (mintemp + maxtemp)/2;
let regvag = 69.95;
let stavg = 69.9;

region_submit.addEventListener('click', function(){
  document.getElementById('useravg').innerHTML = 'Your average temperature is ' + useravg + '.';
  document.getElementById('regionavg').innerHTML = 'The average temperature for the ' + region + ' region is this.';
  document.getElementById('regionavg').innerHTML = 'The average temperature for ' + state + ' is this.';
  if(useravg < stavg){
    let diff = (stavg-useravg);
    document.getElementById('compavg').innerHTML = 'Your average is ' + diff + ' degrees cooler than the state average.';
  }
  else if(useravg > stavg){
    let diff = (useravg-stavg);
    document.getElementById('compavg').innerHTML = 'Your average is ' + diff + ' degrees warmer than the state average.';
  }
  else{
    document.getElementById('compavg').innerHTML = 'Your average is equal to the state average.';
  }
})

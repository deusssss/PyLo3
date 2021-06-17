function mouseOver(button) {
  switch (button) {
    case "prova":
      document.getElementById("div1").innerHTML = "carica gli esempi di sequenze FASTA presenti nella cartella principale!";
      break;
    case "carica":
      document.getElementById("div1").innerHTML = "carica gli sequenze FASTA dal tuo pc!";
      break;
    case "entrez":
      document.getElementById("div1").innerHTML = "carica gli sequenze FASTA da NCBI attraverso accession number!";
      break;
    }
  document.getElementById('div1').style.visibility='visible';
}

function mouseOut() {
document.getElementById('div1').style.visibility='hidden';
}

function clickButton(button){
  exit();
  switch (button) {
    case "prova":
      document.getElementById('div2').style.visibility='visible';
      break;
    case "carica":
      document.getElementById('div3').style.visibility='visible';
      break;
    case "entrez":
      document.getElementById('div4').style.visibility='visible';
      break;
    }
}

function exit(){

  document.getElementById('div2').style.visibility='hidden';
  document.getElementById('div3').style.visibility='hidden';
  document.getElementById('div4').style.visibility='hidden';

}

function loading(){

  document.getElementById("square").src = "res/gifs/".concat(Math.floor(Math.random() * 19)).concat(".gif");
  document.getElementById("audio").play();
}

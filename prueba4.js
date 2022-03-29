class Rectangulo{
  constructor () {
      this.alto = 5; 
      this.ancho = 6;
      this.carro = new Carro();
  }

  calcArea () {
  }
}

class Artefactos{
  constructor(){
    this.artefacto1 = 1
    this.artefacto2 = 2
  }        

  apagar(){
  }
}        

class Carro extends Artefactos{
  constructor () {
      this.alto = 1; 
      this.ancho = 2;
  }  
  encender () {
  }
}

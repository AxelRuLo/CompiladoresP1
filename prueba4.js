class Rectangulo{
    constructor (alto, ancho) {
        this.alto = alto; 
        this.ancho = ancho;
        this.carro = Carro();
    }

    _12calcArea_ () {
      return this.alto * this.ancho;
    }
 }

class Artefactos{
    constructor(artefacto1, artefacto2){
      this.artefacto1 = artefacto1
      this.artefacto2 = artefacto2
    }        
  
    apagar(){
      console.log('apagado')
    }
}        

class Carro extends Artefactos{
    constructor (alto, ancho) {
        this.alto = alto; 
        this.ancho = ancho;
    }  
    encender () {
        console.log('encender');
    }
  }

class Nyuszi {
  /**
   * 
   * @param {number} repa 
   */
  constructor(repa = 0) {
    this._repa = repa;
    /**
     * @type {string[]}
     */
    this.vendegek = [];
  }

  get repa() {
    return this._repa;
  }

  set repa(repa) {    
    this.repa = repa;
  }

  ultet(db = 1) {
    this._repa += db;
  }

  vendeg(vendeg) {
    if (typeof vendeg === "string") {
      this.vendegek.push(vendeg);
    }
  }

  etet() {
    while (this.repa > 0 && this.vendegek.length > 0) {
      this._repa--;
      this.vendegek = [...this.vendegek.slice(1)];
    }
  }
}

// nincs répája Nyuszinak.
var nyusz = new Nyuszi(0);
//ültet egy répát.
nyusz.ultet(1);
console.log(nyusz.repa); // 1.
console.log(nyusz.vendegek); //még nincs vendége az eredmény [].
nyusz.vendeg('Robert Gida'); // Róbert Gida megérkezik Nyuszihoz.
nyusz.vendeg('Malacka'); // Malacka megérkezik Nyuszihoz.
console.log(nyusz.vendegek); ['Robert Gida', 'Malacka']
nyusz.etet(); // Mivel van egy 1 répa, Robert Gida kap egyet és utána haza megy.
// Malackának már nem jutott répa, ezért neki várnia kell.
console.log(nyusz.repa) // 0
console.log(nyusz.vendegek); // ['Malacka']
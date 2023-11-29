
/**
 * 
 * @param {number[]} t 
 * @returns 
 */
const hungi = (t) => {
  if (t === undefined) {
    return 0;
  }


  if (t.length < 10) {
    return "Tul kevesen jottek a buliba";
  }

  if (t.length % 2 !== 0) {
    return "A bulizok kozott biztos van egy szingli";
  }

  const sum = t.reduce((acc, val) => acc + val, 0);
  const avg = sum / t.length;

  return t.filter(val => val > avg).reverse();
};

console.log(hungi([33333,300,2589,990,3780]));
console.log(hungi([3333,300,258,9,990,3780,3333,300,2589,990,3780]));
console.log(hungi([3333,300,2589,990,3780,3333,300,2589,990,3780]));
console.log(hungi());


class Remszarvas {

  /**
   * 
   * @param {string} nev 
   * @param {number} remisztoseg 
   */
  constructor(nev, remisztoseg = 33) {
    this.nev = nev;
    /**
     * @type {string[]}
     */
    this.tulajdonsagok = [];
    this.remisztoseg = remisztoseg;
  }

  get nev() {
    return this._nev;
  }

  set nev(nev) {
    if (typeof nev === "string" && nev.length >= 4) {
      this._nev = nev;
    } else {
      this._nev = "Krampi";
    }
  }
  
  fejleszt(nev) {
    if (typeof nev !== "string") {
      this.tulajdonsagok = [];
    } else if (!nev.includes(" ")) {
      this.tulajdonsagok.push(nev);
    } else {
      this.tulajdonsagok = [nev, ...this.tulajdonsagok];
    }
  }

  rosszindulat() {
    if (this.tulajdonsagok.length === 0) {
      return 0;
    }

    return this.tulajdonsagok.reduce((acc, tulaj)=> acc + tulaj.length, 0) / this.tulajdonsagok.length;
  }

  info(){
    return `${this.nev} rémszarvasunk ${this.remisztoseg} rémisztőséggel rendelkezik. Tulajdonságai: ${this.tulajdonsagok.join(" ")}`;
  }

  remiszt() {
    this.remisztoseg += 5;
    return this.remisztoseg > 50;
  }
}



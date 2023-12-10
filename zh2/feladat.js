/**
 * 
 * @param {number[] | undefined}  tomb 
 */
const advent = (tomb) => {
   if (tomb === undefined) {
    return -1;
   }

   if (tomb.length < 4) {
    return "Nincs eleg gyertya!"; 
   } 
   if (tomb.length % 4 != 0) {
    return "Nincsen eleg gyertya egesz szamu koszoruhoz!";
   }

   const total = tomb.reduce((sum, curr) => sum + curr);
   const avg = total / tomb.length;

   const result = [];
   for (let elem of tomb) {
    if (elem > avg) {
      result.push(elem);
    }
   }
   return result;
}; 

console.log(advent([10,2]));
console.log(advent([20,58,8,9,9]));
console.log(advent([300,2589,990,3780,3333,300,2589,990]));
console.log(advent(undefined));


class ForraltBor {
  /**
   * 
   * @param {string} nev 
   * @param {number} hofok 
   */
  constructor(nev, hofok = 40) {
    this.nev = nev;
    this.hofok = hofok;
    /**
     * @type {string[]}
     */
    this.hozzavalok = [];
  }

  get nev() {
    return this._nev;
  }

  set nev(val) {
    if (typeof val === "string" && val.length >= 5) {
      this._nev = val;
    } else {
      this._nev = "Krampampuli";
    }
  }

  hozzaad(val) {
    if (typeof val !== "string") {
      this.hozzavalok = [];
      return;
    }

    if (val.includes(" ")) {
      this.hozzavalok = [val, ...this.hozzavalok];
    } else {
      this.hozzavalok.push(val);
    }
  }

  /**
   * 
   * @returns {string}
   */
  szlogen() {
    if (this.hozzavalok.length === 0) {
      return this.nev;
    }

    let max = this.hozzavalok[0];

    for (let elem of this.hozzavalok) {
      if (elem.length > max.length) {
        max = elem;
      }
    }

    return max;
  }

  info() {
    return `${this.nev} borunk ${this.hofok} celsius fokos. Tartalmaz: ${this.hozzavalok.join("; ")}`;
  }

  alkoholos() {
    return this.hofok < 80;
  }
}

const test = new ForraltBor();

test.hozzaad("asd");
test.hozzaad("asdasdsadsa");
test.hozzaad("asd");
test.hozzaad("asd");

console.log(test.hozzavalok)
console.log(test.szlogen());
const tokeletes = (num) => {
    if (typeof num !== "number") {
        return false;
    }

    const divisors = [];
    for (let i = 1; i < ((num / 2) + 1); i++) {
        if (num % i === 0) {
            divisors.push(i);
        }
    }

    const sum = divisors.reduce((a, b) => a + b, 0);
    return sum === num;
}

console.log(tokeletes(6)) // true
console.log(tokeletes(28)) // true
console.log(tokeletes(16)) // false
console.log(tokeletes("szoveg")) // false

/**
 * @property {string[]} lapok
 * @property {number} memory
 * @property {number} memoryUsage
 */
class Webbongeszo {
    constructor(memory = 8192) {
        this.lapok = [];
        this.memory = memory;
        this.memoryUsage = 0;
    }

    get memoriafogyasztas() {
        return this.memoryUsage;
    }

    set memoriafogyasztas(value) {
        this.memoryUsage = Math.max(Math.min(value, this.memory), 0);
    }

    ujLap(url) {
        const random = Math.floor(Math.random() * 11);;
        const memoryUsage = random * 140 + 10;

        this.lapok.push(url);
        this.memoriafogyasztas = this.memoriafogyasztas + memoryUsage;
    }

    lapBezar() {
        if (this.lapok.length === 0) {
            return;
        }

        const random = Math.floor(Math.random() * 11);
        const memoryUsage = 97 * random + 30;

        this.lapok.pop();
        this.memoriafogyasztas = this.memoriafogyasztas - memoryUsage;
    }

    panik() {
        this.lapok = [];
        this.memoriafogyasztas = 10;
    }
}
function clear(array) {
    const result = [];
    if (array === undefined || !Array.isArray(array)) {
        return 0;
    }

    const reversed = [...array].reverse();
    reversed.forEach((element) => {
        if (typeof element === "string" && element.length >= 1) {
            result.push(element.substring(0, 2).toUpperCase());
        } else if (typeof element === "number") {
            result.push(element);
        }
    });

    return result;
}

console.log(clear([2,5,3,'heyho',null,7]))
console.log(clear([undefined]))
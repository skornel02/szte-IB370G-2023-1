function matek(abc) {
  if (abc === undefined) {
    return 0;
  }

  if (typeof abc === "string") {
    return 1;
  }

  if (Number.isInteger(abc)) {
    const asd = Number(abc);
    if (asd % 2 === 0) {
      return Math.pow(asd, asd);
    } else {
      return Math.pow(asd - 1, 2);
    }
  }

  return null;
}

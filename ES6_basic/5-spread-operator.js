export default function concatArrays(array1, array2, string) {
  const concatenatedArrays = array1.concat(array2);

  const concatenatedString = [];
  for (let i = 0; i < string.length; i++) {
    concatenatedString.push(string[i]);
  }

  return concatenatedArrays.concat(concatenatedString);
}

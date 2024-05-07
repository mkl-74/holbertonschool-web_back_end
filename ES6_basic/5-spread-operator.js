export default function concatArrays(array1, array2, string) {
  const concatenatedString = [...string];
  return [...array1, ...array2, ...concatenatedString];
}

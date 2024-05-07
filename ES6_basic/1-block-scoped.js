export default function taskBlock(trueOrFalse) {
  // Variable const
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // Variable const
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}

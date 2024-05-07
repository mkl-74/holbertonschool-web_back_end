export default function taskBlock(trueOrFalse) {
    //Variable let
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
        //
        task = true;
        task2 = false;
    }
  
    return [task, task2];
  }
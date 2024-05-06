export default function taskBlock(trueOrFalse) {
    //constante modifiable
    let task = false;
    let task2 = true;
  
    if (trueOrFalse) {
        //constante non modifiable
        task = true;
        task2 = false;
    }
  
    return [task, task2];
  }
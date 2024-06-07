// Array in javascript are just obj with integer based Keys, that act like index

class MyArray {
  constructor() {
    // lenght/key counter
    this.length = 0;
    // data model to store strings
    this.data = {};
  }
  get(index) {
    return this.data[index];
  }
  push(item) {
    // add item to dict data model
    this.data[this.length] = item;
    // increase key/length
    this.length++;
    // return dict data model if they wanna print()
    return this.data;
  }
  pop() {
    const lastItem = this.data[this.length - 1];
    // delete last item from dict data model using key
    delete this.data[this.length - 1];
    // decrement key/length value
    this.length--;
    // return last item, if they wanna print()
    return lastItem;
  }
  deleteAtIndex(index) {
    // get the item by key
    const item = this.data[index];
    // perform shifting operation
    this.shiftItems(index);
    // return item, if they wanna print()
    return item;
  }
  shiftItems(index) {
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    console.log(this.data[this.length - 1]);
    // delete last item to declutter
    delete this.data[this.length - 1];
    // decrement lenght/key value
    this.length--;
  }
}

const myArray = new MyArray();
myArray.push("hi");
myArray.push("you");
myArray.push("!");
myArray.pop();
myArray.deleteAtIndex(0);
myArray.push("are");
myArray.push("nice");
myArray.shiftItems(0);
console.log(myArray);

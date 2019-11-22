


let add = document.getElementById("add");

let input = document.getElementById("input");
let input_value = input.value;

function addItem() {
  let li = document.createElement("li");
  let checkbox = document.createElement("input");
  checkbox.setAttribute("type", "checkbox");
  li.appendChild(checkbox);
  let todoList = document.getElementById("todo-list");
  todoList.appendChild(li);
}



add.onclick = () => addItem();

function addItem(e) {
  console.log(e)
  // create the <li>
  let li = document.createElement("li");
  // create and append <input type="checkbox" /> with event listener attached
  let checkbox = document.createElement("input");
  checkbox.setAttribute("type", "checkbox");
  checkbox.addEventListener("click", completeItem);
  li.appendChild(checkbox);
  // create and append <span class="todo-text">{value}</span>
  let span = document.createElement("span");
  span.className = "todo-text";
  let input_value = document.getElementById("input").value;
  let clear_value = document.getElementById("input");
  clear_value.value = "";
  span.innerText = input_value;
  li.appendChild(span);
  // create and append <i class="far fa-trash-alt"></i> with event listener attached
  let i = document.createElement("i");
  i.className = "far fa-trash-alt";
  i.addEventListener("click", function(e) {
    console.log(e);
    this.parentNode.remove();
  })
  li.append(i);
  // target <ul id="todo-list"> and append all of the children
  let todoList = document.getElementById("todo-list");
  todoList.appendChild(li);
}

function keyPress(e) {
  if (e.which === 13) {
    addItem(e);
    e.preventDefault();
  }
}

function removeItem(e) {
  console.log(e);
  this.parentNode.removeItem();
}

function completeItem(e) {
  console.log(e);
  let completedText = this.parentNode.innerText;
  this.parentNode.remove();
  // create the <li>
  let li = document.createElement("li");
  // create and append <input type="checkbox" /> with event listener attached
  let checkbox = document.createElement("input");
  checkbox.setAttribute("type", "checkbox");
  checkbox.setAttribute("checked", "checked");
  li.appendChild(checkbox);
  // create and append <span class="todo-text">{value}</span>
  let span = document.createElement("span");
  span.classList.add("todo-text", "completed-text");
  span.innerText = completedText;
  li.appendChild(span);
  // create and append <i class="far fa-trash-alt"></i> with event listener attached
  let i = document.createElement("i");
  i.className = "far fa-trash-alt";
  i.addEventListener("click", function(e) {
    console.log(e);
    this.parentNode.remove();
  })
  li.append(i);
  // target <ul id="todo-list"> and append all of the children
  let todoList = document.getElementById("todo-list");
  todoList.appendChild(li);
}

// add the item via click on add button or enter press
let add = document.getElementById("add");
add.addEventListener("click", addItem);
let input = document.getElementById("input");
input.addEventListener("keydown", keyPress);


const api = "http://127.0.0.1:5000/api/menu";

function loadMenu(){
fetch(api)
.then(res => res.json())
.then(data => {
const list = document.getElementById("menu");
list.innerHTML = "";
data.forEach(item => {
list.innerHTML += `
<li>
${item.name} - ₹${item.price}
<button onclick="deleteItem(${item.id})">Delete</button>
</li>
`;
});
});
}

function addItem(){
const name = document.getElementById("name").value;
const price = document.getElementById("price").value;

fetch(api, {
method:"POST",
headers:{"Content-Type":"application/json"},
body: JSON.stringify({name, price})
}).then(loadMenu);
}

function deleteItem(id){
fetch(api+"/"+id, {method:"DELETE"})
.then(loadMenu);
}

loadMenu();

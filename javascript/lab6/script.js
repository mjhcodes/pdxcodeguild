// initializes the map on the "mapid" div with a given center (lat, lng) and zoom
const mymap = L.map('mapid').setView([0, 0], 2);

// loads and displays tile layers on the map - attribution required!
L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox/streets-v11',
    accessToken: ''
}).addTo(mymap);

// obtains JSON data for ten users, stores in a new array and runs function
const users = [];
axios({
  method: "get",
  baseURL: "https://jsonplaceholder.typicode.com/",
  url: "users/",
})
  .then(response => {
    for (let i in response.data) {
      users.push(response.data[i]);
  }
    placeMarkers(users);
    postData(users);
  })
  .catch(error => console.log(error))


// extracts data from each user and adds markers to map based on data
function placeMarkers(users) {
  console.log(users);
  for (let i = 0; i < users.length; i++) {
    let name = users[i].name;
    let city = users[i].address.city;
    let lat = users[i].address.geo.lat;
    let lng = users[i].address.geo.lng;
    let marker = L.marker([lat, lng]).addTo(mymap);
    marker.bindPopup(`<b>${name}</b><br>${city}`).openPopup();
  }
}
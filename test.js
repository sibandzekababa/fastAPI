const apiKey = "pk.d8715ec73d99936a78f359b691297c3d";const apiKey = "pk.d8715ec73d99936a78f359b691297c3d";
const url = `https://locationiq.com{apiKey}&q=Nairobi&format=json`;

fetch(url)
  .then(response => {
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    return response.json();
  })
  .then(data => {
    console.log("✅ Connection Successful! Target Latitude:", 
const url = `https://locationiq.com{apiKey}&q=Nairobi&format=json`;

fetch(url)
  .then(response => {
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    return response.json();
  })
  .then(data => {
    console.log("✅ Connection Successful! Target Latitude:", data[0].lat);
  })

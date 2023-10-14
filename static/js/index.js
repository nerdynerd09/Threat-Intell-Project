socket = io();
socket.connect('http://127.0.0.1:5000/');

socket.on('connect', function() {
    socket.send('a')
})


socket.on('checkentity', function(data) {
    const result = data['dbResult'];

    const resultDiv = document.getElementById("result-text");
    if (result === 'Malicious IP') {
        resultDiv.style.color = 'red';
    } else {
        resultDiv.style.color = '#01ff01';
    }
    resultDiv.innerText = result;
})

function checkentity() {
    const value = document.getElementById("search-box").value;
    // console.log(value)
    // console.log("I amhere")
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/checkentity", true);

    // Send the proper header information along with the request
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");


    xhr.send(`q=${value}`);



}
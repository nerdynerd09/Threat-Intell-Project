socket.on('connect', function() {
    socket.send('a')
})


socket.on('checkentity', function(data) {
    const result = data['dbResult'];

    document.getElementById("result-ul-list").innerHTML += `<li><p>Database</p><p>${result}</p></li>`;

})

socket.on('checkvtip', function(data) {
    const result = data['vtResult'];

    const resultDiv = document.getElementById("result-ul-list");
    resultDiv.innerHTML += `<li><p>Virustotal</p><p>${result}</p></li>`

})

socket.on('checkksipresult', function(data) {
    const result = data['ipResult'];
    const resultDiv = document.getElementById("result-ul-list");
    resultDiv.innerHTML += `<li><p>Kaspersky</p><p>${result["Status"]}</p></li>`

})

socket.on('checkhoneydbipresult', function(data) {
    const result = data['ipResult'];
    document.getElementById("result-ul-list").innerHTML += `<li><p>HoneyDB</p><p>${result}</p></li>`;

})
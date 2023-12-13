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
    console.log("KS Result: ", result)
    const resultDiv = document.getElementById("result-ul-list");
    resultDiv.innerHTML += `<li><p>Kaspersky</p><p>${result["Status"]}</p></li>`

})

socket.on('checkhoneydbipresult', function(data) {
    const result = data['ipResult'];
    document.getElementById("result-ul-list").innerHTML += `<li><p>HoneyDB</p><p>${result}</p></li>`;

})

socket.on('checkabusedbipresult', function(data) {
    const result = data['ipResult'];

    if (result > 10) {
        document.getElementById("result-ul-list").innerHTML += `<li><p>Abuse IP DB</p><p>Malicious</p></li>`;
    } else {
        document.getElementById("result-ul-list").innerHTML += `<li><p>Abuse IP DB</p><p>Safe</p></li>`;
    }

})


socket.on('checkvthash', function(data) {
    // console.log("I am here")
    const result = data['vtResult'];
    console.log(result)

    document.getElementById("result-ul-list").innerHTML += `<li><p>Virustotal</p><p>${result["Status"]}</p></li>`;

})

socket.on('checkkshash', function(data) {
    console.log("Kaspersky is here")
    const result = data['ksResult'];
    console.log(result)

    if (result["Detection Names"] != "") {
        document.getElementById("ks-result-text").innerHTML = `<li>Zone: ${result['Zone']}</li><li>Detection Names: ${result['Detection Names']}</li>`;
    } else {
        document.getElementById("ks-result-text").innerHTML = `<li>${result['Zone']}</li>`;
    }



})

socket.on('checkHashValue', function(data) {
    const result = data['dbResult'];

    document.getElementById("result-ul-list").innerHTML += `<li><p>Database</p><p>${result}</p></li>`;

})
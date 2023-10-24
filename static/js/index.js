document.getElementsByClassName('tab').item(0).click();

fileInput.addEventListener('change', function() {
    const fileInput = document.getElementById('fileInput');
    const fileChosen = document.getElementById('fileInput-label');

    fileChosen.textContent = this.files[0].name

})



socket = io();
socket.connect('http://127.0.0.1:5000/');

socket.on('connect', function() {
    socket.send('a')
})


socket.on('checkentity', function(data) {
    const result = data['dbResult'];

    const resultDiv = document.getElementById("db-result-text");
    if (result === 'Malicious IP') {
        resultDiv.style.color = 'red';
    } else {
        resultDiv.style.color = '#01ff01';
    }
    resultDiv.innerText = result;
})

socket.on('checkvtip', function(data) {
    console.log("I am here")
    const result = data['vtResult'];
    console.log(result)

    Object.entries(result).forEach(([key, value]) => {
        const ulElement = document.getElementById("vt-result-text")
        const liElement = document.createElement("li");
        const nameElement = document.createElement("p");
        const valueElement = document.createElement("p");

        nameElement.textContent = `${key.toUpperCase()}`;
        valueElement.textContent = ` ${value}`;
        // liElement.textContent = `${key.toUpperCase()} ${value}`;
        liElement.append(nameElement);
        liElement.append(valueElement);
        ulElement.append(liElement)
    });


})

function checkentity() {

    const value = document.getElementById("search-box").value;
    document.getElementById("vt-result-text").innerHTML = "";
    document.getElementById("db-result-text").innerHTML = "";
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // Step 5: Handle the response
            var response = xhr.responseText;
            console.log(response);
        }
    };

    xhr.open("GET", `http://127.0.0.1:5000/checkentity?ip=${value}`, true);
    xhr.send();


    var xhr2 = new XMLHttpRequest();
    xhr2.onreadystatechange = function() {
        if (xhr2.readyState === 4 && xhr2.status === 200) {
            // Step 5: Handle the response
            var response = xhr2.responseText;
            console.log(response);
        }
    };

    xhr2.open("GET", `http://127.0.0.1:5000/checkvtip?ip=${value}`, true);
    xhr2.send();


}

function uploadFile() {

    // event.preventDefault();
    var fileInput = document.getElementById("fileInput");
    var xhr = new XMLHttpRequest();
    var formData = new FormData();
    formData.append("file", fileInput.files[0]);
    const uploadFileName = fileInput.files[0].name;

    xhr.open("POST", "/fileUpload", true);
    xhr.setRequestHeader("enctype", "multipart/form-data");

    document.getElementById("progress-wrapper").style.display = "block";
    // document.getElementById("file-wrapper").style.display = "none";

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                document.getElementById("response").innerHTML = "File uploaded successfully.";
                var xhrGet = new XMLHttpRequest();
                xhrGet.open("GET", `/checkFile?fileName=${uploadFileName}`, true)
                xhrGet.send()
            } else {
                document.getElementById("response").innerHTML = "File upload failed.";
            }
        }
    };

    xhr.upload.onprogress = function(event) {
        var progress = (event.loaded / event.total) * 100;
        console.log(progress);
        document.getElementById("progress").style.width = `${progress}%`;
        document.getElementById("progress").innerText = `${Math.floor(progress)}%`;

    };


    xhr.send(formData);

}


function showTab(tabIndex) {
    var tabContents = document.querySelectorAll('.tab-content');
    var tabs = document.querySelectorAll('.tab');
    for (var i = 0; i < tabContents.length; i++) {
        tabContents[i].style.display = 'none';
        tabs[i].style.backgroundColor = '#ccc';
    }

    tabContents[tabIndex - 1].style.display = 'flex';
    tabs[tabIndex - 1].style.backgroundColor = '#fff';
    // tabContents[tabIndex - 1].style.backgroundColor = "white"
}
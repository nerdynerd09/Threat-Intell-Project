document.getElementsByClassName('tab').item(0).click();

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

function uploadFile() {

    // event.preventDefault();
    var fileInput = document.getElementById("fileInput");
    var xhr = new XMLHttpRequest();
    var formData = new FormData();
    formData.append("file", fileInput.files[0]);
    const uploadFileName = fileInput.files[0].name;

    xhr.open("POST", "/fileUpload", true);
    xhr.setRequestHeader("enctype", "multipart/form-data");

    // document.getElementById("progress-wrapper").style.display = "block";
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
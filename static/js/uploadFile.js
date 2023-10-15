function uploadFile() {
    // event.preventDefault();
    var fileInput = document.getElementById("fileInput");
    var xhr = new XMLHttpRequest();
    var formData = new FormData();
    formData.append("file", fileInput.files[0]);
    let uploadFileName = fileInput.files[0].name;

    xhr.open("POST", "/fileUpload", true);
    xhr.setRequestHeader("enctype", "multipart/form-data");


    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                document.getElementById("response").innerHTML = "File uploaded successfully.";
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
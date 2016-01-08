var regexp = /\w{2,}/;

function checkName() {
    var tag = document.getElementById("form_email_name");
    var parent = tag.parentNode;
    if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
        var error = document.createElement("h5");
        error.innerHTML = "Inserisci Nome &#47; Societ&agrave;";
		error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
        parent.removeChild(parent.children[2]);
    }
}

function checkEmail() {
    var tag = document.getElementById("form_email_mail");
    var parent = tag.parentNode;
    if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
        var error = document.createElement("h5");
        error.innerHTML = "Inserisci la tua email";
		error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (tag.value.search(regexp) != -1 && tag.value.search("@") == -1) {
        if (parent.children.length == 3)
            parent.removeChild(parent.children[2]);
        var error = document.createElement("h5");
        error.innerHTML = "Email inserita non valida";
		error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
        parent.removeChild(parent.children[2]);
    }
}

function checkMex() {
    var tag = document.getElementById("form_email_mex");
    var parent = tag.parentNode;
    if (parent.children.length == 2 && tag.value.search(regexp) == -1) {
        var error = document.createElement("h5");
        error.innerHTML = "Inserisci un messaggio";
		error.className = "mail_form_error";
        parent.appendChild(error);
    } else if (parent.children.length == 3 && tag.value.search(regexp) != -1) {
        parent.removeChild(parent.children[2]);
    }
}
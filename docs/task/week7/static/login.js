function clickRegistrationBtn(e) {
    let username = document.querySelector("#registrationForm input[name=username]").value;
    
    if (!!!username) {
        alert('註冊帳號請填帳號');
        // the conditions were not met, so call preventDefault to 
        // stop the browsers default behavior of submitting the form
        e.preventDefault();
        e.stopPropagation();
    }

    let name = document.querySelector("#registrationForm input[name=name]").value;
    
    if (!!!name) {
        alert('註冊帳號請填姓名');
        e.preventDefault();
        e.stopPropagation();
    }

    let password = document.querySelector("#registrationForm input[name=password]").value;
    
    if (!!!password) {
        alert('註冊帳號請填密碼');
        e.preventDefault();
        e.stopPropagation();
    }
}

document.getElementById("registrationBtn").addEventListener("click", clickRegistrationBtn)


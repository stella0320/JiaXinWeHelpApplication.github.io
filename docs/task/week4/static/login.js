
function clickLoginBtn(e) {
    const agreement = document.querySelector("input[name=aggreement]").checked;
    if (!!!agreement) {
        alert('Please check the checkbox first');
        // the conditions were not met, so call preventDefault to 
        // stop the browsers default behavior of submitting the form
        e.preventDefault();
        e.stopPropagation();
    }
}

document.getElementById("loginBtn").addEventListener("click", clickLoginBtn)
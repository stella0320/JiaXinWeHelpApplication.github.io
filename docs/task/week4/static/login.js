
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



function clickCaculateBtn(e) {
    const number = document.querySelector("input[name=number]").value;
    if (isNaN(number) || number <= 0) {
        alert("Please enter a positive number");
        // the conditions were not met, so call preventDefault to 
        // stop the browsers default behavior of submitting the form
        e.preventDefault();
        e.stopPropagation();
    } else {
        location.href = 'http://127.0.0.1:3000/square/'+ number
    }
}

document.getElementById("calculateBtn").addEventListener("click", clickCaculateBtn)
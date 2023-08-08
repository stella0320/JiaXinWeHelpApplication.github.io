
function clickDeleteMessage(e) {
    
    let confirmMessage = confirm('Are you sure to delete message？');
    
    if (confirmMessage) {
        const messageId = e.dataset.id;
        const xhttp = new XMLHttpRequest();
        xhttp.onload = function() {
            location.href = 'http://127.0.0.1:3000/member';
        }
        xhttp.open("POST", "/deleteMessage");
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("messageId=" + messageId);
    }
    
}
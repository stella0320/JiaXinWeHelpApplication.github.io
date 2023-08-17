
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

function clickQueryUsernameBtn() {
    let username = document.getElementById("queryUsername").value;
    fetch('http://127.0.0.1:3000/api/member?username=' + username, {
        method:'GET'
    })
    .then(res => {
        return res.json();
    }).then(data => {
        let user = data['data'];
        let userDisplayName = '';
        if(!!user) {
            userDisplayName = user['name'] + "(" + user['username']  + ")"
        }
        const queryUsernameResult = document.getElementById("queryUsernameResult");
        queryUsernameResult.innerHTML = userDisplayName;
    });
}

document.getElementById("queryUsernameBtn").addEventListener("click", clickQueryUsernameBtn)


function clickUpdateUserBtn() {
    let newName = document.getElementById("newName").value;
    fetch('http://127.0.0.1:3000/api/member', {
        method:'PATCH',
        body: JSON.stringify({
            name : newName
        }),
        headers: {
            'Content-type': 'application/json;',
        }
    })
    .then(res => {
        return res.json();
    }).then(data => {
        console.log(Object.keys(data));
        const result = Object.keys(data)[0];

        if('ok' === result) {
            document.getElementById("updateNameResult").innerHTML = "更新成功"
        }
    });
}

document.getElementById("updateNameBtn").addEventListener("click", clickUpdateUserBtn)

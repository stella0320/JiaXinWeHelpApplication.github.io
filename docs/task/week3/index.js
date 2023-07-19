let createMainItem1 = function(picUrl, tableText) {
    const mainItem2 = document.createElement('div');
    mainItem2.classList.add('main-item-1');

    const itemImage = document.createElement('div');
    itemImage.classList.add('item-1-img');

    // 處理圖片Div
    const itemImageImg = document.createElement('img');
    itemImageImg.classList.add('dog-1');
    itemImageImg.src = picUrl;
    itemImage.append(itemImageImg);
    mainItem2.appendChild(itemImage);
    
    // 處理文字Div
    const itemText = document.createElement('div');
    itemText.classList.add('item-1-text');
    const itemTextTxt = document.createElement('div');
    itemTextTxt.classList.add('promotion');
    // 塞標題文字
    let txt = document.createTextNode(tableText);
    itemTextTxt.appendChild(txt);
    itemText.appendChild(itemTextTxt);
    mainItem2.appendChild(itemText);
    
    let container = document.getElementsByClassName('main-contain-1')[0];
    container.appendChild(mainItem2);
}


let createMainItem2 = function(picUrl, tableText) {
    const mainItem2 = document.createElement('div');
    mainItem2.classList.add('main-item-2');

    const itemImage = document.createElement('div');
    itemImage.classList.add('item-2-img');

    // 處理圖片Div
    const itemImageImg = document.createElement('img');
    itemImageImg.classList.add('dog-2');
    itemImageImg.src = picUrl;
    itemImage.append(itemImageImg);
    mainItem2.appendChild(itemImage);
    
    // 處理文字Div
    const itemText = document.createElement('div');
    itemText.classList.add('item-2-text');
    const itemTextTxt = document.createElement('div');
    itemTextTxt.classList.add('table-text');
    
    // 塞標題文字
    let txt = document.createTextNode(tableText);
    itemTextTxt.appendChild(txt);
    itemText.appendChild(itemTextTxt);
    mainItem2.appendChild(itemText);
    
    let container = document.getElementsByClassName('main-contain-2')[0];
    container.appendChild(mainItem2);
}


let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

let appendMainTable1 = function(data) {
    for (let i = 0; i < 3; i++) {
        let imagUrl = data[i]['file'];
        let imageIndex = imagUrl.indexOf("https://www.travel.taipei/",10);
        let url = imagUrl.slice(0, imageIndex);
        createMainItem1(url, data[i]['stitle']);
    }
}


let appendMainTable2 = function(initIndex, data) {
    for (let i=initIndex; i < initIndex + 12; i++) {
        let txt = data[i]['stitle'];
        let imagUrl = data[i]['file'];
        let imageIndex = imagUrl.indexOf("https://www.travel.taipei/",10);
        let url = imagUrl.slice(0, imageIndex);
        createMainItem2(url, txt);
    }
}

let handleUrlResponse = async function (response) {
    let data = await response.json();
    if(response.status === 200){
        let results = data['result']['results'];
        // 前三張處理
        appendMainTable1(results);

        let initIndex = 3;
        // 後面處理
        appendMainTable2(initIndex, results);
    }else{
     // Rest of status codes (400,500,303), can be handled here appropriately
    }

}

fetch(url)
      .then(handleUrlResponse)
      .catch((err) => {
          console.log(err);
      })


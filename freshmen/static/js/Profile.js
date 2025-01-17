function loadFile(input) {
  var file = chooseFile.files[0];
  console.log(chooseFile.files);

  var newImage = document.createElement("img");
  newImage.setAttribute("class", "img");

  newImage.src = URL.createObjectURL(file);

  newImage.style.width = "130px";
  newImage.style.height = "130px";
  newImage.style.borderRadius = "50%";
  newImage.style.position = "absolute";

  var button = document.getElementById("chooseFile_button");
  button.style.visibility = "hidden";

  var container = document.getElementById("profile_background");
  newImage.remove();
  container.appendChild(newImage);
}

function setThumbnail(event) {
  var reader = new FileReader();
  var container = document.querySelector("div#image_container");

  reader.onload = function (event) {
    var img = document.createElement("img");
    img.setAttribute("src", event.target.result);

    while (container.hasChildNodes()) {
      //자식 요소가 있는지 확인-false가 될때까지 반복
      container.removeChild(container.firstChild); // 첫번째 자식 요소를 삭제
    }

    container.appendChild(img);
    img.style.width = "130px";
  };

  reader.readAsDataURL(event.target.files[0]);
}
function input_click() {
  document.querySelector("#timetable").click();
}

function Save() {
  var input = document.getElementsByClassName("inputbox");
  for (var i = 0; i < input.length; i++) {
    var item = input.item(i);
    item.readOnly = true;
  }
  var save_button = document.getElementById("save_button");
  if (save_button.innerText == "저장") {
    save_button.innerText = "편집";
    var input = document.getElementsByClassName("inputbox");
    for (var i = 0; i < input.length; i++) {
      var item = input.item(i);
      item.readOnly = true;
    }
    var share_button = document.getElementById("share_button");
    share_button.style.visibility = "visible";
  } else {
    save_button.innerText = "저장";
    var input = document.getElementsByClassName("inputbox");
    for (var i = 0; i < input.length; i++) {
      var item = input.item(i);
      item.readOnly = false;
    }
    var share_button = document.getElementById("share_button");
    share_button.style.visibility = "hidden";
  }
}

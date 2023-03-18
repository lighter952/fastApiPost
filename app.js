let xhr = new XMLHttpRequest();
xhr.open("POST", "http://127.0.0.1:8000/");
xhr.setRequestHeader("Accept", "multipart/form-data;");
xhr.setRequestHeader("Content-Type", "Content-Type: application/json");

let data = {
  "username": "78912",
  "password": "Jason Sweet"
};

xhr.send(data);

//let data = `[
//  "name": "string",
//  "description": "string",
//  "price": 0,
//  "tax": 0
//]`;
//fetch(
//  'http://127.0.0.1:8000/items/',
//  {
//    method: 'POST',
//    headers: {
//      'Content-Type': 'application/x-www-form-urlencoded'
//    },
//    body: data
//  }
//)
//.then(resp => resp.text())
//.then(console.log)
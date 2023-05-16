const data = fetch("http://127.0.0.1:5000/video/1")
  .then((res) => res.json())
  .then((data) => console.log(data));

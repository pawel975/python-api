const putDataBtn = document.querySelector(".put-data-btn");
const getDataBtn = document.querySelector(".get-data-btn");

putDataBtn.addEventListener("click", () => {
  const dataToPut = {
    id: 5,
    name: "johnyy",
    views: 5,
    likes: 5,
  };

  fetch(`http://127.0.0.1:5000/video/${Math.floor(Math.random() * 1000)}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(dataToPut),
  })
    .then((res) => res.json())
    .then((data) => console.log(data));
});

getDataBtn.addEventListener("click", () => {
  fetch("http://127.0.0.1:5000/videos", {
    method: "GET",
  })
    .then((res) => res.json())
    .then((data) => console.log(data));
});

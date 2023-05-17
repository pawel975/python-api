const registerForm = document.querySelector(".register__form");

registerForm.addEventListener("submit", () => {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  const registerData = {
    username,
    password,
  };

  fetch(`http://127.0.0.1:5000/user/${Math.floor(Math.random() * 1000)}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(registerData),
  })
    .then((res) => res.json())
    .then((data) => console.log(data));
});

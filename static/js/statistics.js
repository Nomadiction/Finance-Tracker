const data = JSON.parse(localStorage.getItem("transactions")) || [];
const dataContainer = document.getElementById("dataContainer");

if (data.length > 0) {
  let html = "<ul>";

  data.forEach(transaction => {
    html += `
                   <li>
                       <strong>ID:</strong> ${transaction.id}<br>
                       <strong>Название:</strong> ${transaction.name}<br>
                       <strong>Сумма:</strong> ${transaction.amount}<br>
                       <strong>Дата:</strong> ${transaction.date}<br>
                       <strong>Тип:</strong> ${transaction.type}<br><br>
                   </li>
               `;
  });

  html += "</ul>";
  dataContainer.innerHTML = html;
} else {
  dataContainer.textContent = "Нет данных в LocalStorage.";
}
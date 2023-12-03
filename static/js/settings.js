// Пример данных (замените данными из вашего менеджера)
const expenseData = {
    labels: ["Категория 1", "Категория 2", "Категория 3"],
    datasets: [{
      label: "Расходы",
      data: [500, 300, 700],
      backgroundColor: ["red", "orange", "blue"],
    }],
  };
  
  const incomeData = {
    labels: ["Январь", "Февраль", "Март"],
    datasets: [{
      label: "Доходы",
      data: [1000, 800, 1200],
      backgroundColor: ["green", "purple", "yellow"],
    }],
  };
  
  // Создание графика расходов
  const expenseCtx = document.getElementById("expenseChart").getContext("2d");
  const expenseChart = new Chart(expenseCtx, {
    type: "bar",
    data: expenseData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  });
  
  // Создание графика доходов
  const incomeCtx = document.getElementById("incomeChart").getContext("2d");
  const incomeChart = new Chart(incomeCtx, {
    type: "line",
    data: incomeData,
    options: {
      responsive: true,
      maintainAspectRatio: false,
    },
  });
  
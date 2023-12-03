// JavaScript для скрытия/отображения нижнего меню при прокрутке
let lastScrollY = window.scrollY;

window.addEventListener("scroll", () => {
  const currentScrollY = window.scrollY;
  const nav = document.querySelector(".bottom-navigation");

  if (currentScrollY > lastScrollY) {
    // Прокрутка вниз
    nav.classList.add("hide");
  } else {
    // Прокрутка вверх
    nav.classList.remove("hide");
  }

  lastScrollY = currentScrollY;
});

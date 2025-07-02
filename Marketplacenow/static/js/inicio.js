// Scroll efecto en navbar
const navbar = document.getElementById("navbar");
if (navbar) {
  window.addEventListener("scroll", function () {
    if (window.scrollY > 10) {
      navbar.classList.add("scrolled");
    } else {
      navbar.classList.remove("scrolled");
    }
  });
}

// Carrusel
const slides = document.querySelectorAll('.carousel-container img');
const nextBtn = document.getElementById('next');
const prevBtn = document.getElementById('prev');
let current = 0;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.style.opacity = i === index ? '1' : '0';
  });
}

// Solo si existen botones y al menos un slide
if (slides.length > 0 && nextBtn && prevBtn) {
  nextBtn.addEventListener('click', () => {
    current = (current + 1) % slides.length;
    showSlide(current);
  });

  prevBtn.addEventListener('click', () => {
    current = (current - 1 + slides.length) % slides.length;
    showSlide(current);
  });

  // Iniciar carrusel automático
  setInterval(() => {
    current = (current + 1) % slides.length;
    showSlide(current);
  }, 5000);

  // Mostrar el primer slide al cargar
  showSlide(current);
}

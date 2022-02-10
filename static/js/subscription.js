const radio = document.getElementsByClassName("plan");

const quaterly = document.getElementById("quaterly");

const hf = document.getElementById("hf");

const monthly = document.getElementById("monthly");

const rate_civil = document.getElementById("rates_civil");
const rate_criminal = document.getElementById("rates_criminal");
const rate_service = document.getElementById("rates_service");
const rate_tax = document.getElementById("rates_tax");
const rate_cor = document.getElementById("rates_cor");

// VARIABLE TO GET THE PRICES OF MONTHS

cv_monthly = rate_civil.textContent;
cr_monthly = rate_criminal.textContent;
tx_monthly = rate_tax.textContent;
sv_monthly = rate_service.textContent;
crp_monthly = rate_cor.textContent;
cv_quaterly = document.getElementById("cvq").value;
cv_hf = document.getElementById("cvh").value;
cr_quaterly = document.getElementById("crq").value;
cr_hf = document.getElementById("crh").value;
tx_quaterly = document.getElementById("txq").value;
tx_hf = document.getElementById("txh").value;
sv_qauterly = document.getElementById("svq").value;
sv_hf = document.getElementById("svh").value;
crp_quaterly = document.getElementById("crpq").value;
crp_hf = document.getElementById("crph").value;

// END VARIABLE TO GET THE PRICES OF MONTHS

monthly.checked = true;

for (i = 0; i < radio.length; i++) {
  radio[i].addEventListener("click", () => {
    if (quaterly.checked) {
      //For quaterly
      rate_civil.textContent = cv_quaterly;
      rate_criminal.textContent = cr_quaterly;
      rate_service.textContent = sv_qauterly;
      rate_tax.textContent = tx_quaterly;
      rate_cor.textContent = crp_quaterly;
    } else if (hf.checked) {
      //For half_yearly
      rate_civil.textContent = cv_hf;
      rate_criminal.textContent = cr_hf;
      rate_service.textContent = sv_hf;
      rate_tax.textContent = tx_hf;
      rate_cor.textContent = crp_hf;
    } else {
      //For monthly
      rate_civil.textContent = cv_monthly;
      rate_criminal.textContent = cr_monthly;
      rate_service.textContent = sv_monthly;
      rate_tax.textContent = tx_monthly;
      rate_cor.textContent = crp_monthly;
    }
  });
}

var swiper = new Swiper(".mySwiper", {
  effect: "coverflow",
  grabCursor: true,
  centeredSlides: true,
  slidesPerView: "auto",
  coverflowEffect: {
    rotate: 3,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true,
  },
  // loop: true,
});

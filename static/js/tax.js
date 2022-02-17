var taxSubLawType = document.getElementsByClassName("tax-sub-law-type");

var taxSubLawInput = document.querySelectorAll("input[name='tax-sublaw']");

var taxCourt = document.getElementsByClassName("tax-court");

var taxCourtInput = document.querySelectorAll("input[name='tax-court']");

var taxCategory = document.getElementsByClassName("tax-category");

var taxCategoryInput = document.querySelectorAll("input[name='tax-category']");

var openTaxCourtList = document.getElementById("crt-trib-court");

var openTaxTribunalList = document.getElementById("crt-trib-tribunal");

const taxcourtToggle = document.querySelector(".tax-court-ul");

const taxTibunalToggle = document.querySelector(".tax-tribunal-ul");

const taxCategoryToggle = document.querySelector(".tax-category-ul");

// const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

var taxSubLawTypeVal = [];

var taxCourtval = [];

var taxCategoryval = [];

//  FOR TOGGLING THE COURT AND TRIBUNAL LISTS
openTaxCourtList.addEventListener("click", () => {
  var visibility = taxcourtToggle.getAttribute("data-taxcourtvisilble");

  if (visibility === "false") {
    taxcourtToggle.setAttribute("data-taxcourtvisilble", true);
    openTaxCourtList.classList.add("tax-btn-active");
    openTaxTribunalList.classList.remove("tax-btn-active");
    taxTibunalToggle.setAttribute("data-taxtribunalvisilble", false);
  } else {
    taxcourtToggle.setAttribute("data-taxcourtvisilble", false);
    openTaxCourtList.classList.remove("tax-btn-active");
  }
});

openTaxTribunalList.addEventListener("click", () => {
  var visibility = taxTibunalToggle.getAttribute("data-taxtribunalvisilble");

  if (visibility === "false") {
    taxTibunalToggle.setAttribute("data-taxtribunalvisilble", true);
    openTaxTribunalList.classList.add("tax-btn-active");
    openTaxCourtList.classList.remove("tax-btn-active");
    taxcourtToggle.setAttribute("data-taxcourtvisilble", false);
  } else {
    taxTibunalToggle.setAttribute("data-taxtribunalvisilble", false);
    openTaxTribunalList.classList.remove("tax-btn-active");
  }
});

// END  FOR TOGGLING THE COURT AND TRIBUNAL LISTS

// for constant query
for (i = 0; i < taxSubLawType.length; i++) {
  taxSubLawType[i].addEventListener("click", () => {
    for (j = 0; j < taxSubLawInput.length; j++) {
      if (taxSubLawInput[j].checked) {
        taxSubLawTypeVal.push(taxSubLawInput[j].value);
        console.log(taxSubLawTypeVal);
      }
    }
  });
}

for (i = 0; i < taxCourt.length; i++) {
  taxCourt[i].addEventListener("click", () => {
    var visibility = taxCategoryToggle.getAttribute("data-taxcategoryvisible");

    if (visibility === "false") {
      taxCategoryToggle.setAttribute("data-taxcategoryvisible", true);
    }
    for (j = 0; j < taxCourtInput.length; j++) {
      if (taxCourtInput[j].checked) {
        taxCourtval.push(taxCourtInput[j].value);
        console.log(taxCourtval);
      }
    }
  });
}

for (i = 0; i < taxCategory.length; i++) {
  taxCategory[i].addEventListener("click", () => {
    for (j = 0; j < taxCategoryInput.length; j++) {
      if (taxCategoryInput[j].checked) {
        taxCategoryval.push(taxCategoryInput[j].value);
        console.log(taxCategoryval);
      }
    }
  });
}

for (i = 0; i < taxCategory.length; i++) {
  taxCategory[i].addEventListener("click", (e) => {
    e.preventDefault();
    taxsubLawType = taxSubLawTypeVal;
    taxcourt = taxCourtval;
    taxCategory = taxCategoryval;
    console.log("this is from ajax : ", taxsubLawType, taxcourt, taxCategory);
    $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin", // Do not send CSRF token to another domain.
      url: "taxation",
      data: {
        "taxsubLawType[]": taxSubLawTypeVal,
        "taxcourt[]": taxCourtval,
        "taxCategory[]": taxCategoryval,
      },
      success: function (response) {
        // console.log(response.result);
        taxQResult(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
}

function taxQResult(response) {
  taxData = response.result;
  if (response.status == "success") {
    $("#taxqueryResult").empty();
    for (i = 0; i < taxData.length; i++) {
      $("#taxqueryResult").append(
        `
              <a class="tax-title" href="/professional/detail-doc/${
                taxData[i].id
              }">${i + 1}.&nbsp ${
          taxData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="tax-headnote">${taxData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if");
    $("#taxqueryResult").empty();
    $("#taxqueryResult").append(
      `
              <p class="no-citation-found">No citations found...</p>
            `
    );
  } else {
    // console.log("entered the else");
    $("#taxqueryResult").empty();
    $("#taxqueryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}
// end for constant querying
// FOR ADDING THE ACTIVE CLASS IN LABEL

// var labels = document.getElementsByTagName("label");

var taxSubLawlabels = document.getElementsByClassName("tax-sub-law-type-label");

var taxCourtlabels = document.getElementsByClassName("tax-tax-court-label");

var taxCategorylabels = document.getElementsByClassName(
  "tax-law-category-label"
);

for (let i = 0; i < taxSubLawlabels.length; i++) {
  taxSubLawlabels[i].addEventListener("click", taxSublawaddclass);
}

for (let i = 0; i < taxCourtlabels.length; i++) {
  taxCourtlabels[i].addEventListener("click", taxCourtaddclass);
}

for (let i = 0; i < taxCategorylabels.length; i++) {
  taxCategorylabels[i].addEventListener("click", taxCategoryaddclass);
}

function taxSublawaddclass(event) {
  let active = document.getElementsByClassName("tax-sub-law-type-label");

  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("tax-active");
  }
  for (i = 0; i < taxCourtlabels.length; i++) {
    taxCourtlabels[i].classList.remove("tax-active");
  }
  for (i = 0; i < taxCategorylabels.length; i++) {
    taxCategorylabels[i].classList.remove("tax-active");
  }
  event.target.classList.add("tax-active");
}

function taxCourtaddclass(event) {
  let active = document.getElementsByClassName("tax-tax-court-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("tax-active");
  }
  for (i = 0; i < taxCategorylabels.length; i++) {
    taxCategorylabels[i].classList.remove("tax-active");
  }
  event.target.classList.add("tax-active");
}

function taxCategoryaddclass(event) {
  let active = document.getElementsByClassName("tax-law-category-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("tax-active");
  }
  event.target.classList.add("tax-active");
}
// END FOR ADDIING ACTIVE CLASS IN LABEL

// SEARCH FORM AJAX CALLS
$(document).on("submit", "#tax_search_form", function (e) {
  e.preventDefault();
  var taxq = $("#tax_search").val();

  // ajax call

  $.ajax({
    type: "GET",
    // headers: { "X-CSRFToken": csrftoken },
    // mode: "same-origin",
    url: "taxSearch",
    data: {
      q: taxq,
    },
    success: function (response) {
      //   console.log(response.result);
      taxSearchResult(response);
    },
    error: function (error) {
      console.log(error);
    },
  });
});

function taxSearchResult(response) {
  taxData = response.result;
  if (response.status == "success") {
    $("#taxqueryResult").empty();
    for (i = 0; i < taxData.length; i++) {
      $("#taxqueryResult").append(
        `
              <a class="tax-title" href="/professional/detail-doc/${
                taxData[i].id
              }">${i + 1}.&nbsp ${
          taxData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="tax-headnote">${taxData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if of no success");
    $("#taxqueryResult").empty();
    $("#taxqueryResult").append(
      `
              <p class="no-citation-found">No citations found for "${taxData}"</p>
              <p class="no-citation-found">Please Check the spelling or else try searching with a different word.</p>
            `
    );
  } else if (response.status == "empty") {
    // console.log("entered the else if empty");
    $("#taxqueryResult").empty();
    $("#taxqueryResult").append(
      `
              <p class="no-citation-found">You searched nothing...</p>
            `
    );
  } else {
    console.log("entered the else");
    $("#taxqueryResult").empty();
    $("#taxqueryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

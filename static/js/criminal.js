var criminalSubLawType = document.getElementsByClassName(
  "criminal-sub-law-type"
);

var criminalSubLawInput = document.querySelectorAll(
  "input[name='criminal-sublaw']"
);

var criminalCourt = document.getElementsByClassName("criminal-court");

var criminalCourtInput = document.querySelectorAll(
  "input[name='criminal-court']"
);

var criminalCategory = document.getElementsByClassName("criminal-category");

var criminalCategoryInput = document.querySelectorAll(
  "input[name='criminal-category']"
);

const criminalcourtToggle = document.querySelector(".criminal-court-ul");

const criminalCategoryToggle = document.querySelector(".criminal-category-ul");

// const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

var criminalSubLawTypeVal = [];

var criminalCourtval = [];

var criminalCategoryval = [];

// for constant query
for (i = 0; i < criminalSubLawType.length; i++) {
  criminalSubLawType[i].addEventListener("click", () => {
    var visibility = criminalcourtToggle.getAttribute(
      "data-criminalcourtvisilble"
    );

    if (visibility === "false") {
      criminalcourtToggle.setAttribute("data-criminalcourtvisilble", true);
    }

    for (j = 0; j < criminalSubLawInput.length; j++) {
      if (criminalSubLawInput[j].checked) {
        criminalSubLawTypeVal.push(criminalSubLawInput[j].value);
        // console.log(criminalSubLawTypeVal);
      }
    }
  });
}

for (i = 0; i < criminalCourt.length; i++) {
  criminalCourt[i].addEventListener("click", () => {
    var visibility = criminalCategoryToggle.getAttribute(
      "data-criminalcategoryvisible"
    );

    if (visibility === "false") {
      criminalCategoryToggle.setAttribute("data-criminalcategoryvisible", true);
    }
    for (j = 0; j < criminalCourtInput.length; j++) {
      if (criminalCourtInput[j].checked) {
        criminalCourtval.push(criminalCourtInput[j].value);
        // console.log(criminalCourtval);
      }
    }
  });
}

for (i = 0; i < criminalCategory.length; i++) {
  criminalCategory[i].addEventListener("click", () => {
    for (j = 0; j < criminalCategoryInput.length; j++) {
      if (criminalCategoryInput[j].checked) {
        criminalCategoryval.push(criminalCategoryInput[j].value);
        // console.log(criminalCategoryval);
      }
    }
  });
}

for (i = 0; i < criminalCategory.length; i++) {
  criminalCategory[i].addEventListener("click", (e) => {
    e.preventDefault();
    criminalsubLawType = criminalSubLawTypeVal;
    criminalcourt = criminalCourtval;
    criminalCategory = criminalCategoryval;
    console.log(
      "this is from ajax : ",
      criminalsubLawType,
      criminalcourt,
      criminalCategory
    );
    $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin", // Do not send CSRF token to another domain.
      url: "criminal",
      data: {
        "criminalsubLawType[]": criminalSubLawTypeVal,
        "criminalcourt[]": criminalCourtval,
        "criminalCategory[]": criminalCategoryval,
      },
      success: function (response) {
        // console.log(response.result);
        criminalQResult(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
}

function criminalQResult(response) {
  criminalData = response.result;
  if (response.status == "success") {
    $("#criminalqueryResult").empty();
    for (i = 0; i < criminalData.length; i++) {
      $("#criminalqueryResult").append(
        `
              <a class="criminal-title" href="/professional/detail-doc/${
                criminalData[i].id
              }">${i + 1}.&nbsp ${
          criminalData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="criminal-headnote">${criminalData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if");
    $("#criminalqueryResult").empty();
    $("#criminalqueryResult").append(
      `
              <p class="no-citation-found">No citations found...</p>
            `
    );
  } else {
    // console.log("entered the else");
    $("#criminalqueryResult").empty();
    $("#criminalqueryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

// end for constant querying

// FOR ADDING THE ACTIVE CLASS IN LABEL

// var labels = document.getElementsByTagName("label");

var criminalSubLawlabels = document.getElementsByClassName(
  "criminal-sub-law-type-label"
);

var criminalCourtlabels = document.getElementsByClassName(
  "criminal-criminal-court-label"
);

var criminalCategorylabels = document.getElementsByClassName(
  "criminal-law-category-label"
);

for (let i = 0; i < criminalSubLawlabels.length; i++) {
  criminalSubLawlabels[i].addEventListener("click", criminalSublawaddclass);
}

for (let i = 0; i < criminalCourtlabels.length; i++) {
  criminalCourtlabels[i].addEventListener("click", criminalCourtaddclass);
}

for (let i = 0; i < criminalCategorylabels.length; i++) {
  criminalCategorylabels[i].addEventListener("click", criminalCategoryaddclass);
}

function criminalSublawaddclass(event) {
  let active = document.getElementsByClassName("criminal-sub-law-type-label");

  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("criminal-active");
  }
  for (i = 0; i < criminalCourtlabels.length; i++) {
    criminalCourtlabels[i].classList.remove("criminal-active");
  }
  for (i = 0; i < criminalCategorylabels.length; i++) {
    criminalCategorylabels[i].classList.remove("criminal-active");
  }
  event.target.classList.add("criminal-active");
}

function criminalCourtaddclass(event) {
  let active = document.getElementsByClassName("criminal-criminal-court-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("criminal-active");
  }
  for (i = 0; i < criminalCategorylabels.length; i++) {
    criminalCategorylabels[i].classList.remove("criminal-active");
  }
  event.target.classList.add("criminal-active");
}

function criminalCategoryaddclass(event) {
  let active = document.getElementsByClassName("criminal-law-category-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("criminal-active");
  }
  event.target.classList.add("criminal-active");
}
// END FOR ADDIING ACTIVE CLASS IN LABEL

// SEARCH FORM AJAX CALLS
$(document).on("submit", "#criminal_search_form", function (e) {
  e.preventDefault();
  var criminalq = $("#criminal_search").val();

  // ajax call

  $.ajax({
    type: "GET",
    // headers: { "X-CSRFToken": csrftoken },
    // mode: "same-origin",
    url: "criminalSearch",
    data: {
      q: criminalq,
    },
    success: function (response) {
      // console.log(response.result);
      criminalSearchResult(response);
    },
    error: function (error) {
      console.log(error);
    },
  });
});

function criminalSearchResult(response) {
  criminalData = response.result;
  if (response.status == "success") {
    $("#criminalqueryResult").empty();
    for (i = 0; i < criminalData.length; i++) {
      $("#criminalqueryResult").append(
        `
              <a class="criminal-title" href="/professional/detail-doc/${
                criminalData[i].id
              }">${i + 1}.&nbsp ${
          criminalData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="criminal-headnote">${criminalData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if of no success");
    $("#criminalqueryResult").empty();
    $("#criminalqueryResult").append(
      `
              <p class="no-citation-found">No citations found for "${criminalData}"</p>
              <p class="no-citation-found">Please Check the spelling or else try searching with a different word.</p>
            `
    );
  } else if (response.status == "empty") {
    // console.log("entered the else if empty");
    $("#criminalqueryResult").empty();
    $("#criminalqueryResult").append(
      `
              <p class="no-citation-found">You searched nothing...</p>
            `
    );
  } else {
    console.log("entered the else");
    $("#criminalqueryResult").empty();
    $("#criminalqueryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

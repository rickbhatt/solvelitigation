var corporateSubLawType = document.getElementsByClassName(
  "corporate-sub-law-type"
);

var corporateSubLawInput = document.querySelectorAll(
  "input[name='corporate-sublaw']"
);

var corporateCourt = document.getElementsByClassName("corporate-court");

var corporateCourtInput = document.querySelectorAll(
  "input[name='corporate-court']"
);

var corporateCategory = document.getElementsByClassName("corporate-category");

var corporateCategoryInput = document.querySelectorAll(
  "input[name='corporate-category']"
);

const corporatecourtToggle = document.querySelector(".corporate-court-ul");

const corporateCategoryToggle = document.querySelector(
  ".corporate-category-ul"
);

var corporateSubLawTypeVal = [];

var corporateCourtval = [];

var corporateCategoryval = [];

// for constant query
for (i = 0; i < corporateSubLawType.length; i++) {
  corporateSubLawType[i].addEventListener("click", () => {
    var visibility = corporatecourtToggle.getAttribute(
      "data-corporatecourtvisilble"
    );

    if (visibility === "false") {
      corporatecourtToggle.setAttribute("data-corporatecourtvisilble", true);
    }

    for (j = 0; j < corporateSubLawInput.length; j++) {
      if (corporateSubLawInput[j].checked) {
        corporateSubLawTypeVal.push(corporateSubLawInput[j].value);
        // console.log(corporateSubLawTypeVal);
      }
    }
  });
}

for (i = 0; i < corporateCourt.length; i++) {
  corporateCourt[i].addEventListener("click", () => {
    var visibility = corporateCategoryToggle.getAttribute(
      "data-corporatecategoryvisible"
    );

    if (visibility === "false") {
      corporateCategoryToggle.setAttribute(
        "data-corporatecategoryvisible",
        true
      );
    }
    for (j = 0; j < corporateCourtInput.length; j++) {
      if (corporateCourtInput[j].checked) {
        corporateCourtval.push(corporateCourtInput[j].value);
        // console.log(corporateCourtval);
      }
    }
  });
}

for (i = 0; i < corporateCategory.length; i++) {
  corporateCategory[i].addEventListener("click", () => {
    for (j = 0; j < corporateCategoryInput.length; j++) {
      if (corporateCategoryInput[j].checked) {
        corporateCategoryval.push(corporateCategoryInput[j].value);
        // console.log(corporateCategoryval);
      }
    }
  });
}

for (i = 0; i < corporateCategory.length; i++) {
  corporateCategory[i].addEventListener("click", (e) => {
    e.preventDefault();
    corporatesubLawType = corporateSubLawTypeVal;
    corporatecourt = corporateCourtval;
    corporateCategory = corporateCategoryval;
    console.log(
      "this is from ajax : ",
      corporatesubLawType,
      corporatecourt,
      corporateCategory
    );
    $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin", // Do not send CSRF token to another domain.
      url: "corporate",
      data: {
        "corporatesubLawType[]": corporateSubLawTypeVal,
        "corporatecourt[]": corporateCourtval,
        "corporateCategory[]": corporateCategoryval,
      },
      success: function (response) {
        // console.log(response.result);
        corporateQResult(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
}

function corporateQResult(response) {
  corporateData = response.result;
  if (response.status == "success") {
    $("#corporatequeryResult").empty();
    for (i = 0; i < corporateData.length; i++) {
      $("#corporatequeryResult").append(
        `
              <a class="corporate-title" href="/professional/detail-doc/${
                corporateData[i].id
              }">${i + 1}.&nbsp ${
          corporateData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="corporate-headnote">${corporateData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if");
    $("#corporatequeryResult").empty();
    $("#corporatequeryResult").append(
      `
              <p class="no-citation-found">No citations found...</p>
            `
    );
  } else {
    // console.log("entered the else");
    $("#corporatequeryResult").empty();
    $("#corporatequeryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

// end for constant querying

// FOR ADDING THE ACTIVE CLASS IN LABEL

// var labels = document.getElementsByTagName("label");

var corporateSubLawlabels = document.getElementsByClassName(
  "corporate-sub-law-type-label"
);

var corporateCourtlabels = document.getElementsByClassName(
  "corporate-corporate-court-label"
);

var corporateCategorylabels = document.getElementsByClassName(
  "corporate-law-category-label"
);

for (let i = 0; i < corporateSubLawlabels.length; i++) {
  corporateSubLawlabels[i].addEventListener("click", corporateSublawaddclass);
}

for (let i = 0; i < corporateCourtlabels.length; i++) {
  corporateCourtlabels[i].addEventListener("click", corporateCourtaddclass);
}

for (let i = 0; i < corporateCategorylabels.length; i++) {
  corporateCategorylabels[i].addEventListener(
    "click",
    corporateCategoryaddclass
  );
}

function corporateSublawaddclass(event) {
  let active = document.getElementsByClassName("corporate-sub-law-type-label");

  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("corporate-active");
  }
  for (i = 0; i < corporateCourtlabels.length; i++) {
    corporateCourtlabels[i].classList.remove("corporate-active");
  }
  for (i = 0; i < corporateCategorylabels.length; i++) {
    corporateCategorylabels[i].classList.remove("corporate-active");
  }
  event.target.classList.add("corporate-active");
}

function corporateCourtaddclass(event) {
  let active = document.getElementsByClassName(
    "corporate-corporate-court-label"
  );
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("corporate-active");
  }
  for (i = 0; i < corporateCategorylabels.length; i++) {
    corporateCategorylabels[i].classList.remove("corporate-active");
  }
  event.target.classList.add("corporate-active");
}

function corporateCategoryaddclass(event) {
  let active = document.getElementsByClassName("corporate-law-category-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("corporate-active");
  }
  event.target.classList.add("corporate-active");
}
// END FOR ADDIING ACTIVE CLASS IN LABEL

// SEARCH FORM AJAX CALLS
$(document).on("submit", "#corporate_search_form", function (e) {
  e.preventDefault();
  var corporateq = $("#corporate_search").val();

  // ajax call

  $.ajax({
    type: "GET",
    // headers: { "X-CSRFToken": csrftoken },
    // mode: "same-origin",
    url: "corporateSearch",
    data: {
      q: corporateq,
    },
    success: function (response) {
      //   console.log(response.result);
      corporateSearchResult(response);
    },
    error: function (error) {
      console.log(error);
    },
  });
});

function corporateSearchResult(response) {
  corporateData = response.result;
  if (response.status == "success") {
    $("#corporatequeryResult").empty();
    for (i = 0; i < corporateData.length; i++) {
      $("#corporatequeryResult").append(
        `
              <a class="corporate-title" href="/professional/detail-doc/${
                corporateData[i].id
              }">${i + 1}.&nbsp ${
          corporateData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="corporate-headnote">${corporateData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if of no success");
    $("#corporatequeryResult").empty();
    $("#corporatequeryResult").append(
      `
              <p class="no-citation-found">No citations found for "${corporateData}"</p>
              <p class="no-citation-found">Please Check the spelling or else try searching with a different word.</p>
            `
    );
  } else if (response.status == "empty") {
    // console.log("entered the else if empty");
    $("#corporatequeryResult").empty();
    $("#corporatequeryResult").append(
      `
              <p class="no-citation-found">You searched nothing...</p>
            `
    );
  } else {
    console.log("entered the else");
    $("#corporatequeryResult").empty();
    $("#corporatequeryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}
//

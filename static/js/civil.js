var civilSubLawType = document.getElementsByClassName("civil-sub-law-type");

var civilSubLawInput = document.querySelectorAll("input[name='civil-sublaw']");

var civilCourt = document.getElementsByClassName("civil-court");

var civilCourtInput = document.querySelectorAll("input[name='civil-court']");

var civilCategory = document.getElementsByClassName("civil-category");

var civilCategoryInput = document.querySelectorAll(
  "input[name='civil-category']"
);

const courtToggle = document.querySelector(".civil-court-ul");

const civilCategoryToggle = document.querySelector(".civil-category-ul");

const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

var civilSubLawTypeVal = [];

var civilCourtval = [];

var civilCategoryval = [];

// for constant query
for (i = 0; i < civilSubLawType.length; i++) {
  civilSubLawType[i].addEventListener("click", () => {
    var visibility = courtToggle.getAttribute("data-courtvisilble");

    if (visibility === "false") {
      courtToggle.setAttribute("data-courtvisilble", true);
    }

    for (j = 0; j < civilSubLawInput.length; j++) {
      if (civilSubLawInput[j].checked) {
        civilSubLawTypeVal.push(civilSubLawInput[j].value);
        // console.log(civilSubLawTypeVal);
      }
    }
  });
}

for (i = 0; i < civilCourt.length; i++) {
  civilCourt[i].addEventListener("click", () => {
    var visibility = civilCategoryToggle.getAttribute("data-categoryvisible");

    if (visibility === "false") {
      civilCategoryToggle.setAttribute("data-categoryvisible", true);
    }
    for (j = 0; j < civilCourtInput.length; j++) {
      if (civilCourtInput[j].checked) {
        civilCourtval.push(civilCourtInput[j].value);
        // console.log(civilCourtval);
      }
    }
  });
}

for (i = 0; i < civilCategory.length; i++) {
  civilCategory[i].addEventListener("click", () => {
    for (j = 0; j < civilCategoryInput.length; j++) {
      if (civilCategoryInput[j].checked) {
        civilCategoryval.push(civilCategoryInput[j].value);
        // console.log(civilCategoryval);
      }
    }
  });
}

for (i = 0; i < civilCategory.length; i++) {
  civilCategory[i].addEventListener("click", (e) => {
    e.preventDefault();
    subLawType = civilSubLawTypeVal;
    civilcourt = civilCourtval;
    civilCategory = civilCategoryval;
    console.log("this is from ajax : ", subLawType, civilcourt, civilCategory);
    $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin", // Do not send CSRF token to another domain.
      url: "civil",
      data: {
        "subLawType[]": civilSubLawTypeVal,
        "civilcourt[]": civilCourtval,
        "civilCategory[]": civilCategoryval,
      },
      success: function (response) {
        // console.log(response.result);
        civilQResult(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
}

function civilQResult(response) {
  civilData = response.result;
  if (response.status == "success") {
    $("#civilqueryResult").empty();
    for (i = 0; i < civilData.length; i++) {
      $("#civilqueryResult").append(
        `
              <a class="civil-title" href="/professional/detail-doc/${
                civilData[i].id
              }">${i + 1}.&nbsp ${
          civilData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="civil-headnote">${civilData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if");
    $("#civilqueryResult").empty();
    $("#civilqueryResult").append(
      `
              <p class="no-citation-found">No citations found...</p>
            `
    );
  } else {
    // console.log("entered the else");
    $("#civilqueryResult").empty();
    $("#civilqueryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

// end for constant querying

// FOR ADDING THE ACTIVE CLASS IN LABEL

// var labels = document.getElementsByTagName("label");

var civilSubLawlabels = document.getElementsByClassName(
  "civil-sub-law-type-label"
);

var civilCourtlabels = document.getElementsByClassName(
  "civil-civil-court-label"
);

var civilCategorylabels = document.getElementsByClassName(
  "civil-law-category-label"
);

for (let i = 0; i < civilSubLawlabels.length; i++) {
  civilSubLawlabels[i].addEventListener("click", civilSublawaddclass);
}

for (let i = 0; i < civilCourtlabels.length; i++) {
  civilCourtlabels[i].addEventListener("click", civilCourtaddclass);
}

for (let i = 0; i < civilCategorylabels.length; i++) {
  civilCategorylabels[i].addEventListener("click", civilCategoryaddclass);
}

function civilSublawaddclass(event) {
  let active = document.getElementsByClassName("civil-sub-law-type-label");

  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("civil-active");
  }
  for (i = 0; i < civilCourtlabels.length; i++) {
    civilCourtlabels[i].classList.remove("civil-active");
  }
  for (i = 0; i < civilCategorylabels.length; i++) {
    civilCategorylabels[i].classList.remove("civil-active");
  }
  event.target.classList.add("civil-active");
}

function civilCourtaddclass(event) {
  let active = document.getElementsByClassName("civil-civil-court-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("civil-active");
  }
  for (i = 0; i < civilCategorylabels.length; i++) {
    civilCategorylabels[i].classList.remove("civil-active");
  }
  event.target.classList.add("civil-active");
}

function civilCategoryaddclass(event) {
  let active = document.getElementsByClassName("civil-law-category-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("civil-active");
  }
  event.target.classList.add("civil-active");
}
// END FOR ADDIING ACTIVE CLASS IN LABEL

// SEARCH FORM AJAX CALLS
$(document).on("submit", "#civil_search_form", function (e) {
  e.preventDefault();
  var civilq = $("#civil_search").val();

  // ajax call

  $.ajax({
    type: "GET",
    // headers: { "X-CSRFToken": csrftoken },
    // mode: "same-origin",
    url: "civilSearch",
    data: {
      q: civilq,
    },
    success: function (response) {
      // console.log(response.result);
      civilSearchResult(response);
    },
    error: function (error) {
      console.log(error);
    },
  });
});

function civilSearchResult(response) {
  civilData = response.result;
  if (response.status == "success") {
    $("#civilqueryResult").empty();
    for (i = 0; i < civilData.length; i++) {
      $("#civilqueryResult").append(
        `
              <a class="civil-title" href="/professional/detail-doc/${
                civilData[i].id
              }">${i + 1}.&nbsp ${
          civilData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="civil-headnote">${civilData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if of no success");
    $("#civilqueryResult").empty();
    $("#civilqueryResult").append(
      `
              <p class="no-citation-found">No citations found for "${civilData}"</p>
              <p class="no-citation-found">Please Check the spelling or else try searching with a different word.</p>
            `
    );
  } else if (response.status == "empty") {
    // console.log("entered the else if empty");
    $("#civilqueryResult").empty();
    $("#civilqueryResult").append(
      `
              <p class="no-citation-found">You searched nothing...</p>
            `
    );
  } else {
    console.log("entered the else");
    $("#civilqueryResult").empty();
    $("#civilqueryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

function civilactiveClassRemove() {
  for (i = 0; i < civilSubLawlabels.length; i++) {
    civilSubLawlabels[i].classList.remove("civil-acitve");
  }
  for (i = 0; i < civilCourtlabels.length; i++) {
    civilCourtlabels[i].classList.remove("civil-acitve");
  }
  for (i = 0; i < civilCategorylabels.length; i++) {
    civilCategorylabels[i].classList.remove("civil-acitve");
  }
  console.log("entered civilremove active");
}

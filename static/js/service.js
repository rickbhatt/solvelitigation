var serviceSubLawType = document.getElementsByClassName("service-sub-law-type");

var serviceSubLawInput = document.querySelectorAll(
  "input[name='service-sublaw']"
);

var serviceCourt = document.getElementsByClassName("service-court");

var serviceCourtInput = document.querySelectorAll(
  "input[name='service-court']"
);

var serviceCategory = document.getElementsByClassName("service-category");

var serviceCategoryInput = document.querySelectorAll(
  "input[name='service-category']"
);

const servicecourtToggle = document.querySelector(".service-court-ul");

const serviceCategoryToggle = document.querySelector(".service-category-ul");

// const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

var serviceSubLawTypeVal = [];

var serviceCourtval = [];

var serviceCategoryval = [];

// for constant query
for (i = 0; i < serviceSubLawType.length; i++) {
  serviceSubLawType[i].addEventListener("click", () => {
    var visibility = servicecourtToggle.getAttribute(
      "data-servicecourtvisilble"
    );

    if (visibility === "false") {
      servicecourtToggle.setAttribute("data-servicecourtvisilble", true);
    }

    for (j = 0; j < serviceSubLawInput.length; j++) {
      if (serviceSubLawInput[j].checked) {
        serviceSubLawTypeVal.push(serviceSubLawInput[j].value);
        console.log(serviceSubLawTypeVal);
      }
    }
  });
}

for (i = 0; i < serviceCourt.length; i++) {
  serviceCourt[i].addEventListener("click", () => {
    var visibility = serviceCategoryToggle.getAttribute(
      "data-servicecategoryvisible"
    );

    if (visibility === "false") {
      serviceCategoryToggle.setAttribute("data-servicecategoryvisible", true);
    }
    for (j = 0; j < serviceCourtInput.length; j++) {
      if (serviceCourtInput[j].checked) {
        serviceCourtval.push(serviceCourtInput[j].value);
        console.log(serviceCourtval);
      }
    }
  });
}

for (i = 0; i < serviceCategory.length; i++) {
  serviceCategory[i].addEventListener("click", () => {
    for (j = 0; j < serviceCategoryInput.length; j++) {
      if (serviceCategoryInput[j].checked) {
        serviceCategoryval.push(serviceCategoryInput[j].value);
        console.log(serviceCategoryval);
      }
    }
  });
}

for (i = 0; i < serviceCategory.length; i++) {
  serviceCategory[i].addEventListener("click", (e) => {
    e.preventDefault();
    servicesubLawType = serviceSubLawTypeVal;
    servicecourt = serviceCourtval;
    serviceCategory = serviceCategoryval;
    console.log(
      "this is from ajax : ",
      servicesubLawType,
      servicecourt,
      serviceCategory
    );
    $.ajax({
      type: "POST",
      headers: { "X-CSRFToken": csrftoken },
      mode: "same-origin", // Do not send CSRF token to another domain.
      url: "service",
      data: {
        "servicesubLawType[]": serviceSubLawTypeVal,
        "servicecourt[]": serviceCourtval,
        "serviceCategory[]": serviceCategoryval,
      },
      success: function (response) {
        // console.log(response.result);
        serviceQResult(response);
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
}

function serviceQResult(response) {
  serviceData = response.result;
  if (response.status == "success") {
    $("#servicequeryResult").empty();
    for (i = 0; i < serviceData.length; i++) {
      $("#servicequeryResult").append(
        `
              <a class="service-title" href="/professional/detail-doc/${
                serviceData[i].id
              }">${i + 1}.&nbsp ${
          serviceData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="service-headnote">${serviceData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if");
    $("#servicequeryResult").empty();
    $("#servicequeryResult").append(
      `
              <p class="no-citation-found">No citations found...</p>
            `
    );
  } else {
    // console.log("entered the else");
    $("#servicequeryResult").empty();
    $("#servicequeryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

// end for constant querying

// FOR ADDING THE ACTIVE CLASS IN LABEL

// var labels = document.getElementsByTagName("label");

var serviceSubLawlabels = document.getElementsByClassName(
  "service-sub-law-type-label"
);

var serviceCourtlabels = document.getElementsByClassName(
  "service-service-court-label"
);

var serviceCategorylabels = document.getElementsByClassName(
  "service-law-category-label"
);

for (let i = 0; i < serviceSubLawlabels.length; i++) {
  serviceSubLawlabels[i].addEventListener("click", serviceSublawaddclass);
}

for (let i = 0; i < serviceCourtlabels.length; i++) {
  serviceCourtlabels[i].addEventListener("click", serviceCourtaddclass);
}

for (let i = 0; i < serviceCategorylabels.length; i++) {
  serviceCategorylabels[i].addEventListener("click", serviceCategoryaddclass);
}

function serviceSublawaddclass(event) {
  let active = document.getElementsByClassName("service-sub-law-type-label");

  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("service-active");
  }
  for (i = 0; i < serviceCourtlabels.length; i++) {
    serviceCourtlabels[i].classList.remove("service-active");
  }
  for (i = 0; i < serviceCategorylabels.length; i++) {
    serviceCategorylabels[i].classList.remove("service-active");
  }
  event.target.classList.add("service-active");
}

function serviceCourtaddclass(event) {
  let active = document.getElementsByClassName("service-service-court-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("service-active");
  }
  for (i = 0; i < serviceCategorylabels.length; i++) {
    serviceCategorylabels[i].classList.remove("service-active");
  }
  event.target.classList.add("service-active");
}

function serviceCategoryaddclass(event) {
  let active = document.getElementsByClassName("service-law-category-label");
  for (i = 0; i < active.length; i++) {
    active[i].classList.remove("service-active");
  }
  event.target.classList.add("service-active");
}
// END FOR ADDIING ACTIVE CLASS IN LABEL

// SEARCH FORM AJAX CALLS
$(document).on("submit", "#service_search_form", function (e) {
  e.preventDefault();
  var serviceq = $("#service_search").val();

  // ajax call

  $.ajax({
    type: "GET",
    // headers: { "X-CSRFToken": csrftoken },
    // mode: "same-origin",
    url: "serviceSearch",
    data: {
      q: serviceq,
    },
    success: function (response) {
      //   console.log(response.result);
      serviceSearchResult(response);
    },
    error: function (error) {
      console.log(error);
    },
  });
});

function serviceSearchResult(response) {
  serviceData = response.result;
  if (response.status == "success") {
    $("#servicequeryResult").empty();
    for (i = 0; i < serviceData.length; i++) {
      $("#servicequeryResult").append(
        `
              <a class="service-title" href="/professional/detail-doc/${
                serviceData[i].id
              }">${i + 1}.&nbsp ${
          serviceData[i].title
        } <i class="fas fa-external-link-alt"></i></a>
              <p class="service-headnote">${serviceData[i].headnote}</p>
              <span class="bottom-bar"></span>
        `
      );
    }
  } else if (response.status == "nosuccess") {
    // console.log("entered the else if of no success");
    $("#servicequeryResult").empty();
    $("#servicequeryResult").append(
      `
              <p class="no-citation-found">No citations found for "${serviceData}"</p>
              <p class="no-citation-found">Please Check the spelling or else try searching with a different word.</p>
            `
    );
  } else if (response.status == "empty") {
    // console.log("entered the else if empty");
    $("#servicequeryResult").empty();
    $("#servicequeryResult").append(
      `
              <p class="no-citation-found">You searched nothing...</p>
            `
    );
  } else {
    console.log("entered the else");
    $("#servicequeryResult").empty();
    $("#servicequeryResult").append(
      `
              <p class="no-citation-found">We are facing some problems...</p>
            `
    );
  }
}

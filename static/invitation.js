
const form = document.getElementById("form");
form.addEventListener("submit", start);

const loader = document.querySelector("#loading");
// showing loading
function displayLoading() {
  loader.classList.add("display");
}

// hiding loading 
function hideLoading() {
  loader.classList.remove("display");
}

async function start(ev) {
  ev.preventDefault();
  console.log("start form");

  $("#inprogress").show();
  const form = new FormData(ev.target);
  const fullname = form.get("fullname");
  const address = form.get("address");
  const email = form.get("email");
  const dob = form.get("dob");
  const lettertype = form.get("letterselection");
  const og = form.get("og");
  const speaker = form.get("talk");
  const passport_no = form.get("passport_no");
  var data

  displayLoading();

  if (lettertype == "none") {
    data = {
      "fullname": fullname,
      "address": address,
      "email": email,
      "dob": dob,
      "passport_no": passport_no
    }

  } else if (lettertype == "og") {
    data = {
      "fullname": fullname,
      "address": address,
      "email": email,
      "dob": dob,
      "passport_no": passport_no,
      "letteropt": {
        "key": "og",
        "value": og
      }
    };
  } else if (lettertype == "speaker") {
    data = {
      "fullname": fullname,
      "address": address,
      "email": email,
      "dob": dob,
      "passport_no": passport_no,
      "letteropt": {
        "key": "speaker",
        "value": speaker
      }
    };
  }

  displayLoading()
  $("#form").hide();
  await fetch('https://djc-letter.herokuapp.com/invitation', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(data)
  }).then(res => res.json()).then(data => {
    hideLoading()
    console.log(data)
    $("#inprogress").hide();
    $("#ready").show();
  });
}

$(document).ready(function () {
  $("#letterselection").change(function () {
    var selected = $(this).val();
    if (selected == "none") {
      $("#og").hide();
      $("#speaker").hide();
    }
    else if (selected == "og") {
      $("#og").show();
      $("#speaker").hide();
    }
    else if (selected == "speaker") {
      $("#og").hide();
      $("#speaker").show();
    }
  });
});

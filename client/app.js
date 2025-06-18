function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for(var i in uiBathrooms) {
    if(uiBathrooms[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; 
}

function getBedroomValue() {  
  var uiBedroom = document.getElementsByName("uiBedroom"); 
  for(var i in uiBedroom) {
    if(uiBedroom[i].checked) {
        return parseInt(i)+1;
    }
  }
  return -1; 
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");

  var sqft = document.getElementById("uiSqft");
  var bedroom = getBedroomValue(); 
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price"; 

  $.post(url, {
      total_sqft: parseFloat(sqft.value),
      bedroom: bedroom,   
      bath: bathrooms,
      location: location.value
  }, function(data, status) {
      console.log(data.estimated_price);
      estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "</h2>";
      console.log(status);
  });
}

function onPageLoad() {
  console.log("Document loaded, fetching locations...");

  var url = "http://127.0.0.1:5000/get_location_names";
  
  fetch(url)
  .then(response => response.json())
  .then(data => {
      console.log("Response received:", data); 

      if (data.locations && data.locations.length > 0) {
          let uiLocations = document.getElementById("uiLocations");
          uiLocations.innerHTML = ""; 

          let defaultOption = document.createElement("option");
          defaultOption.text = "Choose a Location";
          defaultOption.value = "";
          defaultOption.disabled = true;
          defaultOption.selected = true;
          uiLocations.appendChild(defaultOption);

          data.locations.forEach(location => {
              let opt = document.createElement("option");
              opt.text = location;
              opt.value = location;
              uiLocations.appendChild(opt);
          });

          console.log("Dropdown updated successfully!");
      }
  })
  .catch(error => console.error("Error fetching locations:", error));
}

window.onload = onPageLoad;

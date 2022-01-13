function OpenProduct(i) { 
  //console.log($(".product-price[item-data=" + i + "]").attr("price-data"));
  var item = $('.product-image[item-data="' + i + '"] img');
  var prix = $(".product-price[item-data=" + i + "]");
  var mess = "name" + i;
  console.log(mess);
  var name = document.getElementById('name' + i);
  var lbi = $(".lightbox-blanket .product-image img");
  var lbp = $(".lightbox-blanket .product-price ");
  //var lbn = $(".lightbox-blanket .product-title ");
  console.log($(item).attr("src"));
  console.log($(prix).attr("price-data"));
  console.log(name.innerHTML);
  $(lbi).attr("src", $(item).attr("src"));
  $(lbp).attr("price-data", $(prix).attr("price-data"));
  $(".lightbox-blanket").toggle();
  $("#product-quantity-input").val("0");
  document.getElementById("displayPrice").innerHTML = "$" + $(prix).attr("price-data");
  document.getElementById("displayName").innerHTML = name.innerHTML;
  //console.log($(".lightbox-blanket .product-price ").attr("price-data"));
  CalcPrice(0);
}
//Go Back
function GoBack() {
  $(".lightbox-blanket").toggle();
}

//Calculate new total when the quantity changes.
function CalcPrice(qty) {
  //var price = $(".product-price").attr("price-data");
  var price = $(".lightbox-blanket .product-price").attr("price-data");
  var total = parseFloat(price * qty).toFixed(2);
  $(".product-checkout-total-amount").text(total);
}

//Reduce quantity by 1 if clicked
$(document).on("click", ".product-quantity-subtract", function (e) {
  var value = $("#product-quantity-input").val();
  //console.log(value);
  var newValue = parseInt(value) - 1;
  if (newValue < 0) newValue = 0;
  $("#product-quantity-input").val(newValue);
  CalcPrice(newValue);
});

//Increase quantity by 1 if clicked
$(document).on("click", ".product-quantity-add", function (e) {
  var value = $("#product-quantity-input").val();
  //console.log(value);
  var newValue = parseInt(value) + 1;
  $("#product-quantity-input").val(newValue);
  CalcPrice(newValue);
});

$(document).on("blur", "#product-quantity-input", function (e) {
  var value = $("#product-quantity-input").val();
  //console.log(value);
  CalcPrice(value);
});

function AddToCart(e) {
  e.preventDefault();
  var qty = $("#product-quantity-input").val();
  if (qty === "0") {
    return;
  }
  var toast =
    '<div class="toast toast-success">Added ' + qty + " to cart.</div>";
  $("body").append(toast);
  setTimeout(function () {
    $(".toast").addClass("toast-transition");
  }, 100);
  setTimeout(function () {
    $(".toast").remove();
  }, 3500);
}
function sumProfit() {
	var sum = 0;
	var profit = document.getElementById('profit')
	// iterate through each td based on class and add the values
	$(".profit").each(function() {
		var value = $(this).text();
		// add only if the value is number
		if(!isNaN(value) && value.length != 0) {
			sum += parseFloat(value);
		}
	});
	$("#profit").html(sum.toString());
	return false;
};

$(document).ready(function(){
	var name;
	$.getJSON("https://www.osrsbox.com/osrsbox-db/items-complete.json", function(result){
        $.each(result, function(i, field){
			$.each(field, function(key, value){
				if (key === "name")
					name = value;
				if (key === "tradeable_on_ge" && value === true)
					$("#items").append("<option value='" + name + "'>");
			});
        });
    });
});

function showAddItem() {
	document.getElementById("overlay").style.display = "block";
	document.getElementById("add-item-form").style.display = "block";
}

function hideAddItem() {
	document.getElementById("overlay").style.display = "none";
	document.getElementById("add-item-form").style.display = "none";
}

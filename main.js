function sumFirstProfit() {
	var profit = document.getElementById('profit')
	var sum = 0;
	if (profit.innerHTML == "") {
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
	}
	else
		return false;
};
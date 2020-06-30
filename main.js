 $(document).ready(function(){
    $.getJSON("https://www.osrsbox.com/osrsbox-db/items-json/12453.json", function(result){
        $.each(result, function(i, field){
            $("#items").append($"<option>").attr('value').text('test');
        });
    });
});
$(document).ready(function(){

	$("li").each(function() {
		if( $(this).next("ul").length != 0 ) {
			$(this).css("color","black");
		}
	});

	$("li").click(function() {
  		$(this).next("ul").toggle();
  		$(this).next("ul").children("li").toggle();
	});
});
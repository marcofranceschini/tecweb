$(document).ready(function(){
	$("#play").click(function(){
		$("#carousel").carousel("cycle");
	});
			
	$("#play").hide();
				
	$("#pause").click(function(){
		$("#carousel").carousel("pause");
		$("#pause").hide();
		$("#play").show();
	});
				
	$("#play").click(function(){
		$("#carousel").carousel("cycle");
		$("#play").hide();
		$("#pause").show();
	});
});
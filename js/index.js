$(document).ready(function(){
	$("#backTop").click(function(){
		event.preventDefault();
 		$("html, body").animate({
 			scrollTop:0
 		},"slow"); 
	})
});
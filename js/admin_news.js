document.addEventListener("DOMContentLoaded", function() {
    if (document.getElementById("submit_modal_wallpaper")) {
    
    	document.getElementById("form_modal_modify").onsubmit = function() {
    		var regexp = /\w+\.(gif|png|jpg|jpeg)/i;
    		var img = document.getElementById("wallpaper_new_img");
    		var submit = document.getElementById('submit_modal_wallpaper');
    		
    		if (submit.value == 'Aggiungi') {
    			if (img.value.search(regexp) == -1) {
    				img.style.color = "red";
    				return false;	
    			} else return true;
    		} else return true; 	
    	};
    	 
		document.getElementById("wallpaper_new_img").addEventListener("change", function() {
        	var regexp = /\w+\.(gif|png|jpg|jpeg)/i;
    		var img = document.getElementById("wallpaper_new_img");
    		if (img.value.search(regexp) == -1) {
	        	img.style.color = "red";
    		} else {
    			img.style.color = "black";
    		}   
        });
    }
}, true);
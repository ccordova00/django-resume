$(document).ready(function(){
	$("a[id='close-intro']").click(function() {
			$('#intro-box').hide("slow");
	});
	// $("input[id|='cert-check']").click(function() {
	// 	if (!$(this).is(':checked')){
	// 		$("#cert-check-all").prop('checked', false); //deselects the superior section
	// 	}		
	// });

    $("input[id$='check-all']").click(function() {
		var selected = '';
		var deselect = '';
		switch (this.id){
			case "cert-check-all":
			    selected = 'cert-check';
				break;
			case "skill-check-all":
			    selected = 'skill';
			    break;
			case "skill-program-check-all":
				selected = 'skill-program';
				deselect = '#skill-check-all'; //if this section is deselected, deselect the superior section
			    break;
			case "skill-platform-check-all":
				selected = 'skill-platform';
				deselect = '#skill-check-all'; //if this section is deselected, deselect the superior section
			    break;
			case "skill-network-check-all":
				selected = 'skill-network';
				deselect = '#skill-check-all'; //if this section is deselected, deselect the superior section
			    break;
			case "skill-automation-check-all":
				selected = 'skill-automation';
				deselect = '#skill-check-all'; //if this section is deselected, deselect the superior section
			    break;
			case "skill-protocol-check-all":
				selected = 'skill-protocol';
				deselect = '#skill-check-all'; //if this section is deselected, deselect the superior section
			    break;
			case "skill-apps-check-all":
				selected = 'skill-apps';
				deselect = '#skill-check-all'; //if this section is deselected, deselect the superior section
				break;
			case "exp-check-all":
			    selected = 'exp';
			    break;
			default:
			    console.log("this.id: " + this.id);
			    break;
		}

		if ($(this).is(':checked')){
		    $("input[id|=" + selected + "]").prop('checked', true);
		}
		// else {
		// 	$("input[id|=" + selected + "]").prop('checked', false);
		// 	$(deselect).prop('checked', false); //deselects the superior section
		// }
    });
});

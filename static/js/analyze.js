$(function(){
	$('button').click(function(){
		var lngTxt = $('#inputText').val();
		if(lngTxt.length < 1){
			//if there is no text, let the user know he should enter text
			 $("#myModal").modal();
			 return;
		}

		var lngTxt = $('#inputText').val();
		if(lngTxt.length < 50){
			/*just show a little notification to the user that it would be better to use a longer text for
			better results
			*/
			 $("#myShortModal").modal();
		}

		$.ajax({
			url: '/Summarizer',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				$("#result").html(response.shortTxt);
				$("#summary").show();
			    $("html, body").animate({ scrollTop: $(document).height() }, "slow");
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
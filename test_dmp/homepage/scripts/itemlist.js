$(function () {


// Search function
	$('.searchbar').on('keyup', function(e) {
		var searchTerm = $('.searchbar').val().toLowerCase();
		$('.rental_container').each(function() {
			var item = $(this).find('#item').html().toLowerCase(),
				match = false;

			// Does the item match the search term?
			if(item.indexOf(searchTerm) != -1) {
				match = true;
			}
			if(match) {
				$(this).show();
			} else {
				$(this).hide();
			}
		});
	});

});
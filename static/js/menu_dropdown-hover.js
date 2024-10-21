$(document).ready(function() {
    $('.dropdown').hover(
        function() {
            $(this).find('.dropdown-toggle').dropdown('show');
        },
        function() {
            var $dropdown = $(this).find('.dropdown-toggle');
            if (!$dropdown.next('.dropdown-menu').is(':hover')) {
                $dropdown.dropdown('hide');
            }
        }
    );

    $('.dropdown-menu').mouseleave(function() {
        var $dropdownToggle = $(this).prev('.dropdown-toggle');
        $dropdownToggle.dropdown('hide');
    });
});

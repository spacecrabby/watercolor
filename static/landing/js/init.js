(function($){
  $(function(){

    $('.button-collapse').sideNav();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$('a').click(function(){
    if (+this.href.indexOf('tel') === -1) {
        var contact = "#contact";
        if (+this.href.indexOf(contact) > -1) {
            $("html, body").animate({ scrollTop: $(document).height() }, "slow")
            return false;
        };

        if ($( $.attr(this, 'href') ).offset() === undefined) {
            $("html, body").animate({ scrollTop: 0 }, "slow");
            return false;
        }
        $('html, body').animate({
            scrollTop: $( $.attr(this, 'href') ).offset().top - 64,
        }, "slow");
        return false;
    }
});
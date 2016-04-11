(function($){
  $(function(){

    $('.button-collapse').sideNav();
    $('.materialboxed').materialbox();

  }); // end of document ready
})(jQuery); // end of jQuery name space


$('a').click(function(){
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
});
var comment_has_next = "True";
var page_number = 1;

$(document).ready(function(){
    load_comments();
});

$("#load-more").on( "click", function() {
    load_comments();
});

function load_comments(){
    var url = comments_url + page_number;
    $.get(url, function(data) {
        $("#comments").append(data);
    }).done(function( data ) {
        page_number += 1;
        if(comment_has_next === "False"){
            $("#load-more").remove();
        }
    });
}

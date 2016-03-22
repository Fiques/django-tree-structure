$(document).ready(function(){
    $("#companies").on("click", ".subcompany", function(event){
        event.preventDefault();
        var form = $("#postcompany").clone(true);
        form.find('.parent').val($(this).parent().parent().attr('id'));
        $(this).parent().append(form);
    });
});
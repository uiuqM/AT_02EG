$(document).on('submit', '#nota-form', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/nota',
        data:{
            titulo: $('#titulo').val(),
            conteudo: $('#conteudo').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken').val()
        },
    })
})
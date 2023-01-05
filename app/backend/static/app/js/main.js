function showPword() {
    var x = document.getElementsByClassName("password");
    for (let i = 0; i < x.length; i++) {
        if (x[i].type === "password") {
            x[i].type = "text";
        } else {
            x[i].type = "password";
        }
    }
}


// Used to add a spinner to submit buttons
var temp_button_text;
function CustomFormSubmitPost(e) {
    var el = $(e);
    temp_button_text = el.text()
    el.attr('disabled', 'disabled').text("").append('<class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>Loading...');
};
function CustomFormSubmitResponse(e) {
    var el = $(e);
    el.removeAttr('disabled').text(temp_button_text);
};




//ajax functions to alter tha like and bookmark buttons
"use strict";
var AJAXControls = function () {
    var like = function(){
        $('a.like').click(function() {
            var $obj = $(this);
            var target_id = $obj.attr('id').split('_')[1];
            $obj.prop('disabled', true);
            $.ajax({
                url: '/likes/add-or-remove/',
                type: 'POST',
                data: {target_model: $obj.attr('model'),
                        object_id: target_id
                },
                success: function(response) {
                    var status = response.split("|")[0];
                    var count = response.split("|")[1];
                    if (status == 'added') {
                        $(".like-" + target_id).removeClass('fa-regular').addClass('fa-solid');
                        $(".like").removeClass('btn-outline-primary').addClass('btn-outline-danger');
                    }
                    else {
                        $(".like-" + target_id).removeClass('fa-solid').addClass('fa-regular');
                        $(".like").removeClass('btn-outline-danger').addClass('btn-outline-primary');
                    }
                    $(".like-count-" + target_id).html(count);
                    $obj.prop('disabled', false);
                }
            });
        });
    };

    var bookmark = function(){
        $('a.bookmark').click(function() {
            var $obj = $(this);
            var target_id = $obj.attr('id').split('_')[1];
            $obj.prop('disabled', true);
            $.ajax({
                url: '/bookmarks/add-or-remove/',
                type: 'POST',
                data: {target_model: $obj.attr('model'),
                        object_id: target_id
                },
                success: function(response) {
                    var status = response.split("|")[0];
                    var count = response.split("|")[1];
                    if (status == 'added') {
                        $(".bookmark-" + target_id).removeClass('fa-regular').addClass('fa-solid');
                        $(".bookmark").removeClass('btn-outline-success').addClass('btn-outline-warning');
                    }
                    else {
                        $(".bookmark-" + target_id).removeClass('fa-solid').addClass('fa-regular');
                        $(".bookmark").removeClass('btn-outline-warning').addClass('btn-outline-success');
                    }
                    $(".bookmark-count-" + target_id).html(count);
                    $obj.prop('disabled', false);
                }
            });
        });
    };

    var item = function(){
        $('a.item').click(function() {
            var $obj = $(this);
            var target_id = $obj.attr('id').split('_')[1];
            var action = $obj.attr('action')
            var quantity = $('#quantity-input-'+target_id).val()
            $obj.prop('disabled', true);
            $.ajax({
                url: '/items/add-or-remove/',
                type: 'POST',
                data: {
                    target_model: $obj.attr('model'),
                    object_id: target_id,
                    object_quantity: quantity,
                    action: action
                },
                success: function(data) {
                    if (data["result"] == 'Success'){
                        $(".item-count").html(data["data"]["item_count"]);
                        $(".item-total-price").html(data["data"]["item_total_price"]);
                        $('#stock-input-'+target_id).val(data["data"]["stock"])
                        $('#quantity-input-'+target_id).val(0)
                        $obj.prop('disabled', false);
                        if (data["data"]["status"]=="remove"){
                            $(".item-list-" + target_id).remove();
                        }
                    }
                    ShowAlert(data["result"], data["message"], data["result"].toLowerCase(), data["redirect"]);
                }
            });
        });
    };

    var source = function(){
        $('a.source').click(function() {
            var $obj = $(this);
            var card_id = $obj.attr('value')
            $obj.prop('disabled', true);
            $.ajax({
                url: '/update-source/',
                type: 'POST',
                data: {
                    card_id: card_id,
                },
                success: function(data) {
                    ShowAlert(data["result"], data["message"], data["result"].toLowerCase(), data["redirect"]);
                }
            });
        });
    };

    var pay = function(){
        $('a.pay').click(function() {
            var $obj = $(this);
            var card_id = $obj.attr('value')
            $obj.prop('disabled', true);
            $.ajax({
                url: '/pay/',
                type: 'POST',
                data: {
                    card_id: card_id,
                },
                success: function(data) {
                    ShowAlert(data["result"], data["message"], data["result"].toLowerCase(), data["redirect"]);
                }
            });
        });
    };

    return {
        init: function () {
            like();
            bookmark();
            item();
            source();
            pay();
        }
    };
}();

"use strict";
var FormControls = function () {

    var secureform = function () {
        var form = $('#secureform')
        form.submit(function(event){
            event.preventDefault();
            event.stopImmediatePropagation();
            CustomFormSubmitPost($('#secureform button[type=submit]'));
            grecaptcha.ready(function() {
                grecaptcha.execute(recaptcha_site_key, {action: "/"}).then(function(token) {
                    document.getElementById('id_token').value = token;
                    var formdata = form.serialize() 
                    $.ajax({
                        url: form.attr("action"),
                        method: form.attr("method"),
                        headers: {"X-Requested-With": "XMLHttpRequest"},
                        data: formdata,
                        success: function(data, textStatus, jqXHR){
                            CustomFormSubmitResponse($('#secureform button[type=submit]'));
                            form[0].reset()
                            ShowAlert(data["result"], data["message"], data["result"].toLowerCase(), data["redirect"]);
                        },
                        error: function(xhr){
                            CustomFormSubmitResponse($('#secureform button[type=submit]'));
                            console.log(xhr.status + ": " + xhr.responseText);
                        }
                    }) 
                })
            })
        })    
    };


    var basicform = function () {
        var form = $('#basicform')
        form.submit(function (event) {
            event.preventDefault();
            event.stopImmediatePropagation();
            CustomFormSubmitPost($('#basicform button[type=submit]'));
            var formdata = form.serialize()
            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                headers: {"X-Requested-With": "XMLHttpRequest"},
                data: formdata,
                success: function (data) {
                    CustomFormSubmitResponse($('#basicform button[type=submit]'));
                    ShowAlert(data["result"], data["message"], data["result"].toLowerCase(), data["redirect"]);
                },
                error: function (xhr) {
                    CustomFormSubmitResponse($('#basicform button[type=submit]'));
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            })
        })
    }


    var fileform = function () {
        var form = $('#fileform')
        form.submit(function (event) {
            event.preventDefault();
            event.stopImmediatePropagation();
            var formdata = new FormData(form[0]);
            
            var form_label = $('#id_form_label')
            
            if (form_label == 'user_avatar_form'){
                var file = $('#id_avatar')[0].files[0]
                formdata.append("FILE", file)
            }
            else{
                var file = $('#id_image')[0].files[0]
                formdata.append("FILE", file)
            }

            $.ajax({
                url: form.attr("action"),
                method: form.attr("method"),
                headers: {"X-Requested-With": "XMLHttpRequest"},
                data: formdata,
                processData: false,
                contentType: false,
                success: function (data) {
                    CustomFormSubmitResponse($('#fileform button[type=submit]'));
                    ShowAlert(data["result"], data["message"], data["result"].toLowerCase(), data["redirect"]);
                },
                error: function (xhr) {
                    console.log(xhr.status + ": " + xhr.responseText);
                }
            })
        });
    };

    
    return {
        init: function () {

            basicform();
            secureform();
            fileform();
        }
    };

}();

jQuery(document).ready(function () {

    AJAXControls.init();
    FormControls.init();

});


$(function() {
    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
})

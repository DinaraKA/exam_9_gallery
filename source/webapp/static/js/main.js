const baseUrl = 'http://localhost:8000/api/v1/';

function getFullPath(path) {
    path = path.replace(/^\/+|\/+$/g, '');
    path = path.replace(/\/{2,}/g, '/');
    return baseUrl + path + '/';
}

function makeRequest(path, method, auth=true, data=null) {
    let settings = {
        url: getFullPath(path),
        method: method,
        dataType: 'json'
    };
    if (data) {
        settings['data'] = JSON.stringify(data);
        settings['contentType'] = 'application/json';
    }
    if (auth) {
        settings.headers = {'X-CSRFToken': getCookie('csrftoken')};
    }
    return $.ajax(settings);
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function createComment(text, photo) {
    const credentials = {text, photo};
    request = makeRequest('comments', 'post', true, credentials);
    request.done(function (data) {

    }).fail(function (response, status, message) {
        console.log('Comment not added!');
        console.log(response.responseText);
    });
}

function formComment() {
    let commentForm = $('#add_comment');
    let textInput = $('#comment');
    let photoId = $('#photo_id');
    commentForm.on('submit', function (event) {
        event.preventDefault();
        createComment(textInput.val(), photoId.val());
    });
}

function deleteComment(id) {
    $.ajax({
        url: 'http://localhost:8000/api/v1/comments/' + id,
        method: 'delete',
        headers: {'X-CSRFToken': getCookie('csrftoken')},
        dataType: 'json',
        contentType: 'application/json',
        success: function (response, status) {
            console.log(response);
        },
        error: function (response, status) {
            console.log(response);
        }
    });
}

formComment();

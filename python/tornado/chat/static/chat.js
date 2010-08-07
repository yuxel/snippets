/**
 * This is a simplified version of javascript file
 * from facebook
 *
 * Original file : http://github.com/facebook/tornado/blob/master/demos/chat/static/chat.js
 */

URL_NEW_MESSAGE = "/new";
URL_GET_UPDAGTES = "/updates";

$(document).ready(function() {
    //listen click events
    $("#submitButton").live("click", function(e) {
        e.preventDefault();
        newMessage();
        return false;
    });

    // listen messages
    updater.poll();
});

// post json to URL
jQuery.postJSON = function(url, args, callback) {
    $.ajax({url: url, data: $.param(args), dataType: "text", type: "POST",
            success: function(response) {
        if (callback) callback(eval("(" + response + ")"));
    }, error: function(response) {
        alert('POST ERROR');
    }});
};


// send new message
function newMessage() {
    message = {};
    message["body"] = $("#message").val() || "--- Empty post ---";

    $.postJSON(URL_NEW_MESSAGE, message, function(response) {
        updater.showMessage(response);

        //clear message and focus
        $("#message").val('').select();
    });
}

// message updater
var updater = {
    errorSleepTime: 500,
    cursor: null,

    // set long polling
    poll: function() {
        var args = {};
        if (updater.cursor) args.cursor = updater.cursor;
        $.ajax({url: URL_GET_UPDAGTES, type: "GET", dataType: "text",
                data: $.param(args), success: updater.onSuccess});
    },

    // on success, set new messages
    onSuccess: function(response) {
        try {
            updater.newMessages(eval("(" + response + ")"));
        } catch (e) {
            return;
        }
        updater.errorSleepTime = 500;
        window.setTimeout(updater.poll, 0);
    },

    // show new messages
    newMessages: function(response) {
        if (!response.messages) return;
        updater.cursor = response.cursor;
        var messages = response.messages;
        updater.cursor = messages[messages.length - 1].id;
        for (var i = 0; i < messages.length; i++) {
            updater.showMessage(messages[i]);
        }
    },

    // show existing messages
    showMessage: function(message) {
        var existing = $("#m" + message.id);
        if (existing.length > 0) return;
        var node = $(message.html);
        node.hide();
        $("#inbox").append(node);
        node.slideDown();
    }
};

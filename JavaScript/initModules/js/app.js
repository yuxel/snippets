var app = app || {};

app.init = function () {
    var $body = $("body");

    var getModules = function () {
        return $body.data("modules").split(" ");
    };

    var initModules = function (modules) {
        var moduleName;

        for(var i = 0, len = modules.length; i < len; i++) {
            moduleName = modules[i];
            window.modules && window.modules[moduleName] && new window.modules[moduleName]();
        }
    };

    initModules(getModules());
};

$(app.init);

var app = app || {};

/** get class from theme, fallback to base class */
app.construct = function (className) {
    var theme = app._theme;
    if (window[theme] && window[theme][className]) {
        return new window[theme][className];
    }
    else if (window.base[className]){
        return new window.base[className];
    }
    else {
        throw 'No such class';
    }
};

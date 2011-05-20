Ext.namespace('tart.admin.acl');

tart.admin.acl.init = function () {

    var aclRules = {
        //namespace                 : methods in array
        //'tart.admin.pages.homePage' : ["onSaveButtonClick"]
        //'tart.admin.pages.homePage' : ["init"]
        'tart.admin.pages.homePage' : ["close"]
        //'tart.admin.pages.homePage' : ["init", "onSaveButtonClick", "close"]
    };

    var getObjectFromString = function(string) {
        var parts = string.split(".");
        var obj = window;

        for (var i = 0, len = parts.length; i < len; ++i) {
            if (!obj[parts[i]] ) {
                break;
            }
            obj = obj[parts[i]];
        }

        return obj;
    };

    for(var i in aclRules) {
        var namespace = getObjectFromString(i);
        if (!namespace) continue;
        var methods = aclRules[i];

        for (var j = 0; j < methods.length; j++) {
            namespace[methods[j]] = function () {
                console.log('you dont have an access');
            };
        }
    };
}();

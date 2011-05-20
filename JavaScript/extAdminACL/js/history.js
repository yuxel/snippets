Ext.namespace('tart.admin.history');

    tart.admin.history.init = function () {
    Ext.History.init();
    Ext.History.on('change', tart.admin.history.onChange);
};

tart.admin.history.onChange = function (token) {
    switch(token) {
        case  "homepage.init" : tart.admin.pages.homePage.init(); break;
        case  "homepage.close" : tart.admin.pages.homePage.close(); break;
        case  "homepage.onButtonClick" : tart.admin.pages.homePage.onSaveButtonClick(); break;
    }
};

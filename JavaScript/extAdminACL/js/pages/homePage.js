Ext.namespace("tart.admin.pages.homePage");

tart.admin.pages.homePage.init = function () {
    tart.admin.pages.homePage.panel = new Ext.Window({
        width: 500,
        height: 500,
        items : [
            {xtype : 'button', 
             text : 'Save', 
             handler: tart.admin.pages.homePage.onSaveButtonClick
            }
        ]
    });

    tart.admin.pages.homePage.panel.show();
};

tart.admin.pages.homePage.onSaveButtonClick = function () {
    console.log('you saved something successfully');
};


tart.admin.pages.homePage.close = function () {
    tart.admin.pages.homePage.panel.close();
};

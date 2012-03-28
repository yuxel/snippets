var modules = modules || {};

modules.foo = function () {
    this.moduleName = "foo";
    console.log('initted module ', this.moduleName);
    //you can call lots of specfic functions from this class if you want for module
};

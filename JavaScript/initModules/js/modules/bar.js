var modules = modules || {};

modules.bar = function () {
    this.moduleName = "bar";
    console.log('initted module ', this.moduleName);
    //you can call lots of specfic functions from this class if you want for module
};

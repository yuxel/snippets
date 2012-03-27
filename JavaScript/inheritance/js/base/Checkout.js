var base = base || {};

base.Checkout = function () {
};

base.Checkout.prototype.doFoo = function () {
    console.log('foo -> base');
};

base.Checkout.prototype.doBar = function () {
    console.log('bar -> base');
};

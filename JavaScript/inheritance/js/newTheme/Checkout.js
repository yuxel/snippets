var newTheme = newTheme || {};

//extend newTheme.Checkout from base.Checkout
newTheme.Checkout = function () {
    base.Checkout.apply(this, arguments);
};

newTheme.Checkout.prototype = new base.Checkout();
newTheme.Checkout.prototype._super = base.Checkout;

newTheme.Checkout.prototype.doFoo = function () {
    //We can override this
    console.log('foo -> newTheme');

    //and we can also call parent class' method
    console.log("calling super class' method");
    this._super.prototype.doFoo.apply(this, arguments);
};

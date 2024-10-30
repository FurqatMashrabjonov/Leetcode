/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    return {
        val: init,
        increment(){ return this.val += 1   },
        decrement(){ return this.val -= 1   },
        reset()    { return this.val = init }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
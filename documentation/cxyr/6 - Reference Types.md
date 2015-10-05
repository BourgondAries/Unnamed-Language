## Reference Types ##
*Description*: How are references passed around?

*Discussion*: The language ought to be quite verbose in the way that allows one
to infer what is going on without hopping around in different files. For example
, it would be comforting to know whether a function takes in a reference by
looking at its invocation.

    var 32u a_ = 1000;
    ClassName.doSomething(arg_: ref a_);

ref could be both an operator, and used in declarations, but that seems rather
ambiguous. This also requires us to consider the dereferencing, address-of, and
reference-of operator. There are some symbols that we should consider...

    var 32u a_ = 1000;

    $a_       // Let $ return the address-of
    $$a_      // Let $$ return a const-address-of, because an address of an
              // address is nonsensical.

    @a_       // Let @ dereference a type.
    @@a_      // Let @@ return a const-reference, because a reference to a
              // reference is nonsensical.

    ^a_       // Let ^ return the actual object pointed to.
    ^^a_      // Let ^^ return a const-object that is pointed to.


Imagine calling a function that takes a pointer to a const variable, but your
local variable is not const. You need to be able to infer from the call that
the pointer sent into the function will point to memory which will not be edited
by the function.

  var 32u a_ = 1000;
  doSomething(arg_: $$a_);
  assert(a_ == 1000);

We can safely say that no matter how that `doSomething` operates, it will NEVER,
ever, change the value of a_ locally. I don't like the ^ notation though. That
seems superfluous. Let's try the following.

    (:) functionName
    {
      var 32u a_ = 1000;
      doSomething(value_: $$a_);
    }

    (: cref 32u value_) doSomething
    {
      if (@@value_ == 300)
      { doSomethingElse(); }
      else
      { doSomethingOther(); }
    }

Let `cref` be syntactic sugar for `const ref`. Here, taking a pointer is
automatically casted to a reference type. That seems to work for local
references as well.

    (:) functionName
    {
      var 32u a_ = 1000;
      var ref 32u b_ = $a_;
    }

A reference can be considered simple syntactic sugar for `ref X` ->
`const ptr X`. Maybe cref needs to change to refc, since that's more precise.
It is sugar for: `refc X` `ref const X`. Automatically casting pointers to
references seems like a good idea. In no case does it give us any useful
information about the function if we know if it holds a pointer or reference to
our variable. If it's a pointer it can potentially change the pointer value, and
that doesn't matter to us at all, since that's local inside the function. The
best thought to have is to just consider it a reference due to the semantics.

*Conclusion*:
  We use:
  * $ as the address-of operator.
  * $$ as the address-of-const operator.
  * @ as the dereferencing operator.
  * @@ as the dereferencing-to-const operator.
  * A pointer is automatically casted to a reference.


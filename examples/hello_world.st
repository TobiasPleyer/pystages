[env]
greeting: Hello world.
goodbye: See you!

[STAGES]
greet
goodbye

[greet]
info: Simply print a greeting phrase to stdout
run: echo ${env:greeting}

[goodbye]
info: Prints the goodbye phrase to stdout
run: echo ${env:goodbye}

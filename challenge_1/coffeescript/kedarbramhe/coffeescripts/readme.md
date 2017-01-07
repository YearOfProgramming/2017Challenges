##Install
To install, first make sure you have a working copy of the latest stable version of Node.js. You can then install CoffeeScript globally with npm:

`npm install -g coffee-script`

##Usage
To compile this file command used is

`coffee -o javascripts/ -c coffeescripts/`

Option -c means to compile and -o means the output folder.The ordering should always be output then compile.

To run the compiled file simply run the compiled .js file with node
for example

`node hello_world.js`

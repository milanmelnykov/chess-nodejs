Before anything: run `npm install` inside project directory

## Build

To build client code execute: `npm run build`

## Starting project

* Run server `npm start`
* Run client `npm run client`

## Configure database

Copy the file "config/mongodb-example.json" and modify it as you need:

```
cp config/mongodb-example.json <your_destination>
mongod --config <your_destination>
```

# Bike Parking Finder

\* **This is a clone on BikeParkingFinder. I reread it with DJango and PostGIS**

I presently live in Montreal and I use a bike for commuting. I realised while I was searching for a place to park my bike that car owners have apps to help them to find a parking. I searched for equivalent for bike parking places and I found many apps but not for Montreal. However, the city of Montreal have open data on the position on some parking places for bike (bike hoops) at this web page: http://donnees.ville.montreal.qc.ca/dataset/arceaux-velos. Those data are interesting but incomplete. With reflection, I found the idea to complete and update the data on bike parking places with the help of people via a web page and a mobile app. I know that is not a new idea. It was done for others cites, but I think that Montreal need a thing like that. So, this project is a tentative to make something useful for bike commuters.

## REST API Specifications

### Get bike parking places
* URL: /api/bike_parking
* Method: GET
* URL Params:
 * **latitude** geographic latitude of the position wanted **(required)**
 * **longitude**: geographic longitude of the postion wanted **(required)**
 * **radius**: radius of searching in meter. Default value: 350.
 * **count**: maximum number of results. Default value: 10
* Success Response:
 * Code: 200
 * Content: JSON array of objects
 ```javascript
 [{
   id: '52eecfaa-617d-4470-923f-381902f9e31b'
   latitude: 45.00000,
   longitude: -76.00000,
   name: "default name",
   description: "",
   capacity: 1,   
   indoor: false  
 },
 {
   id: '3ea67644-7c6a-46ef-85e6-313ca1370641'
   latitude: 46.00000,
   longitude: -77.00000,
   name: "a name",
   description: "",
   capacity: 3,
   indoor: false  
 }]
 ```

* Error Responses:
 * Invalid arguments: if arguments are not formated correctly.
   * Code: 400
   * Content: JSON Object
   ```javascript
   {"error": "Invalid arguments"}
   ```
 * Arguments missing: if required arguments are missing.
   * Code: 400
   * Content: JSON Object
   ```javascript
   {"error": "Arguments missing"}
   ```   

### Create a new bike parking place
* URL: /api/bike_parking
* Method: POST
* Data Params: JSON Object
```javascript
{
  latitude: 45.00000, //required
  longitude: -76.00000, //required
  accuracy:  5.0, //required (in meters)
  name: "default name", //default value
  description: "", //optional
  capacity: 1, //default value
  indoor: false  //optional indicate if the location is indoor
  winter: false //optional indicate if the location is available in winter
}
```
* Success Response:
 * Code: 201
 * Content: JSON Object
 ```javascript
 {
   id: '52eecfaa-617d-4470-923f-381902f9e31b' //a unique id will be create
   latitude: 45.00000,
   longitude: -76.00000,
   name: "default name",
   description: "",
   capacity: 1,
   indoor: false  //optional indicate if the location is indoor
   winter: false //optional indicate if the location is available in winter
 }
 ```
* Error Response:

### Confirm a bike parking place existed
* URL: /api/bike_parking/:id
* Method: PUT
* Data Params: JSON Object
```javascript
{
  confirmed: true, //required
}
```
* Success Response:
 * Code: 201
 * Content: JSON Object
 ```javascript
 {
   id: ':id'
   latitude: 45.00000,
   longitude: -76.00000,
   name: "default name",
   description: "",
   capacity: 1,
   indoor: false ,
   winter: false
 }
 ```
* Error Response:

### Remove a bike parking place existed
* URL: /api/bike_parking/:id
* Method: DELETE
* Data Params: JSON Object
* Success Response:
 * Code: 200
* Error Response:

### Modify informations on a bike parking place.
* URL: /api/bike_parkings/:id
* Method: PUT
* Data Params: JSON Object
```javascript
{
  latitude: 45.00000, //optional
  longitude: 76.00000, //optional
  name: "default name", //optional
  description: "", //optional
  capacity: 1, //optional
  indoor: false  //optional indicate if the location is indoor
  winter: false //optional indicate if the location is available in winter
}
```
* Success Response:
 * Code: 200
 * Content: JSON Object
 ```javascript
 {
   id: ":id"
   latitude: 45.00000, //optional
   longitude: 76.00000, //optional
   name: "default name", //optional
   description: "", //optional
   capacity: 1, //optional
   indoor: false  //optional
   winter: false  //optional
 }
 ```
* Error Response:

## Installation and build of the project

This project use vue.js and node.js for the frontend, and rust and ElasticSearch for the backend. I choose node.js for the frontend because of node.js package manager npm and browserify. Browserify give the possibility of bundle javascript ans css files from node.js packages to browser files. I choose rust with the framework rocket.rs because it is a language I want to learn and it's performant.
I choose EleasticSearch because it a performant database and it has geo queries feature.

To build the frontend, you have to install node.js at version 5.6.0 or higher. After, you have to execute these commands

```bash
npm install
gulp all
```  

To build to backend, you have to rust at version 1.28-0-nightly and ElasticSearch at version 6.2. Afet that, you have to execute this command

```
cargo run
```

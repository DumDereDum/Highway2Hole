# Source

![Pipeline](https://github.com/DumDereDum/Highway2Hole/blob/main/src/img/pipeline.png)

## Modules:

### Model

Name: ***yolov3-road-damage-detection***

Function: **find_damage( video )**

* Input: **video** - 1 min of road video

* Output: list of tuples like: **[ (frame1, time1), (frame2, time2), (frame3, time3), ... ]**, where **frame** - frame from video with detected pothole (.png image file), **time** - time, when pothole was recorded on road



### DBMS

Structure:

ID | PHOTO_PATH | TIME | GPS | IS_NEW

* ID - id of pothole
* PHOTO_PATH - path to frame with pothole
* TIME - time, when pothole was recorded on road
* GPS - location of pothole
* IS_NEW - `True` if it is new, `False` if it has been marked on map

Functions:

* **add_pothole( (frame, time, gps) )** - add pothole to DB 
  * ***frame*** - frame with pothole (.png image file)
  * ***time*** - time, when pothole was recorded on road
  * ***gps*** - location of pothole
* **get_new_potholes()** - returns list of tuples like:  **[ (frame1, time1, gps1), (frame2, time2, gps2), (frame3, time3,0 gps2), ... ]** and marks the returned potholes as `False` in IS_NEW field



### MAP_PAINTNG

Functions:

* **create_map()** - create map
* **update( potholes )** - update map with dots
  *   ***potholes*** - the result of function **get_new_potholes()**
* **render()** - render current map as image



### FUNCTIONS

Folder with auxiliary function which are needed for getting data, preparing for work and etc.

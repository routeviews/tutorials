## RouteViews Tutorials
  This is the README file for the RouteViews Tutorials repository. The goal of this document is to provide some guidelines for the use of these scripts.

#### Development Environment
  If Docker Engine is installed, one can easily start an appropriate development environment like so:
  ```
  docker build .
  docker images | awk 'NR==2 { print $3 }'
  docker run -it <container_id> bash
  ```
  
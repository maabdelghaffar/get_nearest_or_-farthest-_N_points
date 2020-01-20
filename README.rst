Workshops
==============================================

The workshops documentation demonstrates few examples on how to utilize GeoNode-Project in order to extend/customize GeoNode's functionalities according to your business. The covered topics include the following:

1- Customize your GeoNode with the geonode-project

2- Customize the look and feel

3- Create your ResourceBase Metadata

4- Create your own django app

5- Add a custom model

6- Permissions and APIs

7- Deploy your GeoNode


1- Customize your GeoNode with the geonode-project
--------------------------------------------------

In this example, GeoNode-Project is cloned to create a template instance in which th rest of the examples will be building on top of it.

1- Assuming you already installed GeoNode-Core, firstly we need to create a GeoNode-Project template and this can be achieved from the following command:

.. code-block:: shell
    
    $ django-admin.py startproject my_geonode --template=https://github.com/GeoNode/geonode-project/archive/master.zip -e py,rst,json,yml,ini,env,sample -n Dockerfile

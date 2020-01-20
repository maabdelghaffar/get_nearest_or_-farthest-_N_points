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


Here, django-admin is used with startproject option to create my_geonode project copying the template which is passed as GeoNode-project Github repo. It also includes "py,rst,json,yml,ini,env,sample" extensions

2- Once the cloning finished, the next step is to install the GeoNode-Project we just downloaded as follows: 

.. code-block:: shell
    
    $ pip install -e my_geonode
3- Install geoserver using paver as follows

.. code-block:: shell
    
    $ cd /home/geonode/my_geonode
    $ paver setup
4- Note the GeoNode database connection parameters mentioned in the local_settings.py configuration file. If not found, copy local_settings.py.sample and rename it to local_settings.py then use psql to create the required user and grant the required previleges as follows:

.. code-block:: shell
    
    $ su postgres 
    $ createdb geonode
    $ psql
	postgres=# CREATE USER geonode WITH PASSWORD 'geonode';
	CREATE ROLE  
	postgres=# GRANT ALL PRIVILEGES ON DATABASE "geonode" to geonode;
	GRANT
	postgres=# \q
5- Run GeoNode using paver 

.. code-block:: shell
    
    $ cd /home/geonode/my_geonode
    $ paver start
.. note:: You may find this warning message: You have 132 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): account, actstream, admin, agon_ratings, announcements, auth, avatar, base, contenttypes, dialogos, documents, favorite, geonode_client, geonode_themes, groups, guardian, invitations, layers, maps, mapstore2_adapter, monitoring, oauth2_provider, people, pinax_notifications, services, sessions, sites, socialaccount, taggit, tastypie, upload, user_messages. Run 'python manage.py migrate' to apply them.


Which means you have some sql statements not executed yet and you need to run the "migrate" to sync your database first then "paver start" again as follows:

.. code-block:: shell
    
    $ python manage.py migrate
    $ paver start
6- Once the previous step is done, you can visit 0.0.0.0:8000 or localhost:8000 to view the GUI of GeoNode. However, we still don't have an account in order to login from the GUI. This can be done using django's manage.py createsuperuser as follows:

.. warning:: If encountered this message: (Invalid HTTP_HOST header: '0.0.0.0:8000'. You may need to add u'0.0.0.0' to ALLOWED_HOSTS) It can be fixed in the local_settings.py file

.. code-block:: shell
    $ python manage.py createsuperuser
    $ Username: admin
    $ Email address: admin@admin.com
    $ Password: admin
    $ Password (again): 
    $ Superuser created successfully
7- Use the created account to login from the GUI through localhost:8000 or 0.0.0.0:8000



2- Customize the look and feel
------------------------------

In this section we will change the look and feel of GeoNode, in particular we will do some customization to help understanding how the template inheritance works and how to add new stuff to your GeoNode. The changes will include the home page, the top menu, the footer and a generic GeoNode page.


.. contents:: Table of Contents
   :depth: 2

CDN Support for Plone: Coral Networks
****************************************

Overview
========
This package provides Coral Networks CDN for Plone.

CoralCDN is a decentralized, self-organizing, peer-to-peer web-content 
distribution network. CoralCDN leverages the aggregate bandwidth of volunteers 
running the software to absorb and dissipate most of the traffic for web sites 
using the system. In so doing, CoralCDN replicates content in proportion to the 
content's popularity, regardless of the publisher's resources.[#]_


Requirements
=============

   * Plone 3.3.x (http://plone.org/products/plone)
   * Plone 4.0.x (http://plone.org/products/plone)
   * collective.cdn.core (http://pypi.python.org/pypi/collective.cdn.core)
       
Installation
=============
    
To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``collective.cdn.coral``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            collective.cdn.coral
    

If another package depends on the collective.cdn.coral egg or 
includes its zcml directly you do not need to specify anything in the 
buildout configuration: buildout will detect this automatically.

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.

Go to the 'Site Setup' page in the Plone interface and click on the
'Add/Remove Products' link.

Choose the CDN Support for Plone (check its checkbox) and click the 'Install' button.

Uninstall -- This can be done from the same management screen, but only
if you installed it from the quick installer.

Note: You may have to empty your browser cache and save your resource 
registries in order to see the effects of the product installation.

Usage
============

CDN settings
----------------
After installing this package, go to the 'Site Setup' page in the 
Plone interface and click on the 'CDN Configuration' link.

In this page you can choose which registries will use the CDN settings 
by clicking the respective checkboxes.

Then choose the CoralCDN provider and save the settings.

How it works
--------------
From now on all choosen resource registries will generate links pointing 
to <site_url>.nyud.net/<path_to_resource>, thus using the Coral Networks 
infrastructure to delivery those files.

For example, the link to simplesconsultoria_site-cachekey0549.css file 
would change from::

   http://www.simplesconsultoria.com.br/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css

to::
	
   http://www.simplesconsultoria.com.br.nyud.net/portal_css/beyondskins_simples/simplesconsultoria_site-cachekey0549.css


Sponsoring
===========

Development of this product was sponsored by `Simples Consultoria 
<http://www.simplesconsultoria.com.br/>`_.


Credits
========

    * Simples Consultoria (products at simplesconsultoria dot com dot br) - 
      Implementation

.. [#] Extracted from http://www.coralcdn.org/overview/

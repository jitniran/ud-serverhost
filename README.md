# Udacity ND Linux Server configuration

    Host the python web app on lightsail with security mesaures in place.
    
# IP Address
    1. 13.126.129.241
    2. SSH port : 2200
# Url
    1.http://13.126.129.241/
# Summary of software install and configuration changes
    1. secured server with changing ssh port, configure ufw, created a user grader created ssh-key pair
    2. Installed apache2 and mod_wsgi-py3 to host python app
    3. Installed postgresql and user which has limited permission
    4. .git folder is public inaccessible by haveing a .htaccess in app host folder.
    5. Virtualenvwrapper is used for virtual environment
   
# HTML endpoints

#### Sport

    1.'/catalog' : shows latest added items with categories
    2.'catalog/<sport>/new' : add new sport (protected)
    3.'catalog/<sport>/edit' : edits sport (protected)
    4.'catalog/<sport>/delete' : deletes sport (protected)

#### SportItems

    1.'/catalog/<sport>/item/show' : shows sports items of that sport
    2.'/catalog/item/<sportitem>/view' : shows a sport item (protected)
    3.'/catalog/item/<sportitem>/edit' : edit a sport item (protected)
    4.'/catalog/item/<sportitem>/delete' : delete a sport item (protected)
    5.'/catalog/item/<sportitem>/new' : add a new sport item (protected)

(protected) means you need to login to view, access the page will redirect to Login 

### JSON endpoints

    1.'/catalog/JSON' : returns the present list of sports categories and items
    2.'/catalog/item/<item>/JSON' : returns a Sport item

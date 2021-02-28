# STEPZ

Please find the application [here]https://stepzapp.herokuapp.com/

## Table of Contents
1. [**UX**](#ux)
2. [**Wireframes**](#wireframes)
3. [**Project Goals**](#project-goals )
4. [**User stories**](#user-stories)
5. [**Design Choices**](#design-choices)
6. [**Typography**](#typography)
7. [**Colours**](#colours)
8. [**Imagery**](#imagery)
9. [**Features**](features)
10. [**Landing Page**](#landing-page)
11. [**Navbar**](#navabr)
12. [**Product Page**](#product-page)
13. [**Product Detail Page**](product-detail-page)
14. [**Wishlist Page**](#wishlist-page)
15. [**Shopping Bag Page**](#shopping-page)
16. [**Checkout Page**](#checkout-page)
17. [**Checkout Success Page**](#checkout-success-page)
18. [**Profile Page**](#profile-page)
19. [**Contact Us Page**](#contact-us-page)
20. [**Admin Product Management**](#admin-product-management)
21. [**Django-allauth features**](#django-allauth-features)
22. [**Features left to Implement**](#general-testing)
23. [**Testing**](#testing)
24. [**Functionality**](#functionality)
25. [**Issues**](#technologies-used)
27. [**Technologies Use**](#technologies-used)
28. [**Deployoment**](#deployoment )
29. [**Credits**](#credits)


# UX

### Wireframes
Please view my wireframes here [here](Wireframes/stepzapp-wireframes.pdf) 


## Project Goals

+ Main goal  is for people to be able to find and buy popular aswell as custome made trainers
+ Easy navigation and use of the website on any device 
+ Wishlist section to save trainers that you like for later on 
+ simple and effective way to order from the site
+ easy payment process 


Future goals is existing users of the site would also be able to sell shoes from the platform.

## User stories 

+ Viewing and Navigation

1. shoppers should be able to view the view products and their indivudals details.
2. shoppers  should be able to filter the products by, brand, price and colour.
3. shopper should be able to search their desired products in the search bar. 
4. shopper should be able to easily view bag and total.

+ Registration and User Accounts

1. User site registration should be simple, and user should be able to view their account profile.
2. User logging in and loggin out process should be simple.
3. User should recieve email confirmation after registration to verify account registration.
4. User, profile should contain, user order history and order confrimation,
5. Usher should be able to to view personalised wishlist
6. User passwrd should be easily recovered or reset when lost.

+ Filter and Searching

1. Shoppers should be able to search by using the search bar.
2. Shoppers should be able to  filter trainer by brand, colour and price of choice.

+ Purchasing and Checkout

1. Shoppers should be able to select product quantity when adding to adding to bag.
2. Shoppers should be able to view content in bag, and the total cost of purchase.
3. Shoppers should have the abilty to to remove items from bag.
4. Shoppers should be able to update bag by reducing and increasing quantity of items in bag.
5. Shoppers should be secure in entering their payment details to purchase items.
6. Shopper should be able to view order confirmamtion after checkout.
7. Shopper should recieve order confirmation email.

+ Admin

1. As Admin I want to be able to add new products to shop.
2. As Admin I want the ablity to edit product fields such as price and descriptions.
3. As Admin I wan to be able to delet products completly from the store.

## Design Choices

The goals was to keep the design for this simple and clean.

### Typography

I kept the fonts simple and Used lato and Roboto. I used Roboto fonts for the project logo and then used lato 
for the rest of the fonts. it waas to keep with theme of keeping everthing nice and simple. 

### Colours 

I didn't want to many colour for my projects I wanted to keep to a total of three colours. Those colours were
black, white and mint green. I wanted to green for my logo because it's nice and vibrant and makes the logo stand out
whilst remaining simple. The black and white, black being the colour of the fonts and white colour of the webiste
would balance would bring everthing together. 

### Imagery

I looked at sites such as Nike adn JD to give me an idea on the type of images to use. From the looking at those site
i decided to on what images i would use and how to lay them out. Also using ideas from boutique ado i used a pic image 
of a pair of trainer. All my images are images of trainers just diffrent brands. I included a carousel of trainers and 
called it  top of the steps, the idea behind this is that those are the trainers that are trending on the site. 

## Features 

This site is composed of 7 applications, products, profiles, contact, home, bag, wishlist,checout.

### Landing Page 

the landing page is composed of a Navbar,small summary of what the website is about, and Carousel.
The carousel is to shows case trending shoes on the website. Then landing page is kept simple with minimal information.

### Navbar

The Navbar consists of the a search bar, website logo, shop, bag, and account icon links. The search bar allows you to Search
products that you maybe interested, using product namesor discriptions. The account dropdown allows you to register, log in, log out,
view your profile or wishlist if you're signed in.

### Product Page 

The Product page shows all the product for sale on the website.They include their names and price. The page includes a filter that allows you to filter items by
colour, price and brand making navigation thought the product page easier. If you're signed you can add desired products to
to your wishlist and if you're a super user you able to delete and edit the products.

### Product Detail Page
The product detail page consists of all the details the shoppers need to know about the Product. They include the name,
price descriptions of the shoes, colours and add to bag button.
The page also allows you to choose the size and the number of shoes you want to add to the bag

### Wishlist Page

Customer can save products on a wishlist page for later on.  The customer can choose the shoe size of
the product and the amount they went and send the product to the shopping bag. They are
given the options to remove items from their wishlist.


### Shopping Bag 

The shopping bag page stores the shoppers' products. It also allows you to adjust the quantity with the quantity and update button. 
The shopper can remove the item from the bag with the remove button. There are keep shopping and the secure checkout button to either
send the customer back to the products page or continue shopping

### Checkout Page 

The checkout page allows you to fill in the information needed to secure checkout and purchase your items. Customers can save their
delivery information the next time they're filled in automatically. Customer can also see their order summary on the side.
Customers don't need to be registered to be able to checkout.   A message is displayed asking if you'd like to sign up.

### Checkout Success Page 

Customers are directed to the customer checkout success page. Where they can view their order details. 
They are given the options to keep shopping and go back to the products page.

### Profile Page 

The Profile page contains the customer's details and order history. The customer can update their order details for future
reference. You can only access the My profile page if you are registered.


### Contact Us page 

The contact us page allows the customer to send the website a message they would like to ask any questions. 
You are then taken to the contact success page where you are given the options to go back to the home page.

### Admin Product Management

This page is only available to superusers. It allows you to add, delete and edit products of your choice.

### Django-allauth features
Base template for allauth has Back to Home button at the end of the page, for easy navigation for users.
Sign Up: The users will be asked to fill out E-mail, User Name and Password to create an account. When the sign up form is submitted, a verification email will be sent to the user's
email address to complete the sign up process.
Log In: Users will be asked to input User Name or Email, and Password to login. If the user successfully logged in, a success message will pop up and redirect to the landing page.
Log out: Log out page is accessible from the site menu. After the user successfully signed out button on the sign out page, a success message will appear and redirect to the landing page.
Forgot password: Forgot password page is accessible from Sign In page. Users will be asked to put in an email address which they have used for their registration to the site. An email with a link to reset the password will be sent after submitting the form.
@https://github.com/AsunaMasuda/FloweryDays



## Features left to Implement

There are quite a few features I'd like to implement after I've gotten a better understanding of how to use Django.
Although I mostly used the features shown to me by boutique ado. I'd like to turn this into a platform where users can also 
sell their Trainer, whether they are custom trainer they made themselves or shoes they've bought similar to Depop.


## Allow Users to Sell products

I want users that are registered to be able to sell their products own on the website.


### Message app 

I want to add a messaging app where the user can privately message each other. This will go along well  with 
the feature of allowing users to sell items themselves they need to able to communicate.

### Add a Rating system

I won't allow users to be able to rate items they've bought to their satisfaction. If other users are also selling
products, I want users to rate their items. Then the rating is assigned to said users. This allows users to identify
those they sell good products.

### Social Account Login

Want users to be able to use their social account to register to the site. which would increase the number of users on the site 
as it is quicker than adding your details.



## Testing 

All Test for the app were done manually using google dev tools and also heroku when then app was deployed.

### Responsivness 

Testing the Respsonsive of the site was done mainly on google dev tools. the repsonsivness of the home page,, profiles and 
contact page where good. Howevere intially the bag, wishlst and contact page all had issues with showing the products fitting on 
one screen. I had to change the intial layout of the table to make it repsonsive on one screen.



### Functionality 

I tested the functionality of each page using the initial user story.

#### Landing page 
- As a Customer, I want to know what services I am being offered. Then be able to simply navigate from one page to another.
- test conducted, clicked on all the icons, which leads to all the correct links.
- Passed all tests in terms of functionality and easy navigation.

#### Product Page
- As a customer, I want to view products available and filter the products to suit my needs
- test all the filters, by filter by colour and products, and brand and the products that fit the description appear.
- Passed all filters work, customers can sort as desired.
-  In the future, I would like to allow customers to apply more than one filter at a time.

#### Product Detail Page 
- A a customer I would like the products page to showcase all the details of the selected product. Customers should be able to select the item quantity and size then adds it to the bag.
- Tested the functionality by adding items to the bag, selecting a different quantity of items, shoe size.
- Passed all 

#### Wishlist 
- if the customer is authenticated they should be able to save the wishlist. They should be able to remove the item from the wishlist or add it to the bag.
- Tested by adding things to the wishlist when signed out. This did not allow me to complete the action. When logged in I was allowed to save, remove and add items to the bag.
- Passed all

#### Shopping bag 
- customer should be able to view inside the shopping and seeing the item selected inside with the quantity and size chosen. 
they should be able to update and remove the items if they choose. They also have the choice to checkout.
- test all these functionalities by completing the steps, removing and updating items in the bag.
- Passed all


####  Checkout Page
- Customer should be able to enter their details, view their order summary, save their details if desired
 and securely checkout.
- Test this by attempting to buy something entering my details and checking out. I was taken the checkout success page
- Passed all tests 

#### Contact Page 

- Customer should be able to send a  message and directed to the contact success page thanking them for their message.
- sent a message and directed to the customer success page.
- Passed all test 

#### Profile page 
- if  a user is authenticated they should see their order history and saved details if they have bought something and saved their details.
- tested this buying an item so I could view order history and saving my info for later on to auto-filled.
- Passed all tests.

#### Register,Sign in page.
- Users should be able to log in, signup easily to the website.
- User is sent an email to verify their account. 
- Tested by creating an account to send a confirmation and had to verify the account. Then it was easy to sign in afterwards.
- Passed all tests.

## Issues

- In the beginning, when creating some of my models I accidentally delete my migration and had to start my whole project again
luckily I hadn't done much.
- Issues with my wishlist, when creating my wishlist I complication how my wishlist my having to models and confusing myself on how to create the relationship between my wishlist and products. I solved this issue by reading up on many to many 
relationship and with the help of my tutor, I was able to simplify my model and crated my wishlist app.
- The update and remove button weren't working in the beginning when the javascript id was placed in the buttons class.When I moved 
them the icon class and id they started working.
- when at first I didn't want to go with the free delivery threshold, however, I couldn't figure out how to make my grand total and 
the delivery total appears so I just followed the boutique ado tutorial to fix it.
- There's still an issue with the footer floating but I am unsure on how to fix it as of right now.
- most of my issues had to do with my not understanding how the models and their fields were supposed to go together, but in the end 
with help of tutor support and my mentor, I began to get a better understanding. 

## Technologies Used

### Libraries and Packages

1. HTML, CSS and Javascript Progamming languages 
2. [Django](https://www.djangoproject.com/)
3. [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
4. [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)
5. [Bootstrap (v4.4.1)](https://www.bootstrapcdn.com/)
6. [JQuery](https://jquery.com/)
7. [JQuery-UI](https://jqueryui.com/)
8. [Popper.js](https://popper.js.org/)
9. [Font Awesome](https://fontawesome.com/)
10. [Stripe](https://stripe.com/ie)
11. [Google Fonts](https://fonts.google.com/)
12. [Unsplash](https://unsplash.com/)- for Product images

### Git/GitHub
1. Gitpod
2. [PIP](https://pip.pypa.io/en/stable/installing/)
3. [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
4. [dbdiagram.io](https://dbdiagram.io/home)
5. [AWS S3 bucket](https://aws.amazon.com/)

### Databases
1. [SQlite3](https://www.sqlite.org/index.html)- database used for development.
3.  [PostgreSQL](https://www.postgresql.org/) - database used for production.

## Deployoment 

### Heroku Deployment with AWS
This website is deployed on [Heroku](https://www.heroku.com/), following these steps:
1. Install these packages to your local environment, since these packages are required to deploy a Django project on Heroku.
- [gnicorn](https://gunicorn.org/): `gnicorn` is Python WSGI(web server gataway interface) server for UNIX.
- [gninx](https://www.nginx.com/): `gninx` is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server.
- [psycopg2-binary](https://pypi.org/project/psycopg2-binary/): `psycopg2-binary` is PostgreSQL database adapter for the Python programming language.
- [dj-database-url](https://pypi.org/project/dj-database-url/): `dj-database-url` allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.
2. Create a `requirements.txt` file and freeze all the modules with the command `pip3 freeze > requirements.txt` in the terminal.
3. Create a `Procfile` write `web: gunicorn boutique_ado.wsgi:application` in the file.
4. `git add` and `git commit` and `git push` all the changes to the Github repositoty of this project.
5. Go to Heroku and create a **new app**. Set a name for this app and select the closest region (Europe) and click **Create app**.
6. Go to **Resources** tab in Heroku, then in the **Add-ons** search bar look for **Heorku Postgres**(you can type postgres), select **Hobby Dev — Free** and click **Submit Order Form** button to add it to your project.
7. In the heroku dashboard for the application, click on **Setting** > **Reveal Config Vars** and set the values as follows:

| Key | Value |
| ----------- | ----------- |
| AWS_ACCESS_KEY_ID | `Your AWS Access Key` |
| AWS_SECRET_ACCESS_KEY | `Your AWS Secret Access Key` |
| DATABASE_URL | `Your Postgres Database URL` |
| EMAIL_HOST_PASS | `Your Email Password (generated by Gmail)` |
| EMAIL_HOST_USER | `Your Email Address` |
| SECRET_KEY | `Your Secret Key` |
| STRIPE_PUBLIC_KEY | `Your Stripe Public Key` |
| STRIPE_SECRET_KEY | `Your Stripe Secret Key` | 
| STRIPE_WH_SECRET | `Your Stripe WH Key` |
| USE_AWS | `True` |

8. Comment out the current database setting in settings.py, and add the code below instead. This is done temporarily to migrate the datbase on Heroku.
```
  DATABASES = {     
        'default': dj_database_url.parse("<your Postrgres database URL here>")     
    }
```
9. Migrate the database models to the Postgres database using the following commands in the terminal:
`python3 manage.py migrate`
10. Load the data fixtures(color_table, flower_table, image_table, product_table) into the Postgres database using the following command:
`python3 manage.py loaddata <fixture_name>`
11. Create a superuser for the Postgres database by running the following command:
`python3 manage.py createsuperuser`
12. Replace the database setting with the code below, so that the right database is used depending on development/deployed environment.
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
13. Disable collect static, so that Heroku won't try to collect static file with: `heroku config:set DISABLE_COLLECTSTATIC=1`
14. Add `'stepzapp.herokuapp.com', 'localhost', '127.0.0.1'` to `ALLOWED_HOSTS` in settings.py.
```
ALLOWED_HOSTS = ['flowerydays.herokuapp.com', 'localhost', '127.0.0.1']
```
15. In Stripe, add Heroku app URL a new webhook endpoint.
16. Update the settings.py with the new Stripe environment variables and email settings.
17. Commit all the changes to Heroku. Medial files are not connected to the app yet but the app should be working on Heroku.

### Amazon Web Service S3
The static files and media files for this deployed site (e.g. image files for product/blog) are hosted in the [AWS](https://aws.amazon.com/) S3 Bucket. You will need to create S3 bucket, complete the setting up and upload static files and media files to the S3 bucket. You can find [Amazon S3 documentation](https://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html) for more information on the setting.
I used CORS configuration below:
```
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
```

- Setting for static/media files in settings.py
1. Install `boto3` and `django-storages` with a command `pip3 install boto3` and `pip3 install django-storages` in your terminal, to connect AWS S3 bucket to Django.
2. Add 'storages' to `INSTALLED_APPS` in settings.py.
3. Add the following in settings.py.
```
if 'USE_AWS' in os.environ:
    # Cache Control
    AWS_S3_OBJECT_PARAMETERS = {
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl': 'max-age=94608000',
    }

    # Bucket Config
    AWS_STORAGE_BUCKET_NAME = 'flowerydays'
    AWS_S3_REGION_NAME = 'eu-west-1'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3-eu-west-1.amazonaws.com'

    # Static and media files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
```
5. Add [custom_storages.py](https://github.com/AsunaMasuda/FloweryDays/blob/master/custom_storages.py).
6. Delete DISABLE_COLLECTSTATIC from Heroku Config Var.
7. Push all the changes to Github/Heroku and all the static files will be uploaded to S3 bucket.
By setting up above, Heroku will run python3 manage.py collectstatic during the build process and look for static and media files.

### Automatic Deploy on Heroku
You can enable automatic deploy in the following steps that pushes update to Heroku everytime you push to github.
1. Go to Deploy in Heroku dashboard.
2. At `Automatic deploys`, choose a github repository you want to deploy.
3. Click `Enable Automatic Deploys`.


## Local Deployment
For local deployment, you need to have an IDE (I used Gitpod for this project) and you need to install the following:
- Git, Python3, PIP3
Also, you need to create account in the following services if you don't own yet:
- Stripe, AWS (S3 bucket), Gmail

1. In the IDE you are using, copy and paste the following commane into the terminal to clone this repository.
    `git clone https://github.com/Tabita99/STEPZ.git`
(the other ways to clone a repository are written in this [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository))
2. Set up environment variable in your selected IDE, or you can create `.env` file in your root directory and add `.env` to `.gitignore` file, and add the followings to the `.env` file.
```
import os  
os.environ["DEVELOPMENT"] = "True"    
os.environ["SECRET_KEY"] = "<Your Secret Key>"
os.environ["STRIPE_PUBLIC_KEY"] = "<Your Stripe Public Key>"    
os.environ["STRIPE_SECRET_KEY"] = "<Your Stripe Secret Key>"    
os.environ["STRIPE_WH_SECRET"] = "<Your Stripe WH Secret Key>"    
```
3. Install all the required packages with `pip3 install -r requirements.txt`
4. Migrate the models to crete a database using in your IDE with `python3 manage.py makemigrations` and `python3 manage.py migrate`
5. Load the data fixtures(color_table, flower_table, image_table, product_table) into the database using the following command:
`python3 manage.py loaddata <fixture_name>`
6. Create a superuser for the Postgres database by running with `python3 manage.py createsuperuser`
7. Now you can access the app using the command `python3 manage.py runserver`
@https://github.com/AsunaMasuda/FloweryDays#heroku-deployment-with-aws

## Credits

### content

* README, website code examples and deploying instruction taken from https://github.com/AsunaMasuda/FloweryDays and 
 https://github.com/ceciliabinck/taste-world-snacks 
 and Code on Boutique-Ado project

### Acknowledgement

I would like to thank :
The tutors at code institute for their help
My mentor Antonio Rodriguez



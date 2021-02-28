# UX

## Project goals

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

### checkout Success Page 

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
10. [Animate.css](https://animate.style/)
11. [Wow.js](https://www.delac.io/wow/)
12. [Stripe](https://stripe.com/ie)
13. [Google Fonts](https://fonts.google.com/)

### Git/GitHub
1. Gitpod
2. [PIP](https://pip.pypa.io/en/stable/installing/)
3. [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)
4. [dbdiagram.io](https://dbdiagram.io/home)
5. [AWS S3 bucket](https://aws.amazon.com/)

## Databases
1. [SQlite3](https://www.sqlite.org/index.html)- database used for development.
3.  [PostgreSQL](https://www.postgresql.org/) - database used for production.

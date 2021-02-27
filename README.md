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











